"""API routes for the backend application."""

from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """
    Root endpoint - API information.

    Returns:
        dict: API metadata and available endpoints
    """
    return {
        "name": "Backend API",
        "version": "0.1.0",
        "endpoints": {
            "health": "/api/health",
            "hello": "/api/hello",
        },
    }


@router.get("/api/hello")
async def api_hello():
    """
    API endpoint for hello world message.

    Returns:
        dict: Welcome message with app metadata and timestamp
    """
    return {
        "message": "Hello World",
        "app": "backend",
        "version": "0.1.0",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


@router.get("/api/health")
async def api_health():
    """
    Health check endpoint for monitoring.

    Returns:
        dict: Health status with timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
