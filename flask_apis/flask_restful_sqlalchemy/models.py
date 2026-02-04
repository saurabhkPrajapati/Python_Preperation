from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# declarative_base() → Creates a base class that all models will inherit from.
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}