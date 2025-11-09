# Applications

This directory contains full application projects that can be deployed.

## Structure

Each app has its own directory with complete source code, tests, and configuration:

```
apps/
├── backend/              # API server application
│   ├── src/
│   ├── tests/
│   └── pyproject.toml
└── frontend/             # Web UI application
    ├── src/
    ├── tests/
    └── package.json
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

## Dependencies

Apps can depend on packages from `packages/`:
```toml
# apps/api/pyproject.toml
[project]
dependencies = [
    "pdf-reader",
    "xlsx-reader",
]
```
