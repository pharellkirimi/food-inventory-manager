import pytest
from app import app
from inventory import inventory


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_inventory_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_get_invalid_item(client):
    response = client.get("/inventory/999")

    assert response.status_code == 404


def test_patch_inventory_item(client):
    response = client.patch(
        "/inventory/1",
        json={
            "price": 99.99,
            "stock": 5
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["price"] == 99.99
    assert data["stock"] == 5


def test_delete_invalid_item(client):
    response = client.delete("/inventory/999")

    assert response.status_code == 404