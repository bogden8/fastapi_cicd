# FastAPI CI/CD Pipeline

A containerised FastAPI application with a fully automated CI/CD pipeline using GitHub Actions, Docker, and GitHub Container Registry. On every push to `main`, the pipeline runs tests, builds and pushes a Docker image to GHCR, then deploys it to a self-hosted homelab VM over Tailscale.

## Stack

- **FastAPI** — Python web framework serving the API
- **Docker** — containerises the application
- **GitHub Actions** — automates the CI/CD workflow
- **GitHub Container Registry (GHCR)** — stores and serves the Docker image
- **Tailscale** — provides secure private network access to the homelab VM for remote deployment
- **pytest + httpx** — automated tests run on every push

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Health check — returns status and version |
| `GET` | `/health` | Returns app status and uptime in seconds |
| `GET` | `/info` | Returns hostname, OS, and Python version of the running container |

## CI/CD Workflow

```
Push to main
    │
    ▼
GitHub Actions
    ├── Run pytest (test_main.py)
    ├── Build Docker image
    ├── Push image to ghcr.io/bogden8/fastapi_cicd
    └── SSH into homelab VM via Tailscale
            └── Pull latest image and restart container
```

## Project Structure

```
fastapi_cicd/
├── .github/
│   └── workflows/       # GitHub Actions CI/CD pipeline definition
├── main.py              # FastAPI application with /, /health, /info endpoints
├── test_main.py         # pytest tests for all three endpoints
├── Dockerfile           # python:3.12-slim image, runs uvicorn on port 8000
├── requirements.txt     # fastapi, uvicorn, pytest, httpx
└── .gitignore
```

## Running Locally

```bash
# Clone the repo
git clone https://github.com/bogden8/fastapi_cicd.git
cd fastapi_cicd

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload

# Run tests
pytest
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## Running with Docker

```bash
docker build -t fastapi_cicd .
docker run -p 8000:8000 fastapi_cicd
```

## Skills Demonstrated

- Building and containerising a Python REST API with FastAPI and Docker
- Writing automated tests with pytest and FastAPI's TestClient
- Designing a GitHub Actions CI/CD pipeline (test → build → push → deploy)
- Publishing Docker images to GitHub Container Registry
- Deploying to a self-hosted environment securely via Tailscale
