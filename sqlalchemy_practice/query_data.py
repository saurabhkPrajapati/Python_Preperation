from database import SessionLocal
from models import User
from sqlalchemy.orm import scoped_session

db_session = scoped_session(SessionLocal)

# Fetch all users
users = db_session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
