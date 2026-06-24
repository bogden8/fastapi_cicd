from fastapi.testclient import TestClient
from main import app

client= TestClient(app)

def test_root():
    response= client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    response=client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_info():
    response=client.get("/info")
    assert response.status_code == 200
    assert "hostname" in response.json()