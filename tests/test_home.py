from fastapi.testclient import TestClient


def test_home_returns_200(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_hello_world(client: TestClient):
    response = client.get("/")
    assert response.text == '"Hello world!"'
