from functools import wraps
from flask_jwt_extended import get_jwt, get_jwt_identity
from flask import jsonify

def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()   # STRING
            print("JWT identity inside decorator:", user_id)
            claims = get_jwt()     
            print("******", claims)        # DICT
            role = claims.get("role")
            if role not in roles:
                return jsonify({"error": "Unauthorized"}), 403
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
