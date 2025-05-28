from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLite engine
engine = create_engine("sqlite:///app.db", echo=False)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Create a Base class for models to inherit from
Base = declarative_base()
