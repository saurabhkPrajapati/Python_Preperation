from database import SessionLocal
from models import User
from sqlalchemy.orm import scoped_session

# Prevents multiple threads from interfering with each other's database transactions.
# Ensures each thread/request in a Flask API gets an isolated session, preventing race conditions
# Automatically manages session creation and cleanup.
db_session = scoped_session(SessionLocal)

# Find user by name
user = db_session.query(User).filter_by(name="Alice").first()
if user:
    user.age = 26  # Update age
    db_session.commit()
    print("User updated!")

