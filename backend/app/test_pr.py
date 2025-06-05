from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_fetch_pr():
    # Using a real public PR for testing
    response = client.get(
        "/fetch-pr?owner=facebook&repo=react&pr_number=1"
    )
    assert response.status_code == 200
    data = response.json()
    # Check for some expected PR fields
    assert "title" in data
    assert "user" in data
    assert "body" in data
