import sqlite3
from database import get_db
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from decorators import role_required
from datetime import timedelta

auth_bp = Blueprint("auth", __name__)


# SIGN UP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    db = get_db()
    cur = db.cursor()

    try:
        cur.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (data["name"], data["email"], generate_password_hash(data["password"]))
        )
        db.commit()
        return jsonify({"message": "User created"}), 201
    except sqlite3.IntegrityError:
        # This triggers if email is already in the database
        return jsonify({"message": "User already exists. Please login."}), 200
    finally:
        db.close()


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "SELECT id, password_hash, role FROM users WHERE email=?",
        (data["email"],)
    )
    user = cur.fetchone()

    if not user or not check_password_hash(user[1], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity=str(user[0]),
                                       expires_delta=timedelta(hours=1),
                                       additional_claims={"role": user[2]})
    print(access_token)
    return jsonify({"access_token": access_token}), 200


# USER ROUTE
@auth_bp.route("/user", methods=["GET"])
@jwt_required()
@role_required(["user", "admin", "super_admin"])
def user_dashboard():
    return jsonify({"message": "User access granted"})


# ADMIN ROUTE
@auth_bp.route("/admin")
@jwt_required()
@role_required(["admin", "super_admin"])
def admin_dashboard():
    return jsonify({"message": "Admin access granted"})


