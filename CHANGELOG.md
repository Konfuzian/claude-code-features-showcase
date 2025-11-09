# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### 2025-11-09

#### Added
- Created CLAUDE.md with project context and development guidelines
- Created `.claude/` directory structure (commands, skills, hooks)
- Added example slash commands:
  - `analyze.md` - Code quality analysis
  - `docs.md` - Documentation generation
  - `test.md` - Test generation
  - `refactor.md` - Code refactoring
- Added example skills:
  - `code-reviewer.md` - Code review skill
  - `test-generator.md` - Test generation skill
  - `pdf-reader.md` - PDF text extraction skill
  - `xlsx-reader.md` - Excel/XLSX reading skill
- Added example hooks:
  - `pre-commit.sh` - Pre-commit validation (updated for markdown)
  - `README.md` - Hook documentation
- Created comprehensive documentation:
  - `docs/models.md` - Model selection guide
  - `docs/file-formats.md` - .md vs .yml guidance
  - `docs/workflows.md` - Common development patterns
  - `docs/context-management.md` - Token usage strategies
- Implemented PDF reader functionality:
  - Python project setup with uv package manager
  - `pyproject.toml` with dependencies (pypdf)
  - `src/pdf_reader/` module with text extraction
  - `tests/` with pytest and approval tests
  - Sample PDF fixture for testing
  - `.gitignore` for Python/testing artifacts
- Implemented XLSX reader functionality:
  - `src/xlsx_reader/` module with Excel data extraction
  - Support for multiple sheets with metadata
  - `tests/test_xlsx_reader.py` with 10 comprehensive tests
  - Sample Excel fixture with employee, project, and summary data
  - openpyxl dependency added
- Added Taskfile.yml with test automation:
  - `task test` - Run pytest suite
  - `task test:watch` - Watch mode with pytest-watcher
  - `task test:coverage` - Coverage reporting

#### Changed
- Restructured README.md with proper markdown hierarchy
- Added title and clearer section headings
- Improved formatting with bold emphasis for key terms
- Organized content into "Configuration & Structure" and "Features & Concepts" sections
- Enhanced readability with consistent formatting
