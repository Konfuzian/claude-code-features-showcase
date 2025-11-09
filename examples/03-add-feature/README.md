# Example 3: Add a Feature (Without Full Spec)

This example shows how to add a feature quickly without writing a formal specification.

## Scenario

You want to add a new API endpoint `/api/version` that returns version information.

## When to Skip the Spec

**Write a spec when:**
- Feature is complex or has many requirements
- Multiple people need to agree on the design
- API design needs review
- Feature will be maintained long-term

**Skip the spec when:**
- Feature is simple and straightforward
- You're prototyping or experimenting
- It's a minor addition to existing functionality
- Requirements are crystal clear

---

## Quick Feature Workflow

```
1. Describe the Feature
2. Implement
3. Test
4. Commit
```

---

## Step-by-Step Process

### Step 1: Describe What You Want

**Prompt to Claude:**
```
Add a new API endpoint /api/version that returns:
{
  "version": "0.1.0",
  "python_version": "3.12",
  "fastapi_version": "<version>"
}

Add it to apps/backend/src/backend/routes.py
```

---

### Step 2: Claude Implements

**Claude adds to `routes.py`:**

```python
import sys
import fastapi

@router.get("/api/version")
async def api_version():
    """Return version information."""
    return {
        "version": "0.1.0",
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "fastapi_version": fastapi.__version__,
    }
```

---

### Step 3: Test It

**Prompt to Claude:**
```
Add a test for the /api/version endpoint
```

**Claude adds to `test_routes.py`:**

```python
def test_api_version():
    """Test version endpoint returns correct structure."""
    response = client.get("/api/version")
    assert response.status_code == 200

    data = response.json()
    assert "version" in data
    assert "python_version" in data
    assert "fastapi_version" in data
    assert data["version"] == "0.1.0"
```

**Run tests:**
```
task test:backend
```

---

### Step 4: Manual Verification

```bash
# Start the server
task backend:dev

# In another terminal
curl http://localhost:8000/api/version
```

**Expected output:**
```json
{
  "version": "0.1.0",
  "python_version": "3.12",
  "fastapi_version": "0.109.0"
}
```

---

### Step 5: Commit

**Prompt to Claude:**
```
/commit
```

**Claude creates:**
```
feat: Add /api/version endpoint

Add endpoint to return version information including app version,
Python version, and FastAPI version.

Changes:
- Add GET /api/version endpoint in routes.py
- Add test for version endpoint
- Returns JSON with version info

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## More Examples

### Example: Add Logging

**Prompt:**
```
Add logging to the PDF reader.
Log when files are opened, pages extracted, and errors occur.
Use Python's logging module.
```

**Claude implements:**
```python
import logging

logger = logging.getLogger(__name__)

def read_pdf(file_path: str | Path) -> str:
    logger.info(f"Reading PDF: {file_path}")
    # ... implementation
    logger.info(f"Successfully extracted {len(text)} characters")
    return text
```

---

### Example: Add Validation

**Prompt:**
```
Add input validation to the XLSX reader to ensure file extension is .xlsx
Raise ValueError with a clear message if the extension is wrong.
```

**Claude implements:**
```python
def read_xlsx(file_path: str | Path) -> Dict[str, List[List[Any]]]:
    path = Path(file_path)

    if path.suffix.lower() != '.xlsx':
        raise ValueError(
            f"Invalid file type: {path.suffix}. "
            f"Expected .xlsx file, got {path.name}"
        )

    # ... rest of implementation
```

---

### Example: Add Configuration

**Prompt:**
```
Make the backend port configurable via environment variable.
Default to 8000 if not set.
Update apps/backend/src/backend/main.py
```

**Claude implements:**
```python
import os

def main():
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")

    uvicorn.run(app, host=host, port=port)
```

---

## Iterative Development

### Start Simple
```
Add a /api/stats endpoint that returns request count
```

### Then Enhance
```
Update /api/stats to also return:
- uptime
- last request time
- total requests per endpoint
```

### Then Refine
```
Add caching to /api/stats so it only updates every 60 seconds
```

Each step is small and testable!

---

## When Things Get Complex

If during implementation you realize:
- Requirements aren't clear
- There are many edge cases
- Multiple design decisions needed
- Feature is larger than expected

**STOP and write a spec!**

**Prompt:**
```
This feature is getting complex. Let's write a proper spec for it.
Create specs/planned/stats-endpoint.md with:
- Requirements
- API design
- Edge cases
- Performance considerations
```

Then follow the spec-driven workflow from Example 1.

---

## Quick Reference

### Simple Feature Checklist

- [ ] Describe the feature clearly
- [ ] Implement the change
- [ ] Add/update tests
- [ ] Run tests to verify
- [ ] Manual verification if needed
- [ ] Commit with clear message

### Prompts for Quick Features

**Add endpoint:**
```
Add a GET /api/[name] endpoint that returns [description]
```

**Add function:**
```
Add a function [name] to [file] that [does what]
```

**Add validation:**
```
Add validation to [function] to check that [condition]
```

**Add configuration:**
```
Make [setting] configurable via environment variable [VAR_NAME]
```

**Add logging:**
```
Add logging to [module] for [events]
```

**Add error handling:**
```
Add error handling to [function] for [error cases]
```

---

## Key Principles

1. **Keep it small** - One feature at a time
2. **Test immediately** - Don't accumulate untested changes
3. **Commit often** - Each working feature gets a commit
4. **Be specific** - Clear prompts get better results
5. **Verify manually** - Run the code, don't just trust tests

---

## See Also

- [Example 1: Spec-Driven Development](../01-spec-driven-development/) - For complex features
- [Example 2: Fix Security Issue](../02-fix-security-issue/) - For bug fixes
- [Example 4: Refactoring](../04-refactoring/) - For code improvements
