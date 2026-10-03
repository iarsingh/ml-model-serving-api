from fastapi.testclient import TestClient
from serving.main import app

def test_versioned_prediction():
    client = TestClient(app)
    payload = client.post("/predict", json={"sqft": 1200, "bedrooms": 2}).json()
    assert payload["price"] == 236000
    assert payload["version"] == "1.0.0"
    assert client.post("/predict", json={"sqft": 1200}).status_code == 422
