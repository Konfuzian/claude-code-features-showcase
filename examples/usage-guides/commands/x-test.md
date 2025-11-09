# Using /x-test

## What It Does

Generates comprehensive test suites including:
- Unit tests for individual functions
- Integration tests for component interactions
- Edge case coverage
- Mock data and fixtures
- Test descriptions and assertions

## When to Use

- After implementing new features
- When test coverage is low
- To add missing edge case tests
- When refactoring code (regression tests)

## Basic Usage

### Generate Tests for Current File

```
/x-test
```

Claude will analyze the open file and generate appropriate tests.

### Generate Tests for Specific Code

```
Can you generate tests for the calculateDiscount function in src/pricing.js?
```

### Generate Tests with Specific Focus

```
Please generate edge case tests for the date parsing logic, including invalid dates and timezone handling
```

## Example

### Input Code (pricing.js)

```javascript
export function calculateDiscount(price, discountPercent, userTier) {
  if (price <= 0) throw new Error('Price must be positive');
  if (discountPercent < 0 || discountPercent > 100) {
    throw new Error('Discount must be between 0 and 100');
  }

  let finalDiscount = discountPercent;

  // Premium users get additional 10% off
  if (userTier === 'premium') {
    finalDiscount += 10;
  }

  const discountAmount = (price * Math.min(finalDiscount, 100)) / 100;
  return price - discountAmount;
}
```

### Generated Tests (pricing.test.js)

```javascript
import { describe, it, expect } from 'vitest';
import { calculateDiscount } from './pricing';

describe('calculateDiscount', () => {
  describe('happy path', () => {
    it('applies standard discount correctly', () => {
      const result = calculateDiscount(100, 20, 'standard');
      expect(result).toBe(80);
    });

    it('applies premium user bonus discount', () => {
      const result = calculateDiscount(100, 20, 'premium');
      expect(result).toBe(70); // 20% + 10% bonus
    });

    it('caps total discount at 100%', () => {
      const result = calculateDiscount(100, 95, 'premium');
      expect(result).toBe(0); // 95% + 10% = 105%, capped at 100%
    });
  });

  describe('edge cases', () => {
    it('handles 0% discount', () => {
      const result = calculateDiscount(100, 0, 'standard');
      expect(result).toBe(100);
    });

    it('handles 100% discount', () => {
      const result = calculateDiscount(100, 100, 'standard');
      expect(result).toBe(0);
    });

    it('handles very small prices', () => {
      const result = calculateDiscount(0.01, 50, 'standard');
      expect(result).toBe(0.005);
    });

    it('handles floating point precision', () => {
      const result = calculateDiscount(10.99, 15, 'standard');
      expect(result).toBeCloseTo(9.3415, 2);
    });
  });

  describe('validation', () => {
    it('throws error for negative price', () => {
      expect(() => calculateDiscount(-10, 20, 'standard'))
        .toThrow('Price must be positive');
    });

    it('throws error for zero price', () => {
      expect(() => calculateDiscount(0, 20, 'standard'))
        .toThrow('Price must be positive');
    });

    it('throws error for negative discount', () => {
      expect(() => calculateDiscount(100, -5, 'standard'))
        .toThrow('Discount must be between 0 and 100');
    });

    it('throws error for discount over 100%', () => {
      expect(() => calculateDiscount(100, 150, 'standard'))
        .toThrow('Discount must be between 0 and 100');
    });
  });

  describe('user tiers', () => {
    it('handles unknown user tier as standard', () => {
      const result = calculateDiscount(100, 20, 'unknown');
      expect(result).toBe(80);
    });

    it('handles null user tier', () => {
      const result = calculateDiscount(100, 20, null);
      expect(result).toBe(80);
    });
  });
});
```

## Test Frameworks Supported

The command adapts to your project's testing framework:

- **JavaScript/TypeScript**: Jest, Vitest, Mocha
- **Python**: Pytest, unittest
- **Go**: testing package
- **Ruby**: RSpec
- **Java**: JUnit

## Tips

1. **Run Tests After Generation**: Verify all tests pass
2. **Review Generated Tests**: Understand what's being tested
3. **Add Custom Cases**: Supplement with domain-specific tests
4. **Update as Code Changes**: Re-generate after refactoring

## Integration with Workflow

```
# Test-driven workflow
1. Implement feature
2. /x-test                 # Generate comprehensive tests
3. npm test                # Run tests, verify they pass
4. /x-test-coverage        # Check coverage gaps
5. Add missing tests if needed
6. /x-commit               # Commit feature + tests together
```

## Related Commands

- [/x-test-coverage](./x-test-coverage.md) - Analyze test coverage
- [/x-analyze](./x-analyze.md) - Check code quality before testing
- [/x-refactor](./x-refactor.md) - Refactor with test safety
