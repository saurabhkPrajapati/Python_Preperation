from database import engine
from models import Base

# create db.sqlite. and all the tables in it
Base.metadata.create_all(engine)
