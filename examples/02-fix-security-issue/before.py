# BEFORE: Insecure CORS Configuration
# File: apps/backend/src/backend/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Backend API",
        version="0.1.0",
        description="Example backend API application",
    )

    # ⚠️ CRITICAL SECURITY ISSUE
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows ANY website to access the API
        allow_credentials=True,  # Dangerous with allow_origins=["*"]
        allow_methods=["*"],  # Allows ALL HTTP methods
        allow_headers=["*"],  # Allows ALL headers
    )

    app.include_router(router)

    return app


app = create_app()
