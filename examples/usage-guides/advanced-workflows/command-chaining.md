# Advanced Workflow: Command Chaining

## Overview

Command chaining combines multiple Claude Code commands in sequence to create powerful, automated workflows. This guide shows how to chain commands effectively for maximum productivity.

## Common Command Chains

### Quality Assurance Chain

**Goal:** Ensure code quality before committing

```
/x-analyze → Fix issues → /x-test → /x-commit
```

**Detailed Steps:**

1. **Analyze Code**
   ```
   /x-analyze
   ```
   Output:
   ```
   Found 3 security issues and 2 code quality problems:
   - SQL injection vulnerability in auth.js
   - Missing input validation in api.js
   - Code duplication in utils.js
   ```

2. **Fix Issues**
   ```
   Please fix the SQL injection and add input validation
   ```
   Claude fixes the code using Edit tool.

3. **Generate Tests**
   ```
   /x-test
   ```
   Creates tests for the fixed code.

4. **Commit Changes**
   ```
   /x-commit
   ```
   Commits with message: "fix: Resolve security vulnerabilities and add tests"

### Documentation Chain

**Goal:** Document new features comprehensively

```
Implement feature → /x-test → /x-docs → /x-commit
```

**Example:**

1. **Implement Feature**
   ```
   Add a password reset feature with email verification
   ```
   Claude implements the feature.

2. **Add Tests**
   ```
   /x-test
   ```
   Generates comprehensive tests.

3. **Generate Documentation**
   ```
   /x-docs
   ```
   Creates API documentation and usage examples.

4. **Commit Everything**
   ```
   /x-commit
   ```
   Commits code + tests + docs together.

### Refactoring Chain

**Goal:** Safely refactor with test coverage

```
/x-test → /x-test-coverage → /x-refactor → Run tests → /x-commit
```

**Example:**

1. **Ensure Test Coverage**
   ```
   /x-test
   Add tests for the authentication module before refactoring
   ```

2. **Check Coverage**
   ```
   /x-test-coverage
   ```
   Verifies adequate test coverage before refactoring.

3. **Refactor**
   ```
   /x-refactor
   Simplify the authentication logic
   ```

4. **Verify Tests Pass**
   ```
   Run the test suite and verify all tests still pass
   ```

5. **Commit**
   ```
   /x-commit
   ```

## Advanced Patterns

### Full Feature Development Workflow

```mermaid
graph LR
    A[Implement Feature] --> B[/x-analyze]
    B --> C[Fix Issues]
    C --> D[/x-test]
    D --> E[Run Tests]
    E --> F{Tests Pass?}
    F -->|No| D
    F -->|Yes| G[/x-docs]
    G --> H[/x-test-coverage]
    H --> I{Coverage OK?}
    I -->|No| D
    I -->|Yes| J[/x-commit]
```

**Step-by-Step:**

```
1. Implement authentication with JWT tokens

2. /x-analyze
   → Finds: Missing token expiration validation

3. Add token expiration validation

4. /x-test
   → Generates tests for auth + token expiration

5. npm test
   → All tests pass

6. /x-docs
   → Creates API documentation

7. /x-test-coverage
   → Coverage: 92% (target: 80%+) ✓

8. /x-commit
   → Commits feature + tests + docs
```

### Security-Focused Workflow

**Goal:** Ensure security at every step

```
Implement → /x-analyze (security focus) → Fix → /x-test (security tests) → /x-commit
```

**Example:**

```
1. Please implement user authentication with email and password

2. /x-analyze
   Please focus on security vulnerabilities

   Output:
   - ❌ Passwords stored in plain text
   - ❌ No rate limiting on login endpoint
   - ❌ Session tokens not using HTTPS-only cookies

3. Fix all security issues found

4. /x-test
   Generate tests including security test cases:
   - Brute force protection
   - Token theft prevention
   - SQL injection attempts

5. npm test
   Verify all security tests pass

6. /x-commit
```

### Data-Driven Development Workflow

**Goal:** Build features from specifications in documents

```
Read spec (PDF/Excel) → Implement → /x-test → Validate against spec → /x-commit
```

**Example:**

```
1. Read the API specification from docs/api-spec.pdf

   (x-pdf-reader skill invoked automatically)

   Extracted requirements:
   - POST /api/users - Create user
   - GET /api/users/:id - Get user
   - Required fields: name, email, role
   - Email must be unique
   - Role must be: admin, user, or guest

2. Implement the API endpoints based on the specification

3. /x-test
   Generate tests covering all requirements from the spec

4. Please verify the implementation matches the specification

   Claude compares implementation against spec requirements.

5. /x-commit
```

### Continuous Improvement Workflow

**Goal:** Iteratively improve code quality

```
/x-test-coverage → Identify gaps → /x-test → /x-refactor → /x-analyze → /x-commit
```

**Example:**

```
1. /x-test-coverage

   Coverage Report:
   - auth.js: 45% (LOW)
   - api.js: 78% (FAIR)
   - utils.js: 92% (GOOD)

2. Focus on auth.js - generate tests for uncovered paths

3. /x-test
   Generate tests specifically for:
   - Token refresh logic
   - Password reset flow
   - Session expiration

4. /x-refactor
   Simplify auth.js to make it more testable

5. /x-analyze
   Check if refactoring introduced any issues

6. npm test
   Verify all tests pass

7. /x-test-coverage

   New coverage:
   - auth.js: 87% (GOOD) ✓

8. /x-commit
```

## Combining Skills and Commands

### Skill + Command Chains

**Example: Process Excel Data → Generate Code → Test → Commit**

```
1. Read customer data from customers.xlsx

   (x-xlsx-reader skill invoked)

   Found 142 customers with fields:
   - id, name, email, phone, status

2. Create a TypeScript interface for this data structure

   Creates Customer interface based on Excel columns.

3. Generate validation functions for the customer data

4. /x-test
   Generate tests for validation functions

5. /x-commit
```

**Example: Review PDF Spec → Implement → Document → Commit**

```
1. Read requirements from spec.pdf and implement the user registration flow

   (x-pdf-reader skill invoked)

   Requirements extracted:
   - Email verification required
   - Password must meet complexity requirements
   - Welcome email sent on registration

2. Implementation created based on requirements

3. /x-test
   Generate tests covering all requirements

4. /x-docs
   Document the registration API

5. /x-commit
```

## Workflow Templates

### Template 1: New Feature (Complete)

```bash
# 1. Implement
Implement [feature description]

# 2. Quality check
/x-analyze

# 3. Fix issues if any
[Fix reported issues]

# 4. Add tests
/x-test

# 5. Verify tests
npm test

# 6. Document
/x-docs

# 7. Check coverage
/x-test-coverage

# 8. Commit
/x-commit
```

### Template 2: Bug Fix (Fast)

```bash
# 1. Analyze issue
/x-analyze

# 2. Fix bug
[Fix the bug]

# 3. Add regression test
/x-test

# 4. Verify fix
npm test

# 5. Commit
/x-commit
```

### Template 3: Refactoring (Safe)

```bash
# 1. Ensure test coverage
/x-test
/x-test-coverage

# 2. Refactor
/x-refactor

# 3. Verify tests still pass
npm test

# 4. Check for new issues
/x-analyze

# 5. Commit
/x-commit
```

### Template 4: Documentation Update

```bash
# 1. Generate docs
/x-docs

# 2. Review and refine
[Manual review]

# 3. Commit
/x-commit
```

## Tips for Effective Chaining

### 1. Order Matters

**Good:**
```
/x-test → /x-refactor → npm test
```
Tests first provide safety net for refactoring.

**Bad:**
```
/x-refactor → /x-test
```
Refactoring without tests is risky.

### 2. Verify Between Steps

Always verify success before proceeding:
```
/x-test
→ Check tests were created
→ Run tests to ensure they pass
→ THEN proceed to /x-commit
```

### 3. Use Focused Commands

Be specific about what you want:
```
# Vague
/x-analyze

# Better
/x-analyze
Focus on security vulnerabilities in the authentication code
```

### 4. Automate Repetitive Chains

Create custom commands for common chains:

```markdown
<!-- .claude/commands/x-feature.md -->
---
name: x-feature
description: Complete feature development workflow
---

When the user uses this command:

1. Analyze code with /x-analyze
2. Generate tests with /x-test
3. Generate documentation with /x-docs
4. Run /x-test-coverage to verify coverage
5. Finally /x-commit to commit everything

Execute each step and verify success before proceeding.
```

## Common Pitfalls

### ❌ Committing Too Early

```
Implement → /x-commit
```

**Missing:** Testing, analysis, documentation

### ❌ Skipping Verification

```
/x-test → /x-commit
```

**Missing:** Running tests to verify they pass

### ❌ No Safety Net

```
/x-refactor → /x-commit
```

**Missing:** Tests before refactoring

### ✅ Complete Workflow

```
Implement → /x-analyze → Fix → /x-test → npm test → /x-docs → /x-commit
```

## Real-World Examples

### Example 1: Payment Integration

```
1. Read payment API docs from payment-api.pdf
2. Implement payment processing based on docs
3. /x-analyze (focus on security)
4. Fix: Add input validation and error handling
5. /x-test (include edge cases: declined cards, timeouts)
6. npm test
7. /x-docs
8. /x-test-coverage
9. /x-commit
```

### Example 2: Database Migration

```
1. Read data mapping from migration-spec.xlsx
2. Generate migration scripts based on mapping
3. /x-test (create migration tests)
4. /x-refactor (optimize migration for large datasets)
5. /x-analyze (check for performance issues)
6. /x-docs (document migration steps)
7. /x-commit
```

### Example 3: API Redesign

```
1. /x-test-coverage (ensure current API is well-tested)
2. /x-refactor (redesign API structure)
3. npm test (verify backward compatibility)
4. /x-docs (update API documentation)
5. /x-analyze (check for breaking changes)
6. /x-commit
```

## See Also

- [Commands Guide](../commands/) - Individual command documentation
- [Skills Guide](../skills/) - Individual skill documentation
- [Workflow Examples](../../) - Complete workflow examples
