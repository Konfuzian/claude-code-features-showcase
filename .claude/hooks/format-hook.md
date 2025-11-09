# Automatic Formatting Hooks Guide

This project uses Claude Code's PostToolUse hooks to automatically format files after editing.

## How It Works

When you edit or write a file using Claude Code, the formatting hook automatically runs to ensure consistent code style.

## Configuration

See [.claude/hooks.json](hooks.json) for the hook configuration.

The hook triggers on `Edit` or `Write` tool use and runs [format-file.sh](format-file.sh).

## Supported File Types

### Python (`.py`)
- **Formatter**: [ruff](https://docs.astral.sh/ruff/)
- **Actions**:
  - Auto-formats code (`ruff format`)
  - Auto-fixes linting issues (`ruff check --fix`)

### Markdown (`.md`)
- **Formatter**: prettier (if installed)
- **Actions**: Auto-formats markdown structure

### JSON/YAML (`.json`, `.yml`, `.yaml`)
- **Formatter**: prettier (if installed)
- **Actions**: Auto-formats structure and indentation

## Installation

### Python Formatter (ruff)
Already installed via uv:
```bash
uv add --dev ruff
```

### Prettier (optional)
For markdown/JSON/YAML formatting:
```bash
npm install -g prettier
```

## Manual Formatting

You can also format files manually:

```bash
# Format Python files
uv run ruff format .
uv run ruff check --fix .

# Format markdown/JSON (if prettier installed)
prettier --write "**/*.md"
prettier --write "**/*.{json,yml,yaml}"
```

## Benefits

- **Consistency**: Automatic formatting ensures all code follows project standards
- **No Manual Work**: Formatting happens automatically after edits
- **Deterministic**: Same formatting rules apply every time
- **Fast**: Formatters run in milliseconds

## Hook Script

The [format-file.sh](format-file.sh) script:
1. Receives the edited file path from Claude Code
2. Determines file type by extension
3. Runs appropriate formatter
4. Exits silently if no formatter available
