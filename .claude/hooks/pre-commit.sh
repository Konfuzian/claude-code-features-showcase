#!/bin/bash
# Pre-commit hook example
# Runs before git commit to ensure code quality

echo "Running pre-commit checks..."

# Check for TODO/FIXME comments in staged files
if git diff --cached --name-only | xargs grep -l "TODO\|FIXME" > /dev/null 2>&1; then
    echo "Warning: Found TODO/FIXME comments in staged files"
    echo "Consider addressing them before committing"
fi

# Run linter if available
if command -v eslint &> /dev/null; then
    echo "Running ESLint..."
    git diff --cached --name-only --diff-filter=ACM | grep '\.js$\|\.ts$' | xargs eslint
    if [ $? -ne 0 ]; then
        echo "ESLint found issues. Please fix before committing."
        exit 1
    fi
fi

# Run tests if available
if [ -f "package.json" ] && grep -q "\"test\"" package.json; then
    echo "Running tests..."
    npm test
    if [ $? -ne 0 ]; then
        echo "Tests failed. Please fix before committing."
        exit 1
    fi
fi

echo "Pre-commit checks passed!"
exit 0
