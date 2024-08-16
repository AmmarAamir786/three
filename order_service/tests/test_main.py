from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={"item_name": "Test Item", "quantity": 1, "price": 9.99})
    assert response.status_code == 200
    data = response.json()
    assert data["item_name"] == "Test Item"
    assert data["quantity"] == 1
    assert data["price"] == 9.99

def test_get_order():
    response = client.post("/orders/", json={"item_name": "Test Item", "quantity": 1, "price": 9.99})
    order_id = response.json()["id"]
    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["item_name"] == "Test Item"
    assert data["quantity"] == 1
    assert data["price"] == 9.99

def test_get_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
