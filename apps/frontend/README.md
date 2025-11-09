# Static HTML Frontend

A zero-build frontend using static HTML, Tailwind CSS, and Datastar for interactivity.

## Features

- **No Build Step**: Just serve the files and go
- **Tailwind CSS**: Utility-first styling via CDN
- **Datastar**: Reactive state management via CDN
- **Zero Configuration**: No package.json, no bundler, no complexity

## Pages

- `index.html` - Home page with feature showcase and interactive counter
- `demo.html` - Interactive demos (todo list, contact form, tabs)
- `about.html` - Project information with accordion

## Development

Serve the static files with Python's built-in HTTP server:

```bash
task frontend:dev
# Or manually:
python3 -m http.server 8080
```

Then open http://localhost:8080 in your browser.

## Why This Approach?

1. **Simplicity**: No build tools, no configuration files
2. **Fast**: Instant page loads, no bundle size
3. **Maintainable**: Plain HTML, easy to understand
4. **Modern**: Reactive UI with Datastar, beautiful styling with Tailwind

## Technology

- **HTML5**: Semantic markup
- **Tailwind CSS v3**: https://cdn.tailwindcss.com
- **Datastar**: https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.11

## Testing

The frontend has comprehensive test coverage (103 tests):

```bash
task test              # Run all tests (including frontend)
```

### Static HTML Tests (76 tests)
Fast tests that validate structure and content:
- HTML structure and syntax
- Required meta tags and CDN includes
- Navigation consistency across pages
- Interactive Datastar components
- Tailwind CSS classes
- No inline scripts (security)

### End-to-End Tests (27 tests)
Browser-based tests using Playwright:
- Interactive counter functionality
- Todo list operations
- Accordion toggle behavior
- Form validation
- Navigation between pages
- Keyboard accessibility
- Responsive design

**E2E Setup:**
```bash
# Install browser dependencies (one-time)
uv run playwright install-deps

# Start dev server
python3 -m http.server 8080

# Run E2E tests
uv run pytest apps/frontend/tests/test_e2e.py
```

See [tests/README.md](tests/README.md) for detailed testing documentation.

## Deployment

Simply copy the HTML files to any static hosting:
- GitHub Pages
- Netlify
- Vercel
- Any CDN or web server

No build step required!
