"""Tests for app module."""

from frontend.app import create_app


def test_create_app():
    """Test that create_app returns a valid config."""
    app = create_app()

    assert app["name"] == "frontend"
    assert app["version"] == "0.1.0"
