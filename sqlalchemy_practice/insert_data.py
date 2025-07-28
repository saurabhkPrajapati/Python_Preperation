from database import SessionLocal
from models import User
from sqlalchemy.orm import scoped_session

# Prevents multiple threads from interfering with each other's database transactions.
# Ensures each thread/request in a Flask API gets an isolated session, preventing race conditions
# Automatically manages session creation and cleanup.
db_session = scoped_session(SessionLocal)

# Add new users
user1 = User(name="Alice", age=2)
user2 = User(name="Bod", age=1)

db_session.add(user1)
db_session.add(user2)
# db_session.add_all([user1, user2])

# Commit changes
db_session.commit()

print("Users added successfully!")
