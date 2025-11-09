"""Main frontend application."""


def create_app():
    """Create and configure the frontend application."""
    return {"name": "frontend", "version": "0.1.0"}


if __name__ == "__main__":
    app = create_app()
    print(f"Frontend application: {app['name']} v{app['version']}")
