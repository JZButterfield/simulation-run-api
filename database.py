import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Python loads the .env file and its variables
load_dotenv()
# Assigns the "DATABASE_URL value from the .env to the variable DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Creates the engine using the connection URL
engine = create_engine(DATABASE_URL)

# Create the session factory
SessionLocal = sessionmaker(bind=engine)

# Base class for database models
Base = declarative_base()