import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get the absolute path of the database file
# db_path = os.path.abspath("oxyzen.db")
current_path = os.path.abspath(__file__)

# Get the directory name of the database
db_directory = os.path.dirname(current_path)

print("Database Directory:", db_directory)

# Create database engine (SQLite example)
# create_engine is used to create a connection to the database.
# It establishes communication between SQLAlchemy and the database (in this case, SQLite).
DATABASE_URL = f"sqlite:///{db_directory}\\oxyzen.db"

# create_engine creates and manages the database connection.
# sessionmaker create sessions on engine. Transactions are executed within a Session.
engine = create_engine(
    DATABASE_URL,
    echo=True,              # show SQL (interview bonus)
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# ORM base class
# It is the base class that is used to define ORM models and it links Python classes to database tables.
Base = declarative_base()
