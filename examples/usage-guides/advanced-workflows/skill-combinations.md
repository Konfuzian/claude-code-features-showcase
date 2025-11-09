# Advanced Workflow: Skill Combinations

## Overview

Skills can be combined to create powerful, automated workflows. This guide demonstrates how different skills work together to accomplish complex tasks.

## Common Skill Combinations

### 1. Document Processing + Code Generation

**Combination:** x-pdf-reader + x-test-generator

**Use Case:** Generate tests from test case documentation

**Example:**

```
Read the test scenarios from test-cases.pdf and generate comprehensive tests for the authentication module
```

**What Happens:**

1. **x-pdf-reader** extracts test scenarios from PDF
   ```
   Test Scenarios Extracted:

   1. Valid Login
      - Input: valid email/password
      - Expected: JWT token returned, redirect to dashboard

   2. Invalid Password
      - Input: valid email, wrong password
      - Expected: 401 error, "Invalid credentials" message

   3. Account Locked
      - Input: locked account credentials
      - Expected: 403 error, "Account locked" message
   ```

2. **x-test-generator** creates tests based on scenarios
   ```javascript
   describe('Authentication', () => {
     it('should return JWT token on valid login', async () => {
       const response = await login('user@example.com', 'ValidPass123!');
       expect(response.status).toBe(200);
       expect(response.data.token).toBeDefined();
       expect(response.data.redirectUrl).toBe('/dashboard');
     });

     it('should return 401 for invalid password', async () => {
       const response = await login('user@example.com', 'WrongPass');
       expect(response.status).toBe(401);
       expect(response.data.error).toBe('Invalid credentials');
     });

     it('should return 403 for locked account', async () => {
       const response = await login('locked@example.com', 'Password123!');
       expect(response.status).toBe(403);
       expect(response.data.error).toBe('Account locked');
     });
   });
   ```

### 2. Spreadsheet Analysis + Code Review

**Combination:** x-xlsx-reader + x-code-reviewer

**Use Case:** Review code against a compliance checklist

**Example:**

```
Read the security checklist from security-requirements.xlsx and review my authentication code against it
```

**What Happens:**

1. **x-xlsx-reader** extracts security requirements
   ```
   Security Requirements:
   ✓ Passwords must be hashed with bcrypt
   ✓ Rate limiting on login endpoint
   ✓ HTTPS-only session cookies
   ✓ Input validation on all fields
   ✓ SQL injection prevention
   ✓ XSS prevention
   ```

2. **x-code-reviewer** audits code against each requirement
   ```
   Security Audit Results:

   ✅ Passwords hashed with bcrypt - PASS
   ❌ Rate limiting - MISSING
      No rate limiting detected on /login endpoint

   ✅ HTTPS-only cookies - PASS
      httpOnly: true, secure: true

   ⚠️ Input validation - PARTIAL
      Email validated, but password validation missing

   ✅ SQL injection prevention - PASS
      Using parameterized queries

   ✅ XSS prevention - PASS
      Output properly escaped

   Score: 4.5/6 requirements met
   ```

### 3. Multi-Document Analysis

**Combination:** x-pdf-reader + x-xlsx-reader + x-code-reviewer

**Use Case:** Validate implementation against multiple specification sources

**Example:**

```
Compare my user management implementation against:
- Technical spec in spec.pdf
- Data requirements in data-model.xlsx
- Security requirements checklist
```

**What Happens:**

1. **x-pdf-reader** extracts technical requirements
2. **x-xlsx-reader** extracts data model specifications
3. **x-code-reviewer** validates implementation against both

**Output:**

```
Implementation Validation Report:

FROM spec.pdf:
✅ User CRUD operations implemented
✅ Email verification flow complete
❌ Password reset with 2FA - Missing 2FA

FROM data-model.xlsx:
✅ User table has all required fields
⚠️ User.role field: spec says ENUM, code uses VARCHAR
✅ Indexes on email and username
❌ Missing created_at/updated_at timestamps

Security Checklist:
✅ Password hashing
✅ SQL injection prevention
❌ Rate limiting not implemented

Summary:
- 8/11 requirements met (73%)
- 3 critical issues to fix
- 2 warnings to address
```

### 4. Data-Driven Code Generation

**Combination:** x-xlsx-reader + x-test-generator

**Use Case:** Generate tests from data in spreadsheets

**Example:**

```
Read the test data from test-inputs.xlsx and generate parameterized tests
```

**What Happens:**

1. **x-xlsx-reader** extracts test data

   | Input | Expected Output | Test Case |
   |-------|----------------|-----------|
   | "" | Error: Required | Empty email |
   | "invalid" | Error: Invalid format | Malformed email |
   | "user@example.com" | Valid | Valid email |
   | "user@" | Error: Invalid domain | Missing domain |

2. **x-test-generator** creates parameterized tests

   ```javascript
   describe('Email Validation', () => {
     const testCases = [
       { input: '', expected: 'Error: Required', case: 'Empty email' },
       { input: 'invalid', expected: 'Error: Invalid format', case: 'Malformed email' },
       { input: 'user@example.com', expected: 'Valid', case: 'Valid email' },
       { input: 'user@', expected: 'Error: Invalid domain', case: 'Missing domain' },
     ];

     testCases.forEach(({ input, expected, case: testCase }) => {
       it(testCase, () => {
         const result = validateEmail(input);
         expect(result).toBe(expected);
       });
     });
   });
   ```

## Advanced Patterns

### Pattern 1: Spec-to-Code Pipeline

**Skills:** x-pdf-reader → x-test-generator → x-code-reviewer

**Workflow:**

```
1. Read API specification from api-spec.pdf

2. Generate API endpoint stubs based on spec

3. Generate tests from spec requirements

4. Implement endpoints to pass tests (TDD)

5. Review implementation against spec using x-code-reviewer
```

**Example:**

```
Step 1: Read api-spec.pdf
→ Extracted 15 endpoints with request/response schemas

Step 2: Generate TypeScript interfaces from spec

Step 3: Generate test cases for each endpoint
→ Created 45 test cases covering:
  - Happy paths
  - Error cases
  - Edge cases

Step 4: Implement endpoints
[Claude implements each endpoint]

Step 5: Review against spec
→ All endpoints match specification ✓
→ All test cases pass ✓
```

### Pattern 2: Data Migration Validation

**Skills:** x-xlsx-reader → x-code-reviewer

**Workflow:**

```
1. Read old data schema from old-schema.xlsx

2. Read new data schema from new-schema.xlsx

3. Review migration script for correctness

4. Generate validation tests
```

**Example:**

```
Old Schema (from old-schema.xlsx):
- users: id, name, email, phone

New Schema (from new-schema.xlsx):
- users: id, first_name, last_name, email, phone_number, created_at

Migration Script Review:
✅ id mapped correctly
❌ name splitting logic: doesn't handle single names
✅ email mapped correctly
⚠️ phone → phone_number: no validation/formatting
❌ created_at: not populated for existing records

Recommendations:
1. Handle single-word names (use as first_name, last_name = '')
2. Add phone number validation
3. Set created_at = NOW() for migrated records
```

### Pattern 3: Compliance Audit

**Skills:** x-pdf-reader + x-xlsx-reader + x-code-reviewer

**Workflow:**

```
1. Read compliance standards from GDPR-requirements.pdf

2. Read data inventory from data-inventory.xlsx

3. Review codebase for compliance violations
```

**Example:**

```
GDPR Requirements (from PDF):
- User consent before data collection
- Data retention limits
- Right to deletion
- Data encryption at rest
- Audit logging

Data Inventory (from Excel):
- Users: email, name, phone (PII)
- Orders: address, payment info (PII)
- Logs: IP addresses (PII)

Compliance Audit Results:

User Consent:
❌ No consent collection before email signup
❌ No cookie consent banner

Data Retention:
❌ No retention policy implemented
❌ Old records never deleted

Right to Deletion:
⚠️ Delete user endpoint exists but doesn't cascade to:
   - Order history
   - Audit logs
   - Cached data

Encryption:
✅ Passwords hashed
❌ PII stored in plain text
❌ Database not encrypted at rest

Audit Logging:
⚠️ Partial - logs some actions but not data access

Compliance Score: 2/10 ⚠️ CRITICAL
```

## Real-World Scenarios

### Scenario 1: API Development from Specification

**Context:** Building an API from provided specification documents

**Skills Used:** x-pdf-reader, x-test-generator, x-code-reviewer

```
User: "I have an API spec in api-spec.pdf. Please implement it with full test coverage."

Claude workflow:
1. Read api-spec.pdf with x-pdf-reader
   → Extract 12 endpoints
   → Understand request/response formats
   → Note authentication requirements

2. Generate TypeScript types from spec

3. Use x-test-generator to create test suite
   → 36 tests covering all endpoints and edge cases

4. Implement each endpoint to pass tests (TDD)

5. Use x-code-reviewer to validate against spec
   → All requirements met ✓
   → Security best practices followed ✓

6. /x-docs to generate API documentation

7. /x-commit to commit implementation + tests + docs
```

### Scenario 2: Data Processing Pipeline

**Context:** Process customer data from Excel, transform, and generate reports

**Skills Used:** x-xlsx-reader, x-test-generator

```
User: "Read customers.xlsx, clean the data, and generate a TypeScript module to process it."

Claude workflow:
1. Use x-xlsx-reader to read customers.xlsx
   → 1,247 customer records
   → Identify data quality issues:
     - 23 duplicate emails
     - 15 invalid phone numbers
     - 8 missing required fields

2. Generate data cleaning utilities
   → Email deduplication
   → Phone number validation
   → Required field validation

3. Use x-test-generator for cleaning utilities
   → Tests for each validation rule
   → Edge cases for data issues found

4. Create TypeScript types from Excel schema

5. Generate data processing module
   → Read from Excel
   → Apply cleaning rules
   → Export cleaned data

6. /x-test to ensure comprehensive coverage

7. /x-commit
```

### Scenario 3: Legacy Code Modernization

**Context:** Modernize old codebase using new standards

**Skills Used:** x-pdf-reader (standards doc), x-code-reviewer

```
User: "Review my legacy authentication code against modern security standards in security-2024.pdf"

Claude workflow:
1. Read security-2024.pdf with x-pdf-reader
   → Extract modern security requirements:
     - Argon2id for password hashing
     - MFA support
     - OAuth 2.0 / OIDC
     - JWT with short expiration
     - Refresh token rotation

2. Use x-code-reviewer on legacy code
   → Compare against modern standards
   → Identify gaps:
     ❌ Using MD5 for passwords
     ❌ No MFA support
     ❌ Custom auth (not OAuth)
     ❌ Long-lived session tokens
     ❌ No refresh token mechanism

3. Generate modernization plan
   → Priority 1: Replace MD5 with Argon2id
   → Priority 2: Implement refresh tokens
   → Priority 3: Add MFA support
   → Priority 4: Migrate to OAuth

4. Implement each improvement

5. Use x-test-generator to ensure security

6. /x-commit for each improvement
```

## Tips for Combining Skills

### 1. Let Claude Choose Skills Automatically

**Good:**
```
Read the spec from spec.pdf and generate tests based on it
```

Claude automatically invokes x-pdf-reader and x-test-generator.

**Unnecessary:**
```
Use the PDF reader skill to read spec.pdf, then use the test generator skill to create tests
```

Trust Claude to invoke skills appropriately.

### 2. Provide Context

**Good:**
```
Read customer data from customers.xlsx and review my import script for data validation issues
```

Clear intent helps Claude combine skills effectively.

**Bad:**
```
Read customers.xlsx
```

Unclear what to do with the data after reading.

### 3. Chain Naturally

**Good:**
```
1. Read test cases from test-plan.pdf
2. Generate tests from those cases
3. Review my implementation against the tests
```

Natural progression of tasks.

### 4. Leverage Multiple Data Sources

**Good:**
```
Compare my database schema against:
- Technical spec in spec.pdf
- Example data in sample-data.xlsx
```

Skills work together to provide comprehensive analysis.

## Common Combinations Reference

| Skill 1 | Skill 2 | Use Case |
|---------|---------|----------|
| x-pdf-reader | x-test-generator | Generate tests from test case docs |
| x-pdf-reader | x-code-reviewer | Validate code against spec |
| x-xlsx-reader | x-test-generator | Create parameterized tests from data |
| x-xlsx-reader | x-code-reviewer | Audit code against checklist |
| x-pdf-reader | x-xlsx-reader | Cross-reference multiple specs |
| x-code-reviewer | x-test-generator | Review code, generate missing tests |

## See Also

- [Skills Guide](../skills/) - Individual skill documentation
- [Commands Guide](../commands/) - Command documentation
- [Command Chaining](./command-chaining.md) - Chaining commands together
- [Workflow Examples](../../) - Complete workflow examples
