from models import SimulationRun
from database import SessionLocal

current_session = SessionLocal()

test_sim = SimulationRun(name = "test_simulation",
                         parameters = {"Speed": 100,
                          "Acceleration": 10,
                          "Time": 5},
                          results = {"Displacement": 637})

current_session.add(test_sim)
current_session.commit()

test_fetch = current_session.get(SimulationRun, test_sim.id)

print(test_fetch.name)
print(test_fetch.parameters)
print(test_fetch.results)
print(test_fetch.status)