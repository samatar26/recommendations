from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from models.account import Account


def test_get_home_returns_200(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200


def test_get_home_returns_hello_world(client: TestClient):
    response = client.get("/")
    assert response.text == '"Hello world!"'


def test_post_home_inserts_account_payload_into_database(client, session: Session):
    all_users = session.query(Account).all()
    assert len(all_users) == 0

    response = client.post("/", json={"id": 1})
    assert response.status_code == 200

    all_users = session.query(Account).all()
    assert len(all_users) == 1
    assert all_users[0].id == 1
