"""API routes for the backend application."""

from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello_world():
    """
    Hello world endpoint.

    Returns:
        dict: Welcome message with app metadata
    """
    return {
        "message": "Hello World",
        "app": "backend",
        "version": "0.1.0",
    }


@router.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.

    Returns:
        dict: Health status with timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
