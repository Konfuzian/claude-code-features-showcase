# FastAPI Backend Specification

**Status**: 📝 Planned
**Version**: 1.0
**Last Updated**: 2025-11-09

## Overview

Convert the backend application to a FastAPI REST API server with a hello world endpoint.

## Purpose

Provide a working example of a Python backend API application that:
- Demonstrates FastAPI framework usage
- Shows how to structure an API in the monorepo
- Can be extended to use packages from `packages/` (pdf-reader, xlsx-reader)
- Serves as a template for building backend services

## Features

### Core Functionality
- FastAPI application setup
- Hello world GET endpoint at `/`
- Health check endpoint at `/health`
- Proper application factory pattern
- CORS middleware configuration
- Request/response logging

### API Endpoints

#### `GET /`
Returns a welcome message.

**Response:**
```json
{
  "message": "Hello World",
  "app": "backend",
  "version": "0.1.0"
}
```

#### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-09T10:00:00Z"
}
```

### Error Handling
- Custom exception handlers
- Proper HTTP status codes
- Consistent error response format

## API

### Application Structure

```python
# src/backend/main.py
from fastapi import FastAPI
from backend.app import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# src/backend/app.py
def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Backend API",
        version="0.1.0",
        description="Example backend API application"
    )

    # Add middleware
    # Add routes
    # Add exception handlers

    return app
```

### Routes Module

```python
# src/backend/routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def hello_world():
    return {
        "message": "Hello World",
        "app": "backend",
        "version": "0.1.0"
    }

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
```

## Implementation Details

### Dependencies

**Add to `apps/backend/pyproject.toml`:**
```toml
[project]
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "pydantic>=2.5.0",
    "pydantic-settings>=2.1.0",
]
```

**Dev dependencies:**
```toml
[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "httpx>=0.26.0",  # For testing FastAPI
    "pytest-asyncio>=0.23.0",
]
```

### Module Structure

```
apps/backend/
├── src/backend/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── app.py           # Application factory
│   ├── routes.py        # Route definitions
│   ├── config.py        # Configuration
│   └── middleware.py    # Custom middleware
├── tests/
│   ├── __init__.py
│   ├── test_main.py     # Main app tests
│   ├── test_routes.py   # Route tests
│   └── conftest.py      # Test fixtures
└── pyproject.toml
```

### Design Decisions

**Why FastAPI?**
- Modern, fast (high-performance)
- Automatic API documentation (Swagger/OpenAPI)
- Built-in data validation with Pydantic
- Async support
- Type hints throughout

**Why Application Factory Pattern?**
- Easier testing (can create app instances)
- Configuration flexibility
- Better organization

**Why Separate Routes Module?**
- Keeps main.py clean
- Easier to organize multiple routers
- Better separation of concerns

## Testing

### Test Coverage
- Hello world endpoint returns correct response
- Health check endpoint returns correct format
- Response status codes are correct
- Application can start and stop cleanly
- CORS headers are set correctly
- Invalid routes return 404

### Test Example

```python
# tests/test_routes.py
from fastapi.testclient import TestClient
from backend.app import create_app

def test_hello_world():
    """Test hello world endpoint."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World",
        "app": "backend",
        "version": "0.1.0"
    }

def test_health_check():
    """Test health check endpoint."""
    client = TestClient(create_app())
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
```

### Running Tests
```bash
cd apps/backend
uv run pytest -v
```

## Usage Examples

### Running the Server

**Development:**
```bash
cd apps/backend
uv run uvicorn backend.main:app --reload
# or
uv run python -m backend.main
```

**With Task:**
```bash
task backend:dev
```

**Production:**
```bash
uv run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing Endpoints

**cURL:**
```bash
# Hello world
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health
```

**Browser:**
- API: http://localhost:8000/
- Swagger docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Integration with Packages

Future endpoints can use packages:

```python
from pdf_reader import read_pdf
from xlsx_reader import read_xlsx

@router.post("/api/extract/pdf")
async def extract_pdf(file: UploadFile):
    """Extract text from uploaded PDF."""
    content = await file.read()
    # Save to temp file, extract, return
    return {"text": extracted_text}
```

## Configuration

### Environment Variables

```python
# src/backend/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Backend API"
    debug: bool = False
    port: int = 8000
    host: str = "0.0.0.0"

    class Config:
        env_file = ".env"
```

## Task Commands

Add to root `Taskfile.yml`:

```yaml
backend:dev:
  desc: Run backend dev server
  dir: apps/backend
  cmds:
    - uv run uvicorn backend.main:app --reload

backend:test:
  desc: Run backend tests
  dir: apps/backend
  cmds:
    - uv run pytest -v
```

## Future Enhancements

Potential improvements (not part of initial implementation):

- **Database**: Add SQLAlchemy + Alembic for database
- **Authentication**: JWT-based auth
- **File Upload**: Endpoints for PDF/XLSX processing
- **WebSocket**: Real-time features
- **Background Tasks**: Celery for async processing
- **Caching**: Redis integration
- **Rate Limiting**: Protect endpoints
- **Logging**: Structured logging with loguru
- **Monitoring**: Prometheus metrics
- **Docker**: Containerization

## Success Criteria

Implementation is complete when:
- ✅ FastAPI application starts without errors
- ✅ GET / returns hello world response
- ✅ GET /health returns health status
- ✅ All tests pass (minimum 4 tests)
- ✅ API documentation accessible at /docs
- ✅ Can run with `task backend:dev`
- ✅ Code follows project conventions
- ✅ Spec moved to specs/implemented/
