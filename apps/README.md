# Applications

This directory contains full application projects that can be deployed.

## Structure

This directory contains both Python and JavaScript/TypeScript applications:

```
apps/
├── backend/              # Python API server (uv)
│   ├── src/backend/
│   ├── tests/
│   └── pyproject.toml
└── frontend/             # React web app (npm/vite)
    ├── src/
    ├── public/
    ├── index.html
    ├── package.json
    └── vite.config.ts
```

## What Goes Here

**Applications** are deployable projects:
- Backend APIs
- Frontend web apps
- CLI tools
- Desktop applications
- Mobile apps
- Worker services

## What Doesn't Go Here

**Shared libraries and tools** belong in `packages/`:
- Reusable code modules
- Utility libraries
- Data processors
- File readers/writers

## Adding a New App

1. Create directory: `apps/my-app/`
2. Add configuration: `apps/my-app/pyproject.toml` or `package.json`
3. Create source: `apps/my-app/src/`
4. Add tests: `apps/my-app/tests/`
5. Update root workspace if needed

## Examples

**Backend App:**
```
apps/api/
├── src/
│   ├── main.py
│   ├── routes/
│   └── models/
├── tests/
└── pyproject.toml
```

**Frontend App:**
```
apps/web/
├── src/
│   ├── components/
│   ├── pages/
│   └── App.tsx
├── tests/
└── package.json
```

## Current Apps

### Backend (Python/uv)
Python API server application.

**Run tests:**
```bash
cd apps/backend
uv run pytest -v
```

**Run application:**
```bash
cd apps/backend
uv run python -m backend.main
```

### Frontend (React/Vite)
React web application with TypeScript and Vite.

**Install dependencies:**
```bash
task frontend:install
# or: cd apps/frontend && npm install
```

**Run dev server:**
```bash
task frontend:dev
# or: cd apps/frontend && npm run dev
```

**Build for production:**
```bash
task frontend:build
# or: cd apps/frontend && npm run build
```

## Dependencies

Python apps can depend on packages from `packages/`:
```toml
# apps/backend/pyproject.toml
[project]
dependencies = [
    "pdf-reader",
    "xlsx-reader",
]
```
