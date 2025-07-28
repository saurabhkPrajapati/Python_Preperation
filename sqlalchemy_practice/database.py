import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
# sessionmaker is used to create session objects, which allow us to interact with the database (insert, update, delete, query).
SessionLocal = sessionmaker(bind=engine)
