from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# declarative_base() → Creates a base class that all models will inherit from.
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

