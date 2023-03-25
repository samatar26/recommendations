from recommendations_api.main import app
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from recommendations_api.env import DATABASE_URL
from recommendations_api.dependencies import get_session

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False)


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture()
def session(connection) -> Session:
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()


@pytest.fixture()
def client(session) -> TestClient:
    def _get_session_override():
        yield session

    app.dependency_overrides[get_session] = _get_session_override
    return TestClient(app)
