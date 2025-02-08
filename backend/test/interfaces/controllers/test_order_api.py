from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)

def test_order_status_endpoint():
    response = client.get("/order/status")
    assert response.status_code == 200
    data = response.json()
    assert "order" in data
    assert data["order"]["subtotal"] > 0
    assert data["order"]["taxes"] > 0