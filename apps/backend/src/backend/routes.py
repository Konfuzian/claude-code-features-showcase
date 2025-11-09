"""API routes for the backend application."""

from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Setup templates
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Serve the HTML frontend.

    Args:
        request: FastAPI request object

    Returns:
        HTMLResponse: Rendered HTML template
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Hello World App"}
    )


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
