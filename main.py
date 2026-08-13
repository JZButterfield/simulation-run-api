
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from database import SessionLocal
from models import SimulationRun

class SimulationRunCreate(BaseModel):
    name: str
    parameters: dict

class SimulationRunUpdate(BaseModel):
    name: str | None = None
    parameters: dict | None = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/runs/{run_id}")
def get_run(run_id: int, db=Depends(get_db)):
    result = db.get(SimulationRun, run_id)
    if result is None:
        raise HTTPException(
            status_code = 404,
            detail = "Run not found."
        )
    return result

@app.get("/runs")
def get_runs(db=Depends(get_db)):
    result = db.execute(select(SimulationRun)).scalars()
    runs = list(result)
    return runs

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