from fastapi.testclient import TestClient
from app.main import app
from app.db_engine import init_db

client = TestClient(app)

def setup_module(module):
    init_db()

def test_create_notification():
    response = client.post("/notifications/", json={
        "title": "Test Notification",
        "message": "This is a test notification.",
        "recipient": "test@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Notification"
    assert data["message"] == "This is a test notification."
    assert data["recipient"] == "test@example.com"

def test_read_notification():
    response = client.post("/notifications/", json={
        "title": "Test Notification",
        "message": "This is a test notification.",
        "recipient": "test@example.com"
    })
    assert response.status_code == 200
    notification_id = response.json()["id"]

    response = client.get(f"/notifications/{notification_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == notification_id
    assert data["title"] == "Test Notification"
    assert data["message"] == "This is a test notification."
    assert data["recipient"] == "test@example.com"

def test_read_notifications():
    response = client.get("/notifications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
