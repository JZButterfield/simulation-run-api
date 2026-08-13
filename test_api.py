from fastapi.testclient import TestClient
from main import app, get_db
from test_database import TestSessionLocal


client = TestClient(app)

def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_create_run():
    response = client.post(
        "/runs",
        json={
            "name": "test_from_pytest",
            "parameters": {
                "speed": 100,
                "time": 5
            }
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "test_from_pytest"

def test_get_runs():
    response = client.get("/runs")

    assert response.status_code == 200
    assert len(response.json()) > 0