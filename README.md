## Overview

The project stores simulation data in a database. Data stored includes: id, name, parameters, results, status, created_at and updated_at.
The API provides endpoints for creating, retrieving, updating and deleting simulation runs.
The project demonstrates: Python, APIs, Docker and deployment with Railway.


## Tech Stack

* **Python** — Base programming language
* **FastAPI** — Web framework used to create the API and endpoints
* **PostgreSQL** — Relational database used to store simulation data
* **SQLAlchemy** — Python library used to interact with the database
* **Docker** — Packages the application and its dependencies into a container
* **Pytest** — Testing framework used for automated tests
* **Railway** — Deployment and hosting platform for the API
* **Neon** — Hosted PostgreSQL database


## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/runs` | Get all simulation runs |
| GET | `/runs/{run_id}` | Get a specific simulation run |
| POST | `/runs` | Create a new simulation run |
| PATCH | `/runs/{run_id}` | Update a specific simulation run |
| DELETE | `/runs/{run_id}` | Delete a specific simulation run |


## Running locally

After cloning the repository, create a .env file using .env.example as a template and add your local PostgreSQL connection details. Install dependencies with pip install -r requirements.txt, then start the API with uvicorn main:app --reload.


## Docker

Build and run the Docker container with docker build -t simulation-run-api . followed by docker run -p 8000:8000 simulation-run-api. The API will then be available at http://localhost:8000.


## Live Demo

The API is deployed on Railway and can be accessed at:
https://simulation-run-api-production.up.railway.app


## Testing

Automated tests can be run with pytest. The tests cover the API endpoints and database functionality.


## Notes and Limitations

This is a portfolio demonstration project and does not currently include authentication or authorisation. The Railway free service may also take a short time to respond after periods of inactivity.
