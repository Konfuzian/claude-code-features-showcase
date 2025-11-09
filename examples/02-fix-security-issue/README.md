# Example 2: Fix Security Issue

How to fix security vulnerabilities quickly without writing specs.

## The Workflow (1-2 Prompts)

### Prompt 1: Identify Issues
```
/analyze
```

**Claude finds:**
- 🔴 **CRITICAL**: CORS misconfiguration in [apps/backend/src/backend/app.py:21-27](../../apps/backend/src/backend/app.py#L21-L27)
- `allow_origins=["*"]` with `allow_credentials=True` enables CSRF attacks and session hijacking

---

### Prompt 2: Fix the Issue
```
Fix the CORS configuration in apps/backend/src/backend/app.py
Use environment variables for allowed origins.
```

**Claude automatically:**
- Replaces wildcard origins with specific allowed origins
- Makes configuration environment-based
- Updates to explicit methods and headers
- Runs tests to verify the fix
- Commits with security fix message

Done! ✅

---

## The Fix

**Claude changes:**

**Before (Insecure):**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # ⚠️ DANGEROUS
    allow_credentials=True,        # ⚠️ FORBIDDEN with ["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**After (Secure):**
```python
import os

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:8080"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # ✅ Specific origins
    allow_credentials=True,         # ✅ Safe with specific origins
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    max_age=600,
)
```

---

## When to Use This Workflow

**Use /analyze → fix for:**
- ✅ Security vulnerabilities
- ✅ Bug fixes
- ✅ Code quality issues
- ✅ Performance problems

**Don't write specs for:**
- ❌ Bug fixes
- ❌ Security fixes
- ❌ Quick patches

---

## Configuration Examples

### Development
```bash
export ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8080"
```

### Production
```bash
export ALLOWED_ORIGINS="https://yourdomain.com,https://www.yourdomain.com"
```

---

## Verifying the Fix

### Test with curl
```bash
# Allowed origin (should work)
curl -H "Origin: http://localhost:8080" \
     -H "Access-Control-Request-Method: GET" \
     -X OPTIONS \
     http://localhost:8000/api/hello

# Disallowed origin (should block)
curl -H "Origin: https://evil.com" \
     -H "Access-Control-Request-Method: GET" \
     -X OPTIONS \
     http://localhost:8000/api/hello
```

---

## See Also

- [Example 1: Spec-Driven Development](../01-spec-driven-development/) - Complex features
- [Example 3: Add Feature](../03-add-feature/) - Quick features
- [Example 4: Refactoring](../04-refactoring/) - Improving code quality
