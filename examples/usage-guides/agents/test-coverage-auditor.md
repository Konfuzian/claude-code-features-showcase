# test-coverage-auditor Agent

Comprehensive test coverage analysis agent invoked via `/x-test-coverage`.

## Usage
```
/x-test-coverage
```

## What It Does
Analyzes test coverage across:
- Unit tests
- Integration tests
- E2E tests
- Edge cases

## Example Output
```
Unit Coverage: 78%
Integration Coverage: 65%
E2E Coverage: 55%

Missing:
- auth/reset.js - 0% coverage
- api/payments.js - Token expiry tests
```

See [/x-test-coverage command](../commands/x-test-coverage.md) for details.
