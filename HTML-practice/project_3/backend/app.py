import os
from flask import Flask, render_template, send_from_directory
from flask_jwt_extended import JWTManager
from auth import auth_bp
from database import init_db

# Initialize DB at startup
init_db()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "../frontend"))

# JWT setup
app.config["JWT_SECRET_KEY"] = "secret123"

jwt = JWTManager(app)

# Register blueprint
app.register_blueprint(auth_bp)

# ----------------- STATIC FILES -----------------
@app.route('/css/<path:filename>')
def css_files(filename):
    return send_from_directory(os.path.join(BASE_DIR, "../frontend/css"), filename)

@app.route('/js/<path:filename>')
def js_files(filename):
    return send_from_directory(os.path.join(BASE_DIR, "../frontend/js"), filename)

# ---------- FRONTEND ROUTES ----------

# Landing page (Login / Sign-up options)
@app.route("/")
def home():
    return render_template("home.html")

# Login page
@app.route("/login")
def login_page():
    return render_template("login.html")

# Signup page
@app.route("/signup")
def signup_page():
    return render_template("signup.html")

# User dashboard
@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

# Admin dashboard
@app.route("/admin")
def admin_page():
    return render_template("admin.html")

# ------------------------------------

from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return {"msg": f"Invalid token: {reason}"}, 422

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return {"msg": "Token has expired"}, 422

@jwt.unauthorized_loader
def missing_token_callback(reason):
    return {"msg": f"Missing token: {reason}"}, 401

if __name__ == "__main__":
    app.run(debug=True)
