"""Main application entry point."""

from backend.app import create_app

app = create_app()


def main():
    """Run the backend application with uvicorn."""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
