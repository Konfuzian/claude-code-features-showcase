---
name: test-coverage-auditor
description: Analyzes test coverage comprehensively across unit, integration, and end-to-end tests. Identifies gaps in test coverage, suggests missing test scenarios, validates test quality, and ensures proper test pyramid distribution. Use when auditing test suites, improving coverage, or ensuring production readiness.
---

# Test Coverage Auditor Skill

Performs comprehensive analysis of test coverage to ensure production-quality testing.

## Primary Capabilities

### 1. Coverage Analysis
- Analyzes unit test coverage (functions, classes, modules)
- Evaluates integration test coverage (component interactions)
- Assesses end-to-end test coverage (user workflows)
- Identifies untested code paths
- Reports coverage statistics and gaps

### 2. Test Quality Assessment
- Validates test structure and organization
- Checks for proper assertions
- Identifies flaky or unreliable tests
- Ensures test independence
- Validates test naming conventions

### 3. Test Pyramid Validation
- Ensures proper test distribution (70% unit, 20% integration, 10% e2e)
- Identifies over-reliance on slow tests
- Suggests refactoring opportunities
- Validates test execution speed

### 4. Gap Identification
- Lists functions/classes without tests
- Identifies missing edge case coverage
- Finds missing error handling tests
- Detects missing security scenario tests
- Reports missing integration tests

## Analysis Process

1. **Discovery Phase**
   - Scan codebase for all source files
   - Identify all test files
   - Map tests to source code
   - Detect testing framework

2. **Coverage Phase**
   - Analyze unit test coverage
   - Evaluate integration test coverage
   - Assess e2e test coverage
   - Calculate coverage percentages
   - Identify coverage gaps

3. **Quality Phase**
   - Review test structure
   - Check assertion quality
   - Validate test independence
   - Assess test maintainability
   - Check for test smells

4. **Reporting Phase**
   - Generate coverage report
   - List missing tests by priority
   - Provide specific recommendations
   - Suggest test implementations
   - Estimate effort required

## Test Categories

### Unit Tests
**Purpose**: Test individual functions/classes in isolation

**What to Check**:
- Every public function has tests
- Happy path covered
- Edge cases covered (empty input, null, max values)
- Error conditions tested
- Type validation tested
- Business logic validated

**Example Gaps**:
- Function without any tests
- Missing edge case (empty list)
- Missing error handling test
- Missing type validation

### Integration Tests
**Purpose**: Test component interactions and data flow

**What to Check**:
- Module integration tested
- API endpoints tested
- Database interactions tested
- External service mocks tested
- Data transformation validated
- Error propagation tested

**Example Gaps**:
- API endpoint without integration test
- Database query not tested
- Error propagation not validated
- Component interaction missing

### End-to-End Tests
**Purpose**: Test complete user workflows

**What to Check**:
- Critical user flows covered
- Authentication flows tested
- Data persistence validated
- UI interactions tested (if applicable)
- Error scenarios tested

**Example Gaps**:
- No e2e tests for critical workflow
- Authentication not tested end-to-end
- Data persistence not validated

## Coverage Metrics

### Line Coverage
- Percentage of code lines executed by tests
- Target: 80%+ for production code

### Branch Coverage
- Percentage of conditional branches tested
- Target: 75%+ for production code

### Function Coverage
- Percentage of functions with tests
- Target: 95%+ for public functions

### Integration Coverage
- Percentage of component interactions tested
- Target: 80%+ for critical paths

## Test Quality Criteria

### Good Tests
- ✅ Test one thing at a time
- ✅ Have descriptive names
- ✅ Are independent (no shared state)
- ✅ Are fast (unit tests < 1ms)
- ✅ Have clear arrange/act/assert structure
- ✅ Use appropriate mocks/fixtures
- ✅ Test behavior, not implementation

### Test Smells (Bad Patterns)
- ❌ Tests that depend on execution order
- ❌ Tests without assertions
- ❌ Tests that test multiple things
- ❌ Slow unit tests (> 100ms)
- ❌ Tests with hardcoded dates/times
- ❌ Tests with sleep/wait calls
- ❌ Tests that require manual setup

## Report Format

### Coverage Summary
```
Total Coverage: 76% (Target: 80%)
├─ Unit Tests: 85% (Good)
├─ Integration Tests: 65% (Needs Improvement)
└─ End-to-End Tests: 45% (Critical Gap)

Test Distribution:
├─ Unit: 120 tests (65%)
├─ Integration: 50 tests (27%)
└─ E2E: 15 tests (8%)

Target Distribution:
├─ Unit: 70%
├─ Integration: 20%
└─ E2E: 10%
```

### Critical Gaps (High Priority)
List of untested critical functions with specific test recommendations

### Medium Priority Gaps
List of partially tested functions needing edge case coverage

### Low Priority Gaps
List of helper functions or utilities with missing tests

### Test Quality Issues
List of test smells and refactoring suggestions

## Usage Examples

### Example 1: Audit Entire Codebase
```
Analyze test coverage for the entire codebase.
Report gaps in unit, integration, and e2e tests.
Prioritize by criticality.
```

### Example 2: Audit Specific Module
```
Analyze test coverage for the PDF reader package.
List all missing tests with specific recommendations.
```

### Example 3: Pre-Release Audit
```
Perform comprehensive test coverage audit before release.
Identify any critical gaps blocking production deployment.
Validate test pyramid distribution.
```

### Example 4: Security Testing Audit
```
Audit test coverage for security scenarios:
- Path traversal tests
- Input validation tests
- Authentication tests
- Authorization tests
```

## Integration with Workflows

### Before Release
Run comprehensive audit to ensure production readiness

### After Major Feature
Validate that new feature has adequate test coverage

### During Code Review
Check that PR includes appropriate tests

### Regular Audits
Weekly/monthly coverage reviews to maintain quality

## Supported Testing Frameworks

Automatically detects and works with:
- **Python**: pytest, unittest
- **JavaScript/TypeScript**: Jest, Mocha, Vitest
- **Java**: JUnit, TestNG
- **Go**: testing package
- **Ruby**: RSpec, Minitest

## Output Deliverables

1. **Coverage Report**
   - Overall coverage percentage
   - Coverage by category (unit/integration/e2e)
   - Test distribution analysis
   - Coverage trends

2. **Gap Analysis**
   - Prioritized list of missing tests
   - Specific recommendations for each gap
   - Code examples for suggested tests
   - Effort estimates

3. **Test Quality Report**
   - Test smells identified
   - Refactoring suggestions
   - Performance issues
   - Maintainability concerns

4. **Action Plan**
   - Prioritized list of improvements
   - Estimated effort for each item
   - Suggested implementation order
   - Timeline recommendations

## Best Practices Enforced

- Test pyramid adherence (70/20/10 split)
- Proper test isolation and independence
- Fast unit tests (< 100ms each)
- Descriptive test names (test_should_do_something_when_condition)
- Arrange/Act/Assert structure
- Minimal use of mocks (only for external dependencies)
- Tests as documentation (clear intent)

## Priority Levels

### CRITICAL (Must Fix)
- Functions in critical path without tests
- Security-related code without tests
- Error handling without tests
- No integration tests for key workflows

### HIGH (Should Fix Soon)
- Public API functions without tests
- Missing edge case coverage
- No e2e tests for main user flows
- Test pyramid imbalance

### MEDIUM (Plan to Fix)
- Helper functions without tests
- Partial coverage with gaps
- Missing integration tests
- Test quality issues

### LOW (Nice to Have)
- Internal utilities without tests
- Redundant test coverage
- Test refactoring opportunities
