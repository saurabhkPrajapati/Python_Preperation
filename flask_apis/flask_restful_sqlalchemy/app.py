from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api
from sqlalchemy.orm import scoped_session
from database import SessionLocal, engine
from models import User, Registration
from schemas_validation import user_schema, registration_schema
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from datetime import timedelta
from logger import logger_singleton

app = Flask(__name__)
api = Api(app)

# Global error handler for 400 - Bad Request
@app.errorhandler(400)
def handle_bad_request_error(error):
    return jsonify({"error": "Bad request - Invalid data or missing fields"}), 400

# Global error handler for 404 - Resource not founds
@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({"error": "Resource not founds"}), 404

# Global error handler for 500 - Internal server error
@app.errorhandler(500)
def handle_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Secret Key for JWT
# app.config["JWT_SECRET_KEY"] = "your_secret_key"  # Change this in production

app.config['SECRET_KEY'] = 'your_unique_secret_key'

# Initialize JWT
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Create a scoped DB session
db_session = scoped_session(SessionLocal)

# Prevents multiple threads from interfering with each other's database transactions.
# Ensures each thread/request in a Flask API gets an isolated session, preventing race conditions
# Automatically manages session creation and cleanup.

# call logger
request_logger = logger_singleton.get_request_logger("123")


# User Registration
class Register(Resource):
    def post(self):
        data = registration_schema.load(request.get_json()) # for data validation using user_schema (using marshmallow library)
        username = data.get("username")
        password = data.get("password")

        existing_user = db_session.query(Registration).filter_by(username=username).first()
        if existing_user:
            return {"error": "User already exists"}, 400

        # hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8") 
        new_user_registration = Registration(username=username, password=hashed_password)
        db_session.add(new_user_registration)
        db_session.commit()

        return {"message": "User registered successfully"}, 201


# User Login & Token Generation
class Login(Resource):
    def post(self):
        data = registration_schema.load(request.get_json()) # for data validation using user_schema (using marshmallow library)
        username = data.get("username")
        password = data.get("password")

        logger_singleton.console_logger.info(f"Request received from {request.remote_addr}")
        request_logger.info(f"username:{username}, password: {password}")

        registration = db_session.query(Registration).filter_by(username=username).first()
        if not registration or not bcrypt.check_password_hash(registration.password, password):
            return {"error": "Invalid username or password"}, 401
        
        # Store registration ID in the session
        session['registration_id'] = registration.id  
        session["logged_in"] = True
        #session data will be stored in a cookie that does not get deleted when the browser is closed
        session.permanent = True 
        app.permanent_session_lifetime = timedelta(minutes=1)  # Optional: Set session expiration time

        # Generate JWT access token (used for stateless authentication)
        # (you don’t need to store user state on the server), which is scalable.
        access_token = create_access_token(identity=str(registration.id))

        # access_token = create_access_token(identity=str(registration.id), expires_delta=timedelta(minutes=30))
        
        return {"message": "Login successful", "access_token": access_token}, 200


class UserResource(Resource):
    # Create User (POST)
    def post(self):
        try:
            # data = request.get_json()
            data = user_schema.load(request.get_json()) # for data validation using user_schema (using marshmallow library)
            new_user = User(name=data["name"], email=data["email"])
            db_session.add(new_user)
            db_session.commit()
            return {"message": "User created", "user": new_user.to_dict()}, 201
        except ValidationError as e:
            return {"error": e.messages}, 400  # 👈 Return a 400 error

    
    # Get All Users (GET)
    @jwt_required()
    def get(self):
        print(session["registration_id"])
        if 'registration_id' not in session:
            return {"error": "Session expired or not authenticated"}, 401
        users = db_session.query(User).all()
        return [user.to_dict() for user in users], 200


class SingleUserResource(Resource):
    # Get a Single User (GET)
    @jwt_required()
    def get(self, user_id):
        user = db_session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        return user.to_dict(), 200

    def put(self, user_id):
        user = db_session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        
        data = request.get_json()
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        db_session.commit()
        
        return {"message": "User updated", "user": user.to_dict()}, 200
    
    def patch(self, user_id):
        user = db_session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404

        data = request.get_json()
        if "email" in data:
            user.email = data["email"]
            db_session.commit()
            return {"message": "Email updated", "user": user.to_dict()}, 200
        else:
            return {"message": "Email field is required for update"}, 400
    
    def delete(self, user_id):
        user = db_session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        
        db_session.delete(user)
        db_session.commit()
        return {"message": "User deleted"}, 200


class UsersPaginationResource(Resource):
    def get(self):
        """Paginate and fetch users"""
        try:
            # Get query parameters (defaults if not provided)
            start_page = int(request.args.get("start_page", 1))
            per_page = int(request.args.get("per_page", 2))  # Default: 10 users per page

            # Ensure pagination parameters are valid
            if start_page < 1 or per_page < 1:
                return {"error": "Invalid pagination parameters"}, 400

            # Fetch paginated users
            users_query = db_session.query(User)
            total_users = users_query.count()  # Total count before pagination
            users = users_query.offset((start_page - 1) * per_page).limit(per_page).all()

            return {
                "start_page": start_page,
                "per_page": per_page,
                "total_users": total_users,
                "total_pages": (total_users + per_page - 1) // per_page,  # Total pages
                "users": [user.to_dict() for user in users]  # Convert users to dictionary
            }, 200
        except Exception as e:
            return {"error": str(e)}, 500


api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(UserResource, '/users')
api.add_resource(SingleUserResource, '/users/<int:user_id>')
api.add_resource(UsersPaginationResource, "/users/page")


if __name__ == '__main__':
    app.run(debug=True)

