# Example 3: Add a Feature

How to add simple features quickly without writing specs.

## The Workflow (1 Prompt)

### Prompt: Describe What You Want
```
Add a new API endpoint /api/version that returns:
{
  "version": "0.1.0",
  "python_version": "3.12",
  "fastapi_version": "<version>"
}

Add it to apps/backend/src/backend/routes.py and write tests.
```

**Claude automatically:**
- Implements the endpoint in [routes.py](../../apps/backend/src/backend/routes.py)
- Adds tests in [test_routes.py](../../apps/backend/tests/test_routes.py)
- Runs tests to verify it works
- Commits with feature description

Done! ✅

---

## The Implementation

**Claude adds to routes.py:**
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

**Claude adds test:**
```python
def test_api_version():
    """Test version endpoint returns correct structure."""
    response = client.get("/api/version")
    assert response.status_code == 200

    data = response.json()
    assert "version" in data
    assert "python_version" in data
    assert "fastapi_version" in data
```

---

## More Quick Feature Examples

**Add logging:**
```
Add logging to the PDF reader for file opens and errors
```

**Add validation:**
```
Add input validation to XLSX reader to ensure file extension is .xlsx
```

**Add configuration:**
```
Make the backend port configurable via environment variable PORT
```

---

## When to Use This Workflow

**Use simple 1-prompt for:**
- ✅ Single endpoints
- ✅ Configuration changes
- ✅ Small utilities
- ✅ Simple validations

**Write a spec instead for:**
- ❌ Complex features with multiple requirements
- ❌ Features needing design review
- ❌ Long-term maintained APIs

---

## When to Switch to Spec-Driven

If during implementation you realize:
- Requirements aren't clear
- Many edge cases exist
- Multiple design decisions needed
- Feature is larger than expected

**STOP and write a spec:**
```
This is getting complex. Write a spec for [feature] in specs/planned/
```

Then follow [Example 1: Spec-Driven Development](../01-spec-driven-development/)

---

## See Also

- [Example 1: Spec-Driven Development](../01-spec-driven-development/) - Complex features
- [Example 2: Fix Security Issue](../02-fix-security-issue/) - Bug fixes
- [Example 4: Refactoring](../04-refactoring/) - Code improvements
