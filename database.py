import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Python loads the .env file and its variables
load_dotenv()
# Read the database connection URL from the environment so credentials aren't hard-coded
DATABASE_URL = os.getenv("DATABASE_URL")

# Creates the engine using the connection URL
engine = create_engine(DATABASE_URL)

# Create the session factory
SessionLocal = sessionmaker(bind=engine)

# Base class for database models
Base = declarative_base()