from faker import Faker
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from questdb.ingress import IngressError

from app.main import app
from app.db import quest

client = TestClient(app)
faker = Faker()

async def good_ingress_connection():
    mock = MagicMock()
    mock.row.return_value = None

    yield mock

def test_health_check_success():
    app.dependency_overrides[quest.ingress_connection] = good_ingress_connection

    response = client.get("/_health")
    assert response.status_code == 200
    assert response.text == "OK"

    app.dependency_overrides = {}

FAILURE = faker.word()

async def bad_ingress_connection():
    mock = MagicMock()
    mock.row.side_effect = IngressError(500, FAILURE)

    yield mock

def test_health_check_failure():
    app.dependency_overrides[quest.ingress_connection] = bad_ingress_connection

    response = client.get("/_health")
    assert response.status_code == 500
    assert response.text == FAILURE

    app.dependency_overrides = {}