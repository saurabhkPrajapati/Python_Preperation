from database import engine
from models import Base

# create db.sqlite. and all the tables in it
# It creates table only if it doesn't exist
Base.metadata.create_all(engine)


# Looks at all ORM models that inherit from Base
# Collects their table definitions (__tablename__, columns, constraints)
# Creates tables that do NOT already exist

# Metadata = Blueprint / Schema Definition
# Metadata stores the structure (schema) of database table
# It contains: Table names, Columns, Data types, Primary keys, Foreign keys, Constraints, Indexes