from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_text():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "hello world"
