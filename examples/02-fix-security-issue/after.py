# AFTER: Secure CORS Configuration
# File: apps/backend/src/backend/app.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router


# Get allowed origins from environment variable
# In production, set ALLOWED_ORIGINS="https://yourdomain.com,https://www.yourdomain.com"
# In development, defaults to localhost
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:8080"
).split(",")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Backend API",
        version="0.1.0",
        description="Example backend API application",
    )

    # ✅ SECURE CORS CONFIGURATION
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,  # Specific origins only
        allow_credentials=True,  # Safe with specific origins
        allow_methods=["GET", "POST", "PUT", "DELETE"],  # Explicit methods
        allow_headers=["Content-Type", "Authorization"],  # Explicit headers
        max_age=600,  # Cache preflight requests for 10 minutes
    )

    app.include_router(router)

    return app


app = create_app()
