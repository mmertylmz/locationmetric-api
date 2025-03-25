import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # Adjust based on your actual response

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "price": 10.0})
    assert response.status_code == 201
    assert response.json() == {"name": "Test Item", "price": 10.0}  # Adjust based on your actual response

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "price": 10.0}  # Adjust based on your actual response

def test_update_item():
    response = client.put("/items/1", json={"name": "Updated Item", "price": 15.0})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Item", "price": 15.0}  # Adjust based on your actual response

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 204
    assert response.content == b""  # Adjust based on your actual response