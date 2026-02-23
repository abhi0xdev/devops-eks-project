import pytest
from app.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health(client):
    response = client.get("/health")
    assert response.json["status"] == "ok"

def test_config(client):
    response = client.get("/config")
    assert "env" in response.json