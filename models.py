from sqlalchemy import Column, Integer, String, JSON, Enum, DateTime
from sqlalchemy.sql import func
from database import Base

# Create the simulation run class
class SimulationRun(Base):
    # Add a table name for SQLAlchemy
    __tablename__ = "simulation_runs"
    # Create the ID and make it the primary key, autoincrements already
    id = Column(Integer, primary_key=True)
    # Create the simulation name, limited to 100 characters
    name = Column(String(100))
    # Create the parameters, set to JSON database type
    parameters = Column(JSON)
    # Create the results, set to JSON database type
    results = Column(JSON)
    # Create the simulation status value and restrict the options
    status = Column(Enum("queued","running", "complete", "failed", name = "simulation_status"), default="queued")
    # Create the created at information using SQL function for datetime
    created_at = Column(DateTime, server_default=func.now())
    # Create the updated at infromation time and the auto update 
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())