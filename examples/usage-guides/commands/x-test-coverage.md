# Using /x-test-coverage

## What It Does

Performs comprehensive test coverage analysis across the testing pyramid:
- **Unit tests**: Individual function/method coverage
- **Integration tests**: Component interaction coverage
- **End-to-end tests**: User workflow coverage
- **Edge cases**: Boundary condition coverage
- **Error paths**: Exception handling coverage

## When to Use

- Before releasing features
- After major refactoring
- During code reviews
- To identify untested code paths
- When improving overall test quality

## Basic Usage

### Analyze Current Project

```
/x-test-coverage
```

This launches the test-coverage-auditor agent to analyze your entire test suite.

### Analyze Specific Module

```
Can you analyze test coverage for the authentication module?
```

### Focus on Coverage Gaps

```
What are the critical untested paths in our payment processing code?
```

## Example Output

```
🧪 Test Coverage Analysis

=== Unit Test Coverage ===

src/auth/login.js:
  ✅ authenticateUser - 95% coverage
  ⚠️  refreshToken - 60% coverage
     Missing: Token expiry edge cases, invalid signature handling
  ❌ revokeSession - 0% coverage
     No tests found

src/payment/process.js:
  ✅ calculateTotal - 100% coverage
  ⚠️  processPayment - 45% coverage
     Missing: Network timeout, declined payment, partial refund
  ⚠️  validateCard - 70% coverage
     Missing: Expired card, invalid CVV

=== Integration Test Coverage ===

Authentication Flow:
  ✅ Login → Dashboard (tested)
  ✅ Login → Logout (tested)
  ⚠️  Login → Password Change → Re-login (not tested)
  ❌ Login Failure → Rate Limiting (not tested)

Payment Flow:
  ✅ Add to Cart → Checkout → Success (tested)
  ⚠️  Add to Cart → Checkout → Payment Failure → Retry (partial)
  ❌ Multiple Items → Apply Coupon → Checkout (not tested)

=== E2E Test Coverage ===

Critical User Journeys:
  ✅ New User Signup → Profile Setup → First Purchase
  ⚠️  Returning User → Add to Cart → Complete Purchase
     Missing: Saved payment methods, address selection
  ❌ User → Subscription → Cancel → Refund
     No E2E test exists

=== Recommendations ===

HIGH PRIORITY:
1. Add unit tests for revokeSession (0% coverage, security-critical)
2. Test payment failure scenarios (network errors, declined cards)
3. Add E2E test for subscription cancellation flow

MEDIUM PRIORITY:
4. Test authentication rate limiting
5. Add integration tests for password change flow
6. Test coupon application with multiple items

LOW PRIORITY:
7. Add edge cases for refreshToken expiry
8. Test saved payment method selection
9. Add tests for partial refund scenarios

=== Coverage Metrics ===

Unit Test Coverage:      78% (target: 80%+)
Integration Coverage:    65% (target: 70%+)
E2E Coverage:           55% (target: 60%+)
Critical Path Coverage: 82% (target: 95%+)

Overall Assessment: ⚠️ NEEDS IMPROVEMENT
```

## Understanding the Report

### Coverage Levels

- ✅ **Good (80%+)**: Well-tested, low risk
- ⚠️ **Fair (50-79%)**: Partially tested, medium risk
- ❌ **Poor (<50%)**: Inadequately tested, high risk

### Test Pyramid Balance

```
    /\
   /E2E\      <- Few, slow, high-level
  /------\
 /Integr.\   <- Medium number, medium speed
/----------\
/   Unit   \  <- Many, fast, low-level
/------------\
```

A healthy test suite has:
- **70%** unit tests (fast, isolated)
- **20%** integration tests (component interaction)
- **10%** E2E tests (full user workflows)

### Critical Paths

Code that handles:
- Authentication and authorization
- Payment processing
- Data persistence
- Security boundaries
- Business-critical workflows

Should have **95%+ coverage** including edge cases.

## Taking Action

### After Running Coverage Analysis

1. **Fix Critical Gaps First**
   ```
   /x-test
   Please add tests for revokeSession including error cases
   ```

2. **Run Tests to Verify**
   ```
   npm test
   ```

3. **Re-analyze to Confirm**
   ```
   /x-test-coverage
   ```

4. **Commit Improvements**
   ```
   /x-commit
   ```

## Integration with Workflow

```
# Coverage improvement workflow
1. /x-test-coverage        # Analyze current state
2. Identify high-priority gaps
3. /x-test                 # Generate missing tests
4. npm test                # Verify tests pass
5. /x-test-coverage        # Verify improvement
6. /x-commit               # Commit new tests
```

## Tips

1. **Start with Critical Paths**: Authentication, payments, data integrity
2. **Don't Chase 100%**: Diminishing returns after 80-90%
3. **Test Behavior, Not Implementation**: Focus on what matters
4. **Include Negative Tests**: Error cases and edge conditions
5. **Balance the Pyramid**: More unit tests, fewer E2E tests

## Common Coverage Gaps

### Missing Error Handling
```javascript
// Code
async function fetchUser(id) {
  const response = await api.get(`/users/${id}`);
  return response.data;
}

// Missing tests for:
// - Network timeout
// - 404 Not Found
// - 500 Server Error
// - Invalid response format
```

### Missing Edge Cases
```javascript
// Code
function divide(a, b) {
  return a / b;
}

// Missing tests for:
// - Division by zero
// - Negative numbers
// - Very large numbers
// - Floating point precision
```

### Missing Integration Scenarios
```javascript
// Tested individually but not together:
// - User creates account ✓
// - User verifies email ✓
// - User logs in ✓

// Missing:
// - User creates account → receives email → verifies → logs in
```

## Related Commands

- [/x-test](./x-test.md) - Generate tests for gaps
- [/x-analyze](./x-analyze.md) - Find code quality issues
- [/x-refactor](./x-refactor.md) - Simplify code for easier testing
