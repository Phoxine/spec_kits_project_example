from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_read_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Note: Other tests require auth, but for POC, skip or mock