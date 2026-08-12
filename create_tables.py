from database import engine, Base
from models import SimulationRun

Base.metadata.create_all(bind=engine)