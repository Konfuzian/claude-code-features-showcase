# Frontend Tests

This directory contains tests for the static HTML frontend organized into three tiers.

## Test Tiers

### 1. Static HTML Tests (`test_html_pages.py`) - 51 tests
- **Purpose**: Validate HTML structure, content, and static elements
- **Dependencies**: pytest only (no browser)
- **Speed**: < 1 second
- **When**: Always run with `task test`

**Tests include:**
- HTML structure validation
- CDN inclusion (Tailwind, Datastar)
- Navigation links presence
- Content verification
- No inline scripts policy

**Run:**
```bash
task test  # Includes these tests
```

### 2. Sanity Tests (`test_sanity.py`) - 9 tests
- **Purpose**: Quick browser checks that pages load and basic features work
- **Dependencies**: Playwright + browser
- **Speed**: ~5-10 seconds
- **When**: Part of standard test suite

**Tests include:**
- Pages load without console errors
- Page titles are correct
- Navigation between pages works
- Counter buttons work
- Accordion toggles

**Run:**
```bash
# Local (requires browser deps)
task test:sanity

# Docker (no system deps needed)
task test:sanity:docker
```

### 3. End-to-End Tests (`test_e2e.py`) - 27 tests
- **Purpose**: Comprehensive browser testing of all interactive features
- **Dependencies**: Playwright + browser
- **Speed**: ~30-60 seconds
- **When**: Opt-in only (not part of default `task test`)

**Tests include:**
- All sanity checks plus:
- Detailed interactive element testing
- Form validation behavior
- Tab switching logic
- Keyboard accessibility
- Responsive design verification
- Cross-page navigation flows

**Run:**
```bash
# Local (requires browser deps)
task test:e2e

# Docker (no system deps needed)
task test:e2e:docker
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

**Static HTML tests**: 51 tests covering structure and content
**Sanity tests**: 9 tests covering basic browser functionality
**E2E tests**: 27 tests covering comprehensive interactive functionality

**Total**: 87 frontend tests
**Default suite**: 51 tests (static HTML only, no browser required)
