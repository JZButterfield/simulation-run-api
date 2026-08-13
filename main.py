
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from sqlalchemy import select
from database import SessionLocal
from models import SimulationRun

class SimulationRunCreate(BaseModel):
    name: str
    parameters: dict

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