"""Tests for main module."""

from backend.main import app


def test_app_exists():
    """Test that app instance is created."""
    assert app is not None
    assert app.title == "Backend API"
    assert app.version == "0.1.0"
