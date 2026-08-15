
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from database import SessionLocal
from models import SimulationRun

# Request model for creating a simulation run
class SimulationRunCreate(BaseModel):
    name: str
    parameters: dict

# Request model for updating a simulation run
class SimulationRunUpdate(BaseModel):
    name: str | None = None
    parameters: dict | None = None

# Create a database session for the request and ensure it is closed when the request finishes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Launch the API
app = FastAPI()

# API route to get all stored runs
@app.get("/runs")
def get_runs(db=Depends(get_db)):
    result = db.execute(select(SimulationRun)).scalars()
    runs = list(result)
    return runs

# API route to get a specific run via its ID
@app.get("/runs/{run_id}")
def get_run(run_id: int, db=Depends(get_db)):
    result = db.get(SimulationRun, run_id)
    if result is None:
        raise HTTPException(
            status_code = 404,
            detail = "Run not found."
        )
    return result

# API route to create and store a simulation object
@app.post("/runs")
def create_run(run: SimulationRunCreate, db = Depends(get_db)):
    new_run = SimulationRun(
        name = run.name,
        parameters = run.parameters
    )
    db.add(new_run)
    db.commit()
    db.refresh(new_run)
    return new_run

# API route to update a specific run's data via its ID
@app.patch("/runs/{run_id}")
def update_run(run_id: int, run: SimulationRunUpdate, db=Depends(get_db)):
    result = db.get(SimulationRun, run_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Run not found."
        )

    if run.name != None:
        result.name = run.name

    if run.parameters != None:
        result.parameters = run.parameters

    db.commit()
    db.refresh(result)

    return result

# API route to delete a specific simulation run via its ID
@app.delete("/runs/{run_id}")
def delete_run(run_id: int, db=Depends(get_db)):
    result = db.get(SimulationRun, run_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Run not found."
        )

    db.delete(result)
    db.commit()

    return {"message": "Simulation successfully deleted"}
