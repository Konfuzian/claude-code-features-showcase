"""Tests for API routes."""

from fastapi.testclient import TestClient

from backend.app import create_app


def test_index_page():
    """Test that index page renders HTML."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Hello World App" in response.text
    assert "Tailwind" in response.text
    assert "Datastar" in response.text


def test_api_hello():
    """Test API hello endpoint returns correct response."""
    client = TestClient(create_app())
    response = client.get("/api/hello")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello World"
    assert data["app"] == "backend"
    assert data["version"] == "0.1.0"
    assert "timestamp" in data
    assert data["timestamp"].endswith("Z")


def test_api_health():
    """Test API health check endpoint returns correct format."""
    client = TestClient(create_app())
    response = client.get("/api/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["timestamp"].endswith("Z")


def test_not_found():
    """Test that invalid routes return 404."""
    client = TestClient(create_app())
    response = client.get("/invalid")

    assert response.status_code == 404


def test_api_docs_available():
    """Test that API documentation is accessible."""
    client = TestClient(create_app())

    # Test OpenAPI JSON
    response = client.get("/openapi.json")
    assert response.status_code == 200

    # Test Swagger UI
    response = client.get("/docs")
    assert response.status_code == 200

    # Test ReDoc
    response = client.get("/redoc")
    assert response.status_code == 200
