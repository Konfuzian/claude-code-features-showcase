#!/bin/bash
# Automatic file formatting hook
# Runs after Edit or Write tool use

# Get the file path from environment variable set by Claude Code
FILE_PATH="${TOOL_USE_FILE_PATH}"

if [ -z "$FILE_PATH" ]; then
    exit 0
fi

# Only format if file exists
if [ ! -f "$FILE_PATH" ]; then
    exit 0
fi

# Get file extension
EXT="${FILE_PATH##*.}"

case "$EXT" in
    py)
        # Format Python files with ruff
        if command -v ruff &> /dev/null; then
            ruff format "$FILE_PATH" 2>/dev/null
            ruff check --fix "$FILE_PATH" 2>/dev/null
        fi
        ;;
    md)
        # Format markdown files with prettier
        if command -v prettier &> /dev/null; then
            prettier --write "$FILE_PATH" 2>/dev/null
        fi
        ;;
    json|yml|yaml)
        # Format JSON/YAML with prettier
        if command -v prettier &> /dev/null; then
            prettier --write "$FILE_PATH" 2>/dev/null
        fi
        ;;
esac

exit 0
