from recommendations_api.main import app
import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    return TestClient(app)
