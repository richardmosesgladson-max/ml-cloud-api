
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "ML Prediction API is running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post("/predict", json={"size": 12})

    assert response.status_code == 200
    assert response.json()["size"] == 12
    assert isinstance(response.json()["predicted_price_lakhs"], (int, float))


def test_invalid_size():
    response = client.post("/predict", json={"size": -5})
    assert response.status_code == 422
