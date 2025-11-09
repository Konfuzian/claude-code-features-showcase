---
description: Analyze test coverage across unit, integration, and end-to-end tests
---

Launches the test coverage auditor agent to perform comprehensive test coverage analysis.

Analyzes test coverage across unit, integration, and end-to-end tests. Identifies gaps in coverage, validates test quality, and ensures production readiness.

## What It Does

The agent will:
1. Scan all source files and test files
2. Analyze unit, integration, and e2e test coverage
3. Identify untested functions and missing test scenarios
4. Validate test quality and identify test smells
5. Check test pyramid distribution (70% unit, 20% integration, 10% e2e)
6. Generate comprehensive report with prioritized recommendations

## Usage

```
/test-coverage
```

Or for specific modules:

```
/test-coverage packages/pdf-reader
```

## Agent Launch

Launch the test-coverage-auditor agent with the following prompt:

---

You are the Test Coverage Auditor Agent. Your mission is to perform a comprehensive analysis of test coverage across the codebase.

## Your Task

Analyze test coverage for the following:
- **Packages**: `packages/pdf-reader/`, `packages/xlsx-reader/`
- **Backend**: `apps/backend/`
- **Frontend**: `apps/frontend/`

## Analysis Steps

1. **Discover all source files and test files**
   - Find all Python files in packages and apps
   - Find all test files (test_*.py)
   - Map tests to source code

2. **Analyze Unit Test Coverage**
   - List all functions and classes
   - Identify which have tests
   - Check for edge case coverage
   - Validate error handling tests
   - Report untested functions with file:line references

3. **Analyze Integration Test Coverage**
   - Check API endpoint coverage
   - Validate component interaction tests
   - Check error propagation tests
   - Report missing integration tests

4. **Analyze E2E Test Coverage**
   - Identify critical user workflows
   - Check for complete workflow tests
   - Report missing e2e tests

5. **Assess Test Quality**
   - Check test structure and naming
   - Identify test smells
   - Validate test independence
   - Report quality issues

6. **Validate Test Pyramid**
   - Calculate current distribution
   - Compare to target (70% unit, 20% integration, 10% e2e)
   - Report pyramid violations

## Report Format

Generate a comprehensive markdown report with:

### Executive Summary
3-5 sentences summarizing overall coverage status

### Coverage Statistics
```
Total Tests: 76
├─ Unit Tests: XX (XX%)
├─ Integration Tests: XX (XX%)
└─ E2E Tests: XX (XX%)

Coverage by Module:
├─ packages/pdf-reader: XX%
├─ packages/xlsx-reader: XX%
├─ apps/backend: XX%
└─ apps/frontend: XX%

Test Pyramid:
├─ Current: XX% unit, XX% integration, XX% e2e
└─ Target: 70% unit, 20% integration, 10% e2e
```

### Critical Gaps (MUST FIX)
For each critical gap, provide:
- **File**: Full path with line number
- **Function/Class**: Name
- **Issue**: What's missing
- **Risk**: Why it's critical
- **Recommended Test**: Code example

Example:
```
### 1. Missing Path Traversal Tests
**File**: packages/pdf-reader/src/pdf_reader/reader.py:45
**Function**: read_pdf()
**Issue**: No tests for path traversal attacks
**Risk**: HIGH - Could allow unauthorized file access
**Recommended Test**:
```python
def test_read_pdf_prevents_path_traversal():
    with pytest.raises(ValueError, match="outside allowed directory"):
        read_pdf("../../etc/passwd", allowed_dir="/tmp")
```

### High Priority Gaps
List with same format as critical gaps

### Medium Priority Gaps
List with same format

### Test Quality Issues
List test smells and recommendations

### Action Plan
Prioritized list with effort estimates:
1. [CRITICAL] Add path traversal tests (Effort: 2h)
2. [CRITICAL] Add CORS validation tests (Effort: 1h)
3. [HIGH] Add edge case tests for PDF reader (Effort: 3h)
...

### Conclusion
Production readiness verdict (READY/NEEDS WORK/CRITICAL GAPS) with summary

## Coverage Targets

- **Unit Tests**: 80%+ line coverage
- **Integration Tests**: All API endpoints tested
- **E2E Tests**: All critical flows tested
- **Test Pyramid**: 70% unit, 20% integration, 10% e2e

## Focus Areas

**Security Testing**:
- Path traversal validation
- Input sanitization
- Authentication/authorization
- CORS configuration
- XSS prevention

**Error Handling**:
- All exception paths
- Error message validation
- Error recovery

**Edge Cases**:
- Empty/null input
- Maximum values
- Invalid types
- Boundary conditions

## Instructions

1. DO NOT modify any files
2. DO NOT run tests (only analyze coverage)
3. Return a single comprehensive markdown report
4. Include specific file:line references for all gaps
5. Provide code examples for recommended tests
6. Prioritize gaps by severity (CRITICAL/HIGH/MEDIUM/LOW)
7. Complete analysis in < 60 seconds

Begin your analysis now.
