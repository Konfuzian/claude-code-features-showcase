# HTML Frontend Integration Specification

**Status**: 📝 Planned
**Version**: 1.0
**Last Updated**: 2025-11-09

## Overview

Create an HTML page that fetches and displays the "Hello World" message from the backend API using Jinja2 templates, Tailwind CSS for styling, and Datastar for reactive data binding.

## Purpose

Demonstrate a modern HTML-first frontend approach that:
- Integrates with the FastAPI backend
- Uses server-side templating (Jinja2)
- Provides reactive UI with Datastar (HTMX successor)
- Styles with Tailwind CSS
- Requires no build step (simple, fast development)

## Features

### Core Functionality
- Render HTML template with Jinja2
- Fetch data from backend API using Datastar
- Display hello world message reactively
- Show loading states
- Handle errors gracefully
- Auto-refresh capability

### UI Components
- Header with app title
- Message display card
- Refresh button
- Health status indicator
- Styled with Tailwind CSS

### Reactive Features (Datastar)
- Load message on page load
- Refresh message on button click
- Show loading spinner during fetch
- Display fetch timestamp
- Error handling with user feedback

## Implementation Details

### Backend Changes

Add template rendering to FastAPI backend:

**Update `apps/backend/pyproject.toml`:**
```toml
[project]
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "jinja2>=3.1.3",  # Add for templates
]
```

**Create templates directory:**
```
apps/backend/
├── src/backend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── (optional static files)
```

**Update `src/backend/app.py`:**
```python
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

def create_app() -> FastAPI:
    app = FastAPI(title="Backend API", version="0.1.0")

    # Setup templates
    templates_dir = Path(__file__).parent / "templates"
    templates = Jinja2Templates(directory=str(templates_dir))

    # Mount static files (if needed)
    # app.mount("/static", StaticFiles(directory="static"), name="static")

    return app
```

**Add route to serve HTML (`src/backend/routes.py`):**
```python
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the HTML frontend."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Hello World App"}
    )

@router.get("/api/hello")
async def api_hello():
    """API endpoint for hello world message."""
    return {
        "message": "Hello World",
        "app": "backend",
        "version": "0.1.0",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@router.get("/api/health")
async def api_health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
```

### Frontend Template

**`src/backend/templates/index.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>

    <!-- Tailwind CSS via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Datastar library -->
    <script type="module" src="https://cdn.jsdelivr.net/npm/@sudodevnull/datastar"></script>
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <!-- Header -->
        <header class="mb-8">
            <h1 class="text-4xl font-bold text-gray-800">{{ title }}</h1>
            <p class="text-gray-600 mt-2">FastAPI + Jinja2 + Tailwind + Datastar</p>
        </header>

        <!-- Main Content -->
        <main
            data-on-load="$$get('/api/hello')"
            data-store="{message: '', loading: true, error: null, timestamp: ''}"
        >
            <!-- Loading State -->
            <div data-show="$loading" class="text-center py-12">
                <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
                <p class="mt-4 text-gray-600">Loading...</p>
            </div>

            <!-- Error State -->
            <div data-show="$error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                <strong>Error:</strong> <span data-text="$error"></span>
            </div>

            <!-- Success State -->
            <div data-show="!$loading && !$error" class="bg-white rounded-lg shadow-lg p-8">
                <!-- Message Card -->
                <div class="text-center mb-6">
                    <div class="text-6xl mb-4">👋</div>
                    <h2 class="text-3xl font-bold text-gray-800 mb-2" data-text="$message"></h2>
                    <p class="text-gray-600">
                        App: <span class="font-semibold" data-text="$app"></span>
                    </p>
                    <p class="text-gray-600">
                        Version: <span class="font-semibold" data-text="$version"></span>
                    </p>
                </div>

                <!-- Timestamp -->
                <div class="text-center text-sm text-gray-500 mb-6">
                    Last updated: <span data-text="$timestamp"></span>
                </div>

                <!-- Refresh Button -->
                <div class="text-center">
                    <button
                        data-on-click="$$get('/api/hello')"
                        class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-6 rounded-lg transition duration-200 ease-in-out transform hover:scale-105"
                    >
                        🔄 Refresh Message
                    </button>
                </div>
            </div>

            <!-- Health Status -->
            <div class="mt-8 bg-white rounded-lg shadow p-4">
                <div
                    data-on-load="$$get('/api/health')"
                    data-store="{healthStatus: 'checking...', healthTime: ''}"
                    class="flex items-center justify-between"
                >
                    <div class="flex items-center">
                        <div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
                        <span class="text-gray-700">Status: </span>
                        <span class="font-semibold ml-1" data-text="$healthStatus"></span>
                    </div>
                    <span class="text-sm text-gray-500" data-text="$healthTime"></span>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="mt-12 text-center text-gray-600 text-sm">
            <p>Built with FastAPI, Jinja2, Tailwind CSS, and Datastar</p>
        </footer>
    </div>
</body>
</html>
```

## Design Decisions

### Why Jinja2?
- Built-in FastAPI support
- Server-side rendering (SSR)
- Template inheritance and components
- Python-native templating

### Why Datastar?
- Modern HTMX successor
- Reactive data binding
- Small footprint (~10KB)
- No build step required
- Simple declarative syntax
- Native fetch API usage

### Why Tailwind CSS via CDN?
- No build step needed
- Rapid prototyping
- Utility-first approach
- Responsive by default
- Small production size with JIT

### Why This Stack?
- **Zero build step**: Instant development
- **SEO-friendly**: Server-side rendering
- **Progressive enhancement**: Works without JS
- **Simple deployment**: Single FastAPI app
- **Fast development**: Hot reload with uvicorn

## API Endpoints

### `GET /`
Serves the HTML page.

**Response**: HTML document

### `GET /api/hello`
Returns hello world message.

**Response:**
```json
{
  "message": "Hello World",
  "app": "backend",
  "version": "0.1.0",
  "timestamp": "2025-11-09T10:00:00Z"
}
```

### `GET /api/health`
Returns health status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-09T10:00:00Z"
}
```

## Testing

### Manual Testing
1. Start backend: `task backend:dev`
2. Open browser: http://localhost:8000
3. Verify message displays
4. Click refresh button
5. Verify health status shows "healthy"

### Automated Testing

**Test template rendering:**
```python
# tests/test_routes.py
def test_index_page():
    """Test that index page renders."""
    client = TestClient(create_app())
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Hello World App" in response.text
    assert "Tailwind" in response.text

def test_api_hello():
    """Test API endpoint."""
    client = TestClient(create_app())
    response = client.get("/api/hello")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello World"
    assert "timestamp" in data
```

## Usage Examples

### Development
```bash
# Start backend with templates
task backend:dev

# Open browser
open http://localhost:8000
```

### Features to Test
- ✅ Page loads and displays message
- ✅ Refresh button updates timestamp
- ✅ Health status shows green indicator
- ✅ Responsive design works on mobile
- ✅ Loading spinner shows during fetch
- ✅ Error handling if backend is down

## File Structure

```
apps/backend/
├── src/backend/
│   ├── templates/
│   │   ├── index.html       # Main template
│   │   ├── base.html        # (Optional) Base layout
│   │   └── components/      # (Optional) Reusable components
│   ├── static/              # (Optional) Static assets
│   │   └── css/
│   ├── app.py
│   ├── routes.py
│   └── main.py
└── tests/
    ├── test_routes.py
    └── test_templates.py
```

## Future Enhancements

### Templates
- Template inheritance with `base.html`
- Reusable components (header, footer, card)
- Multiple pages (about, contact, etc.)

### Functionality
- Form submissions with Datastar
- WebSocket support for real-time updates
- Dark mode toggle
- User authentication pages

### Datastar Features
- Form validation
- Optimistic UI updates
- Debounced inputs
- Infinite scroll
- Modal dialogs

### Styling
- Custom Tailwind configuration
- CSS file for custom styles
- Animation library integration
- Icon library (Heroicons, Font Awesome)

## Success Criteria

Implementation is complete when:
- ✅ HTML page loads at /
- ✅ Message fetched from /api/hello displays correctly
- ✅ Refresh button updates message with new timestamp
- ✅ Health indicator shows status from /api/health
- ✅ Loading states work correctly
- ✅ Page is responsive (mobile, tablet, desktop)
- ✅ No build step required
- ✅ All tests pass
- ✅ Datastar reactive features working
- ✅ Spec moved to specs/implemented/

## Dependencies

**Backend (apps/backend/pyproject.toml):**
```toml
[project]
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "jinja2>=3.1.3",
]
```

**Frontend (CDN - no package manager needed):**
- Tailwind CSS: https://cdn.tailwindcss.com
- Datastar: https://cdn.jsdelivr.net/npm/@sudodevnull/datastar

## Notes

- This approach uses CDN links for development simplicity
- For production, consider using Tailwind CLI or PostCSS
- Datastar is actively developed and well-documented
- Templates can be extended to full-featured web app
- Can coexist with React frontend (different routes)
