# Using Format Hook

## What It Does

The format hook automatically formats code when you edit or write files using Claude Code's Edit or Write tools. It formats:
- **Python**: Using `ruff` formatter
- **Markdown**: Using `prettier`
- **JSON**: Using `prettier`
- **YAML**: Using `prettier`

Hook files:
- Configuration: [.claude/hooks.json](../../../.claude/hooks.json)
- Script: [.claude/hooks/format-file.sh](../../../.claude/hooks/format-file.sh)
- Prompt: [.claude/hooks/format-hook.md](../../../.claude/hooks/format-hook.md)

## When It Runs

Automatically triggered after:
- Using the Edit tool to modify a file
- Using the Write tool to create/overwrite a file

Event type: `PostToolUse` (after Edit or Write completes)

## Example 1: Python Formatting

### Before Formatting (Messy Code)

```python
# utils.py
def calculate_total(items):
    total=0
    for item in items:
        if item[ 'price' ]>0:
            total+=item['price']*item.get('quantity',1)
    return total

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
```

### Claude Edits the File

```
User: "Add a discount parameter to calculate_total"
Claude: [Uses Edit tool to modify function]
```

### Hook Runs Automatically

```
🔄 Formatting Python file: utils.py
✓ Formatted with ruff
```

### After Formatting (Clean Code)

```python
# utils.py
def calculate_total(items, discount=0):
    total = 0
    for item in items:
        if item["price"] > 0:
            subtotal = item["price"] * item.get("quantity", 1)
            total += subtotal

    if discount > 0:
        total = total * (1 - discount / 100)

    return total


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

Changes applied:
- ✅ Proper spacing around operators
- ✅ Consistent quote style (double quotes)
- ✅ Two blank lines between top-level definitions
- ✅ Proper indentation

## Example 2: Markdown Formatting

### Before Formatting

```markdown
# API  Documentation

## Endpoints

-   GET /users - Get all users
- POST /users -Create user
*   DELETE /users/:id  -  Delete user

### Example
```json
{"name":"John","email":"john@example.com"}
```

**Note:**  All endpoints require   authentication.
```

### Claude Writes the File

```
User: "Create a markdown file with the API docs"
Claude: [Uses Write tool to create file]
```

### Hook Runs

```
🔄 Formatting Markdown file: API.md
✓ Formatted with prettier
```

### After Formatting

```markdown
# API Documentation

## Endpoints

- GET /users - Get all users
- POST /users -Create user
- DELETE /users/:id - Delete user

### Example

```json
{
  "name": "John",
  "email": "john@example.com"
}
```

**Note:** All endpoints require authentication.
```

Changes applied:
- ✅ Consistent list formatting
- ✅ Proper spacing around headings
- ✅ Formatted JSON code blocks
- ✅ Normalized whitespace

## Example 3: JSON Formatting

### Before Formatting

```json
{"users":[{"id":1,"name":"Alice","roles":["admin","user"]},{"id":2,"name":"Bob","roles":["user"]}],"total":2}
```

### Hook Runs

```
🔄 Formatting JSON file: users.json
✓ Formatted with prettier
```

### After Formatting

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "roles": ["admin", "user"]
    },
    {
      "id": 2,
      "name": "Bob",
      "roles": ["user"]
    }
  ],
  "total": 2
}
```

Much more readable!

## Example 4: YAML Formatting

### Before Formatting

```yaml
name: Deploy
on:
  push:
   branches: [main]
jobs:
  deploy:
   runs-on: ubuntu-latest
   steps:
    - uses: actions/checkout@v2
    - name: Deploy
      run: |
       npm install
       npm run build
```

### After Formatting

```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy
        run: |
          npm install
          npm run build
```

Consistent indentation applied.

## Configuration

### Location

```
.claude/hooks.json - Hook configuration
.claude/hooks/format-file.sh - Formatting script
.claude/hooks/format-hook.md - Hook prompt
```

### Hook Configuration

```json
{
  "hooks": [
    {
      "hookId": "format-on-edit",
      "eventType": "PostToolUse",
      "toolPattern": "^(Edit|Write)$",
      "promptFile": ".claude/hooks/format-hook.md",
      "enabled": true
    }
  ]
}
```

### Customization

Edit `.claude/hooks/format-file.sh` to customize:

```bash
#!/bin/bash

FILE_PATH="$1"

# Python formatting
if [[ "$FILE_PATH" == *.py ]]; then
  if command -v ruff &>/dev/null; then
    ruff format "$FILE_PATH"
    # Add additional formatting
    # autopep8 --in-place "$FILE_PATH"
  fi
fi

# Add support for other languages
if [[ "$FILE_PATH" == *.js ]] || [[ "$FILE_PATH" == *.ts ]]; then
  if command -v prettier &>/dev/null; then
    prettier --write "$FILE_PATH"
  fi
fi

# Custom formatter
if [[ "$FILE_PATH" == *.custom ]]; then
  my-formatter "$FILE_PATH"
fi
```

## Supported File Types

| File Type | Formatter | Config |
|-----------|-----------|--------|
| `.py` | ruff | `ruff.toml` or `pyproject.toml` |
| `.md` | prettier | `.prettierrc` |
| `.json` | prettier | `.prettierrc` |
| `.yml`, `.yaml` | prettier | `.prettierrc` |

To add more:
1. Install formatter tool
2. Add file extension check to `format-file.sh`
3. Run formatter command

## Formatter Installation

### Ruff (Python)

```bash
pip install ruff
# or
uv add --dev ruff
```

### Prettier (Markdown, JSON, YAML)

```bash
npm install -D prettier
# or
yarn add -D prettier
```

## Disabling the Hook

### Temporarily

Comment out in `.claude/hooks.json`:

```json
{
  "hooks": [
    {
      "hookId": "format-on-edit",
      "enabled": false,  // Disable
      ...
    }
  ]
}
```

### For Specific Files

Add to `.prettierignore` or formatter config:

```
# .prettierignore
generated/
*.min.json
docs/examples/*.md
```

### Permanently

Remove hook configuration from `.claude/hooks.json`.

## Benefits

### Consistency
- All code follows same style
- No manual formatting needed
- Reduces diff noise in PRs

### Time Saving
- Automatic formatting as you work
- No need to run formatters manually
- Focus on logic, not style

### Code Quality
- Catches syntax errors early
- Enforces best practices
- Improves readability

## Common Issues

### Formatter Not Found

**Problem:**
```
🔄 Formatting Python file: utils.py
❌ ruff not found, skipping formatting
```

**Solution:**
```bash
# Install the formatter
pip install ruff
# or for prettier
npm install -D prettier

# Verify installation
ruff --version
prettier --version
```

### Formatting Errors

**Problem:**
```
🔄 Formatting JSON file: config.json
❌ Formatting failed: SyntaxError: Unexpected token
```

**Solution:**
```bash
# File has syntax errors
# Fix the syntax before formatting
# Or check formatter config
```

### Unwanted Changes

**Problem:** Hook formats code differently than expected

**Solution:**
```bash
# Configure formatter settings
# For ruff: Create ruff.toml
[format]
quote-style = "single"
indent-width = 2

# For prettier: Create .prettierrc
{
  "singleQuote": true,
  "tabWidth": 2
}
```

### Performance Impact

**Problem:** Hook slows down file editing

**Solution:**
```bash
# Disable for large files
# Or optimize formatter settings
# Or disable hook temporarily
```

## Integration with Workflows

### Standard Workflow
```
1. User asks Claude to edit code
2. Claude uses Edit tool
3. Hook runs automatically
4. File is formatted
5. User sees formatted result
```

### With Pre-commit Hook
```
1. Claude edits files (format hook runs)
2. Files are properly formatted
3. git add <files>
4. git commit
5. Pre-commit hook validates
6. Commit succeeds (code already formatted)
```

### Team Workflow
```
1. Configure formatter settings in repo
2. All team members have hook enabled
3. All edits are auto-formatted consistently
4. PRs have minimal formatting diff
5. Code reviews focus on logic
```

## Best Practices

### DO
✅ Configure formatter settings in project config
✅ Install required formatters in project
✅ Commit formatter configs to version control
✅ Keep hook script simple and fast

### DON'T
❌ Fight the formatter with manual changes
❌ Disable hook without team agreement
❌ Use multiple conflicting formatters
❌ Skip formatter installation

## Related Hooks

- [Pre-commit Hook](./pre-commit-hook.md) - Validates before commits
- [Post-generate Hook](./post-generate-hook.md) - Runs after code generation

## See Also

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Prettier Documentation](https://prettier.io/docs/en/)
- [.claude/hooks/README.md](../../../.claude/hooks/README.md) - Hook configuration guide
