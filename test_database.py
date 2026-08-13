import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from database import Base
from models import SimulationRun

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

TEST_DATABASE_URL = DATABASE_URL.replace(
    "simulation_runs",
    "simulation_runs_test"
)

test_engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(bind=test_engine)

Base.metadata.create_all(bind=test_engine)