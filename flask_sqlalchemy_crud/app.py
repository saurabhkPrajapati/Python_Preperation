from flask import Flask, request, jsonify
from database import SessionLocal
from models import User

# __name__ helps Flask locate templates/static files
# Creates WSGI application object
app = Flask(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()


# SQLAlchemy expires ORM objects on commit(), NOT on close()

# db.commit(): orm Objects expire
# db.close(); Session closes, but already-loaded orm objects remain accessible 

@app.route("/users", methods=["POST"])
def create_user():
    db = SessionLocal()
    data = request.json

    user = User(
        name=data["name"],
        email=data["email"]
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()
    return jsonify({"id": user.id, "message": "User created"}), 201
# jsonify converts Python data into a JSON response with correct headers.


@app.route("/users", methods=["GET"])
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()

    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()

    if not user:
        return {"error": "User not found"}, 404

    return jsonify({"id": user.id, "name": user.name, "email": user.email})


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    db = SessionLocal()
    data = request.json

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        db.close()
        return {"error": "User not found"}, 404

    user.name = data["name"]
    user.email = data["email"]
    db.commit()
    db.close()

    return {"message": "User updated"}, 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        db.close()
        return {"error": "User not found"}, 404

    db.delete(user)
    db.commit()
    db.close()

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
