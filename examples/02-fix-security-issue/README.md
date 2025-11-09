# Example 2: Fix Security Issue (CORS Configuration)

This example demonstrates how to fix a security vulnerability identified by code analysis.

## Scenario

The `/analyze` command identified a **CRITICAL** CORS misconfiguration in the backend API.

## The Problem

**File:** `apps/backend/src/backend/app.py:21-27`
**Severity:** CRITICAL
**Issue:** CORS configured with `allow_origins=["*"]` and `allow_credentials=True`

**Security Risks:**
- Session hijacking
- CSRF attacks
- Data theft from legitimate users
- Any malicious website can make authenticated requests

---

## Workflow: Fix Without Spec

For bug fixes and security issues, you typically **don't write a spec**. Instead:

```
1. Identify Issue (via /analyze or manual review)
2. Understand the Fix
3. Implement the Fix
4. Test the Fix
5. Commit
```

---

## Step-by-Step Fix Process

### Step 1: Run Code Analysis

**Prompt to Claude:**
```
/analyze
```

**Claude identifies:**
```
🔴 Critical: CORS Security Misconfiguration
File: apps/backend/src/backend/app.py:21-27

The CORS configuration allows ALL origins (*) with credentials enabled.
This is a security vulnerability that enables CSRF attacks and session hijacking.
```

---

### Step 2: Ask for Fix Recommendation

**Prompt to Claude:**
```
Show me how to fix the CORS configuration issue.
Provide the complete fixed code.
```

**Claude explains the issue and provides the fix** (see `before.py` and `after.py` in this directory).

---

### Step 3: Implement the Fix

**Prompt to Claude:**
```
Fix the CORS configuration in apps/backend/src/backend/app.py
Use environment variables for allowed origins.
Default to localhost:8080 for development.
```

**Claude makes the changes:**

#### Before (Insecure):
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ DANGEROUS
    allow_credentials=True,  # ⚠️ FORBIDDEN with ["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### After (Secure):
```python
import os

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:8080"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # ✅ Specific origins
    allow_credentials=True,  # ✅ Safe with specific origins
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # ✅ Explicit
    allow_headers=["Content-Type", "Authorization"],  # ✅ Explicit
    max_age=600,
)
```

---

### Step 4: Test the Fix

**Prompt to Claude:**
```
Run the backend tests to verify the CORS fix doesn't break anything
```

**Commands:**
```bash
task test:backend
```

**Expected result:** All tests pass ✓

**Manual verification:**
1. Start the backend: `task backend:dev`
2. Try accessing from allowed origin (localhost:8080) - Should work
3. Try accessing from disallowed origin - Should be blocked

---

### Step 5: Verify Security

**Prompt to Claude:**
```
Verify that the CORS configuration is now secure.
Run /analyze again to confirm.
```

**Claude re-analyzes and confirms:**
```
✅ CORS configuration is now secure
- Specific origins only
- Safe with credentials enabled
- Explicit methods and headers
```

---

### Step 6: Document the Fix

**Optional but recommended:** Add a comment explaining why:

```python
# CORS Configuration
# Restricts API access to specific origins to prevent CSRF attacks
# and session hijacking. Configure via ALLOWED_ORIGINS environment variable.
# Production: ALLOWED_ORIGINS="https://yourdomain.com"
# Development: Defaults to localhost:3000,localhost:8080
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:8080"
).split(",")
```

---

### Step 7: Commit the Fix

**Prompt to Claude:**
```
/commit
```

**Claude creates commit:**
```
fix: Secure CORS configuration to prevent CSRF attacks

Replace wildcard CORS origins with environment-based whitelist.

Changes:
- Replace allow_origins=["*"] with specific allowed origins
- Make origins configurable via ALLOWED_ORIGINS environment variable
- Make HTTP methods and headers explicit (not wildcard)
- Add max_age for preflight request caching
- Default to localhost origins for development

Security Fix:
- Prevents CSRF attacks
- Prevents session hijacking
- Prevents unauthorized cross-origin requests

Fixes: Critical CORS misconfiguration identified by /analyze

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Configuration for Different Environments

### Development
```bash
# .env or shell
export ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8080"
```

### Staging
```bash
export ALLOWED_ORIGINS="https://staging.yourdomain.com"
```

### Production
```bash
export ALLOWED_ORIGINS="https://yourdomain.com,https://www.yourdomain.com"
```

### Docker
```yaml
# docker-compose.yml
services:
  backend:
    environment:
      - ALLOWED_ORIGINS=https://yourdomain.com
```

---

## Testing the Fix

### Test 1: Allowed Origin (Should Work)
```bash
curl -H "Origin: http://localhost:8080" \
     -H "Access-Control-Request-Method: GET" \
     -X OPTIONS \
     http://localhost:8000/api/hello
```

**Expected:** Returns CORS headers allowing the request

### Test 2: Disallowed Origin (Should Block)
```bash
curl -H "Origin: https://evil.com" \
     -H "Access-Control-Request-Method: GET" \
     -X OPTIONS \
     http://localhost:8000/api/hello
```

**Expected:** No `Access-Control-Allow-Origin` header for evil.com

---

## Key Takeaways

### When to Skip Specs

**DO write specs for:**
- New features
- API changes
- Architecture decisions

**DON'T write specs for:**
- Bug fixes
- Security fixes
- Refactoring (unless major)
- Typos and formatting

### Security Fix Workflow

1. **Identify** - Use `/analyze` or security tools
2. **Understand** - Ask Claude to explain the vulnerability
3. **Fix** - Implement the recommended solution
4. **Test** - Verify the fix works and doesn't break things
5. **Verify** - Re-analyze to confirm fix
6. **Commit** - Clear commit message explaining the security issue

### Best Practices

✅ **Always test security fixes** - Don't assume they work
✅ **Use environment variables** - For configuration flexibility
✅ **Be explicit** - Avoid wildcards in security settings
✅ **Document the why** - Explain security decisions
✅ **Re-analyze after fixing** - Verify the issue is resolved

---

## Related Examples

- [Example 1: Spec-Driven Development](../01-spec-driven-development/)
- [Example 3: Add Feature](../03-add-feature/)
- [Example 4: Refactoring](../04-refactoring/)

## See Also

- [Code Analysis Documentation](../../docs/workflows.md#code-analysis)
- [Security Best Practices](../../docs/security.md) (if exists)
- `/analyze` command documentation
