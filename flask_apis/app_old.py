from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy.orm import scoped_session
from database import SessionLocal, engine
from models import User
from schemas_validation import user_schema, ValidationError

app = Flask(__name__)
api = Api(app)

# Create a scoped session
session = scoped_session(SessionLocal)

# Prevents multiple threads from interfering with each other's database transactions.
# Ensures each thread/request in a Flask API gets an isolated session.
# Automatically manages session creation and cleanup.

class UserResource(Resource):
    
    # Create User (POST)
    def post(self):
        # data = request.get_json()
        data = user_schema.load(request.get_json())
        new_user = User(name=data["name"], email=data["email"])
        session.add(new_user)
        session.commit()
        return {"message": "User created", "user": new_user.to_dict()}, 201

    # Get All Users (GET)
    def get(self):
        users = session.query(User).all()
        return [user.to_dict() for user in users], 200

class SingleUserResource(Resource):

    # Get a Single User (GET)
    def get(self, user_id):
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        return user.to_dict(), 200

    def put(self, user_id):
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        
        data = request.get_json()
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        session.commit()
        
        return {"message": "User updated", "user": user.to_dict()}, 200
    
    def patch(self, user_id):
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404

        data = request.get_json()
        if "email" in data:
            user.email = data["email"]
            session.commit()
            return {"message": "Email updated", "user": user.to_dict()}, 200
        else:
            return {"message": "Email field is required for update"}, 400
    
    def delete(self, user_id):
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        
        session.delete(user)
        session.commit()
        return {"message": "User deleted"}, 200

api.add_resource(UserResource, '/users')
api.add_resource(SingleUserResource, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
