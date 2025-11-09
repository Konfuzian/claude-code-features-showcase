# Packages

This directory contains shared libraries and tools that can be used by applications.

## Structure

Each package is a self-contained module with its own configuration and tests:

```
packages/
├── pdf-reader/           # PDF text extraction
│   ├── src/pdf_reader/
│   ├── tests/
│   └── pyproject.toml
└── xlsx-reader/          # Excel data extraction
    ├── src/xlsx_reader/
    ├── tests/
    └── pyproject.toml
```

## What Goes Here

**Shared libraries and tools:**
- File readers/writers (PDF, Excel, JSON, etc.)
- Data processors and transformers
- Utility libraries
- API clients
- Common functionality used across apps

## What Doesn't Go Here

**Applications** belong in `apps/`:
- Backend APIs
- Frontend web apps
- CLI tools that are deployed

## Adding a New Package

1. Create directory: `packages/my-package/`
2. Add configuration: `packages/my-package/pyproject.toml`
3. Create source: `packages/my-package/src/my_package/`
4. Add tests: `packages/my-package/tests/`
5. The workspace will auto-discover it

## Package Structure

```
packages/my-package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── module.py
├── tests/
│   ├── __init__.py
│   └── test_module.py
└── pyproject.toml
```

## Testing

Run tests for all packages:
```bash
task test
```

Run tests for specific package:
```bash
cd packages/my-package
uv run pytest -v
```

## Current Packages

### pdf-reader
Extract text from PDF files with support for multi-page documents.

**Usage:**
```python
from pdf_reader import read_pdf, extract_text_by_page

text = read_pdf("document.pdf")
pages = extract_text_by_page("document.pdf")
```

### xlsx-reader
Extract data from Excel workbooks with support for multiple sheets.

**Usage:**
```python
from xlsx_reader import read_xlsx, extract_sheets

data = read_xlsx("workbook.xlsx")
sheets = extract_sheets("workbook.xlsx")
```
