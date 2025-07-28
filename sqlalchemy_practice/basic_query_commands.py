from database import SessionLocal
from models import User
from sqlalchemy.orm import scoped_session
from sqlalchemy import func

db_session = scoped_session(SessionLocal)

# Get All Records
users = db_session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

# Get First Record
user = db_session.query(User).first()
print(user.name, user.age)

# Get Record by ID
user = db_session.query(User).filter(User.id == 1).first()
print(user.name, user.age)

# Filtering with Conditions
user = db_session.query(User).filter(User.name == "Alice").first()
print(user.age)

# Not Equal (!=)
users = db_session.query(User).filter(User.name != "Alice").all()
for user in users:
    print(user.name)

# LIKE (like) → Case-sensitive search
users = db_session.query(User).filter(User.name.like("A%")).all()  # Names starting with 'A'
for user in users:
    print(user.name)

# ILIKE (ilike) → Case-insensitive search
users = db_session.query(User).filter(User.name.ilike("a%")).all()  # Matches 'Alice', 'alice'
for user in users:
    print(user.name)

# IN (in_) → Match multiple values
users = db_session.query(User).filter(User.name.in_(["Alice", "Bob"])).all()
for user in users:
    print(user.name)

# NOT IN
users = db_session.query(User).filter(~User.name.in_(["Alice", "Bob"])).all()
for user in users:
    print(user.name)

# Greater Than (>) & Less Than (<)
users = db_session.query(User).filter(User.id > 1).all()
for user in users:
    print(user.name)

# Between
users = db_session.query(User).filter(User.id.between(1, 2)).all()
for user in users:
    print(user.name)

# Contains (contains)
users = db_session.query(User).filter(User.age.contains("example")).all()
for user in users:
    print(user.age)

# Ascending Order (asc())
users = db_session.query(User).order_by(User.name.asc()).all()
for user in users:
    print(user.name)

# Descending Order (desc())
users = db_session.query(User).order_by(User.name.desc()).all()
for user in users:
    print(user.name)

# ________________________________________________________________________________________________________________________________________

# Count Total Users
user_count = db_session.query(func.count(User.id)).scalar()
print("Total Users:", user_count)

# //// Using .scalar() (Returns a single value) \\\\

# Find the Oldest and Youngest User
oldest_age = db_session.query(func.max(User.age)).scalar()
youngest_age = db_session.query(func.min(User.age)).scalar()
print(f"Oldest Age: {oldest_age}, Youngest Age: {youngest_age}")

# Get the Average Age of Users
average_age = db_session.query(func.avg(User.age)).scalar()
print(f"Average Age: {average_age}")
