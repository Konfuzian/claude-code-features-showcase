#!/bin/bash
# Pre-commit hook example
# Runs before git commit to ensure code quality

echo "Running pre-commit checks..."

# Check for TODO/FIXME comments in staged files
if git diff --cached --name-only | xargs grep -l "TODO\|FIXME" > /dev/null 2>&1; then
    echo "Warning: Found TODO/FIXME comments in staged files"
    echo "Consider addressing them before committing"
fi

# Validate markdown files
if command -v markdownlint &> /dev/null; then
    echo "Checking markdown files..."
    git diff --cached --name-only --diff-filter=ACM | grep '\.md$' | xargs markdownlint
    if [ $? -ne 0 ]; then
        echo "Markdown validation failed. Please fix before committing."
        exit 1
    fi
fi

# Check for trailing whitespace
if git diff --cached --check; then
    echo "Found trailing whitespace. Please fix before committing."
    exit 1
fi

echo "Pre-commit checks passed!"
exit 0
