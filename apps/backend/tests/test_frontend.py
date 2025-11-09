"""Tests for HTML frontend integration."""

from fastapi.testclient import TestClient

from backend.app import create_app


def test_index_renders_html():
    """Test that index page returns HTML content."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert response.text.startswith("<!DOCTYPE html>")


def test_index_has_correct_title():
    """Test that index page has the correct title."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "<title>Hello World App</title>" in response.text
    assert "<h1" in response.text
    assert "Hello World App" in response.text


def test_index_includes_tailwind_cdn():
    """Test that Tailwind CSS is loaded via CDN."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "https://cdn.tailwindcss.com" in response.text
    assert 'script src="https://cdn.tailwindcss.com"' in response.text


def test_index_includes_datastar():
    """Test that Datastar library is loaded."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "datastar" in response.text.lower()
    assert "@sudodevnull/datastar" in response.text


def test_index_has_datastar_attributes():
    """Test that page has Datastar reactive attributes."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    # Check for Datastar data attributes
    assert "data-on-load" in response.text
    assert "data-store" in response.text
    assert "data-show" in response.text
    assert "data-text" in response.text
    assert "data-on-click" in response.text


def test_index_references_api_endpoints():
    """Test that page references the correct API endpoints."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "/api/hello" in response.text
    assert "/api/health" in response.text


def test_index_has_loading_state():
    """Test that page includes loading state UI."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "Loading..." in response.text
    assert "animate-spin" in response.text


def test_index_has_error_handling():
    """Test that page includes error handling UI."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "$error" in response.text
    assert "Error:" in response.text


def test_index_has_refresh_button():
    """Test that page includes refresh button."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "Refresh Message" in response.text
    assert "<button" in response.text


def test_index_has_health_status():
    """Test that page includes health status indicator."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "Status:" in response.text
    assert "healthStatus" in response.text


def test_index_has_responsive_classes():
    """Test that page uses Tailwind responsive classes."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    # Check for common Tailwind utility classes
    assert "container" in response.text
    assert "mx-auto" in response.text
    assert "bg-" in response.text
    assert "text-" in response.text


def test_index_has_footer():
    """Test that page includes footer with tech stack info."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "<footer" in response.text
    assert "FastAPI" in response.text
    assert "Jinja2" in response.text
    assert "Tailwind CSS" in response.text
    assert "Datastar" in response.text


def test_index_template_context():
    """Test that template receives correct context variables."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    # The title variable should be rendered in the template
    assert "Hello World App" in response.text


def test_index_has_meta_tags():
    """Test that page has proper meta tags."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert '<meta charset="UTF-8">' in response.text
    assert 'name="viewport"' in response.text


def test_api_integration():
    """Test that API endpoints work with frontend integration."""
    client = TestClient(create_app())

    # Test that all endpoints are accessible
    index_response = client.get("/")
    hello_response = client.get("/api/hello")
    health_response = client.get("/api/health")

    assert index_response.status_code == 200
    assert hello_response.status_code == 200
    assert health_response.status_code == 200

    # Verify API responses have expected data
    hello_data = hello_response.json()
    assert "message" in hello_data
    assert "timestamp" in hello_data

    health_data = health_response.json()
    assert "status" in health_data
    assert "timestamp" in health_data
