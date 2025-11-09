# Frontend Tests

This directory contains tests for the static HTML frontend.

## Test Types

### Static HTML Tests (`test_html_pages.py`)
- **Purpose**: Validate HTML structure, content, and static elements
- **Dependencies**: pytest only
- **Fast**: Runs in < 1 second
- **CI-friendly**: No browser required

**Tests include:**
- HTML structure validation
- CDN inclusion (Tailwind, Datastar)
- Navigation links presence
- Content verification
- No inline scripts policy

**Run:**
```bash
task test
# or
uv run pytest apps/frontend/tests/test_html_pages.py
```

### End-to-End Tests (`test_e2e.py`)
- **Purpose**: Test actual browser functionality and interactivity
- **Dependencies**: Playwright + system browser dependencies
- **Slower**: Runs in ~10-30 seconds
- **Requires**: Running web server at http://localhost:8080

**Tests include:**
- Interactive counter functionality
- Todo list add/remove operations
- Accordion toggle behavior
- Tab switching
- Form validation
- Navigation between pages
- Keyboard accessibility
- Responsive design

**Setup:**
```bash
# Install Playwright system dependencies (one-time)
uv run playwright install-deps

# Or manually install required libraries
sudo apt-get install libnspr4 libnss3 libasound2t64

# Start the web server
python3 -m http.server 8080 --directory apps/frontend
```

**Run:**
```bash
# Run all E2E tests (headless)
uv run pytest apps/frontend/tests/test_e2e.py

# Run with visible browser
uv run pytest apps/frontend/tests/test_e2e.py --headed

# Run specific test class
uv run pytest apps/frontend/tests/test_e2e.py::TestAboutPageE2E
```

## Test Organization

### TestIndexPageE2E
- Page loading
- Navigation links
- Interactive counter (+, -, Reset buttons)
- Feature cards visibility
- Responsive design

### TestDemoPageE2E
- Todo list functionality
- Contact form validation
- Tabbed content switching

### TestAboutPageE2E
- Accordion toggle behavior
- Exclusive opening (one section at a time)
- Architecture section visibility

### TestCrossBrowserNavigation
- Navigation between all pages
- Consistent footer across pages

### TestAccessibility
- Proper heading structure (h1 exists)
- Keyboard-accessible buttons

## Running Tests in CI

The E2E tests will automatically skip if browser dependencies are not available. Static HTML tests always run.

```yaml
# Example GitHub Actions
- name: Run tests
  run: |
    uv run playwright install-deps chromium || true
    task test
```

## Debugging E2E Tests

**View browser during test:**
```bash
uv run pytest apps/frontend/tests/test_e2e.py --headed --slowmo 1000
```

**Pause on failure:**
```bash
uv run pytest apps/frontend/tests/test_e2e.py --pdb
```

**Screenshot on failure:**
```bash
uv run pytest apps/frontend/tests/test_e2e.py --screenshot on
```

## Test Coverage

**Static HTML tests**: 76 tests covering structure and content
**E2E tests**: 27 tests covering interactive functionality

**Total**: 103 frontend tests
