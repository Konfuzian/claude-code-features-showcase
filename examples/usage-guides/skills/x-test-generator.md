# Using x-test-generator Skill

## What It Does

Generates comprehensive test suites including:
- **Unit tests**: Individual function/method tests
- **Integration tests**: Component interaction tests
- **Edge cases**: Boundary conditions and unusual inputs
- **Mock data**: Realistic test fixtures
- **Error scenarios**: Exception and error handling tests

Adapts to project testing frameworks: Jest, Vitest, Pytest, JUnit, RSpec, Go testing, etc.

## When to Use

- Creating tests for new functionality
- Improving test coverage
- Generating test fixtures
- Adding missing edge case tests
- Following test-driven development (TDD)

## How to Invoke

Skills are invoked automatically by Claude based on context. Ask for test generation:

```
Generate tests for this authentication function
```

```
Create comprehensive test cases including edge cases
```

```
I need integration tests for the checkout flow
```

## Example 1: Unit Test Generation

### Request
```
Generate tests for this password validation function:

function validatePassword(password) {
  if (password.length < 8) return false;
  if (!/[A-Z]/.test(password)) return false;
  if (!/[a-z]/.test(password)) return false;
  if (!/[0-9]/.test(password)) return false;
  if (!/[!@#$%^&*]/.test(password)) return false;
  return true;
}
```

### Generated Tests
```javascript
import { describe, it, expect } from 'vitest';
import { validatePassword } from './password';

describe('validatePassword', () => {
  describe('valid passwords', () => {
    it('accepts password with all requirements', () => {
      expect(validatePassword('Abc123!@#')).toBe(true);
    });

    it('accepts password exactly 8 characters', () => {
      expect(validatePassword('Abcd123!')).toBe(true);
    });

    it('accepts password with multiple special characters', () => {
      expect(validatePassword('Abc123!@#$%')).toBe(true);
    });

    it('accepts very long password', () => {
      expect(validatePassword('Abcd123!'.repeat(10))).toBe(true);
    });
  });

  describe('invalid passwords - length', () => {
    it('rejects password with 7 characters', () => {
      expect(validatePassword('Abc123!')).toBe(false);
    });

    it('rejects empty password', () => {
      expect(validatePassword('')).toBe(false);
    });

    it('rejects very short password', () => {
      expect(validatePassword('Ab1!')).toBe(false);
    });
  });

  describe('invalid passwords - missing uppercase', () => {
    it('rejects password without uppercase letter', () => {
      expect(validatePassword('abc123!@#')).toBe(false);
    });

    it('rejects password with numbers and special chars but no uppercase', () => {
      expect(validatePassword('abcdefg123!')).toBe(false);
    });
  });

  describe('invalid passwords - missing lowercase', () => {
    it('rejects password without lowercase letter', () => {
      expect(validatePassword('ABC123!@#')).toBe(false);
    });
  });

  describe('invalid passwords - missing number', () => {
    it('rejects password without number', () => {
      expect(validatePassword('Abcdefg!@#')).toBe(false);
    });
  });

  describe('invalid passwords - missing special character', () => {
    it('rejects password without special character', () => {
      expect(validatePassword('Abcd12345')).toBe(false);
    });

    it('rejects password with space instead of special char', () => {
      expect(validatePassword('Abcd123 ')).toBe(false);
    });

    it('rejects password with period (not in special chars list)', () => {
      expect(validatePassword('Abcd123.')).toBe(false);
    });
  });

  describe('edge cases', () => {
    it('rejects null password', () => {
      expect(() => validatePassword(null)).toThrow();
    });

    it('rejects undefined password', () => {
      expect(() => validatePassword(undefined)).toThrow();
    });

    it('rejects non-string password', () => {
      expect(() => validatePassword(12345678)).toThrow();
    });

    it('handles unicode characters', () => {
      expect(validatePassword('Abc123!café')).toBe(true);
    });

    it('handles emoji in password', () => {
      // Emojis don't satisfy requirements
      expect(validatePassword('Abc123😀')).toBe(false);
    });
  });

  describe('security edge cases', () => {
    it('rejects password that is only minimum length', () => {
      expect(validatePassword('Abc123!')).toBe(false); // Only 7 chars
    });

    it('accepts common password pattern if it meets requirements', () => {
      // Note: This function doesn't check against common passwords
      expect(validatePassword('Password123!')).toBe(true);
    });

    it('accepts password with SQL injection attempt', () => {
      // Note: This function doesn't sanitize, just validates format
      expect(validatePassword("Abc123!'; DROP TABLE users--")).toBe(true);
    });
  });
});
```

## Example 2: Integration Test Generation

### Request
```
Create integration tests for this shopping cart flow:

class ShoppingCart {
  constructor(db, paymentGateway) {
    this.db = db;
    this.paymentGateway = paymentGateway;
    this.items = [];
  }

  async addItem(productId, quantity) {
    const product = await this.db.getProduct(productId);
    this.items.push({ product, quantity });
  }

  async checkout(userId, paymentMethod) {
    const total = this.calculateTotal();
    const payment = await this.paymentGateway.charge(paymentMethod, total);
    const order = await this.db.createOrder(userId, this.items, payment.id);
    this.items = [];
    return order;
  }

  calculateTotal() {
    return this.items.reduce((sum, item) =>
      sum + (item.product.price * item.quantity), 0
    );
  }
}
```

### Generated Tests
```javascript
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { ShoppingCart } from './ShoppingCart';

describe('ShoppingCart Integration Tests', () => {
  let cart;
  let mockDb;
  let mockPaymentGateway;

  beforeEach(() => {
    // Mock database
    mockDb = {
      getProduct: vi.fn(),
      createOrder: vi.fn(),
    };

    // Mock payment gateway
    mockPaymentGateway = {
      charge: vi.fn(),
    };

    cart = new ShoppingCart(mockDb, mockPaymentGateway);
  });

  describe('adding items', () => {
    it('successfully adds item to cart', async () => {
      const product = { id: 1, name: 'Widget', price: 19.99 };
      mockDb.getProduct.mockResolvedValue(product);

      await cart.addItem(1, 2);

      expect(mockDb.getProduct).toHaveBeenCalledWith(1);
      expect(cart.items).toHaveLength(1);
      expect(cart.items[0]).toEqual({ product, quantity: 2 });
    });

    it('adds multiple different items', async () => {
      mockDb.getProduct
        .mockResolvedValueOnce({ id: 1, name: 'Widget', price: 19.99 })
        .mockResolvedValueOnce({ id: 2, name: 'Gadget', price: 29.99 });

      await cart.addItem(1, 1);
      await cart.addItem(2, 3);

      expect(cart.items).toHaveLength(2);
    });

    it('handles product not found error', async () => {
      mockDb.getProduct.mockRejectedValue(new Error('Product not found'));

      await expect(cart.addItem(999, 1))
        .rejects.toThrow('Product not found');
    });
  });

  describe('calculating total', () => {
    it('calculates total for single item', async () => {
      mockDb.getProduct.mockResolvedValue({ id: 1, price: 19.99 });
      await cart.addItem(1, 2);

      const total = cart.calculateTotal();

      expect(total).toBe(39.98);
    });

    it('calculates total for multiple items', async () => {
      mockDb.getProduct
        .mockResolvedValueOnce({ id: 1, price: 19.99 })
        .mockResolvedValueOnce({ id: 2, price: 29.99 });

      await cart.addItem(1, 2);  // 39.98
      await cart.addItem(2, 1);  // 29.99

      expect(cart.calculateTotal()).toBe(69.97);
    });

    it('returns 0 for empty cart', () => {
      expect(cart.calculateTotal()).toBe(0);
    });
  });

  describe('checkout flow', () => {
    it('completes successful checkout', async () => {
      const product = { id: 1, price: 19.99 };
      const paymentResult = { id: 'pay_123', status: 'success' };
      const orderResult = { id: 'order_456', status: 'confirmed' };

      mockDb.getProduct.mockResolvedValue(product);
      mockPaymentGateway.charge.mockResolvedValue(paymentResult);
      mockDb.createOrder.mockResolvedValue(orderResult);

      await cart.addItem(1, 2);
      const order = await cart.checkout('user_789', 'card_abc');

      expect(mockPaymentGateway.charge).toHaveBeenCalledWith('card_abc', 39.98);
      expect(mockDb.createOrder).toHaveBeenCalledWith(
        'user_789',
        expect.any(Array),
        'pay_123'
      );
      expect(order).toEqual(orderResult);
      expect(cart.items).toHaveLength(0); // Cart cleared
    });

    it('handles payment failure', async () => {
      mockDb.getProduct.mockResolvedValue({ id: 1, price: 19.99 });
      mockPaymentGateway.charge.mockRejectedValue(
        new Error('Payment declined')
      );

      await cart.addItem(1, 1);

      await expect(cart.checkout('user_123', 'card_bad'))
        .rejects.toThrow('Payment declined');

      // Verify order was not created
      expect(mockDb.createOrder).not.toHaveBeenCalled();
      // Cart should still have items
      expect(cart.items).toHaveLength(1);
    });

    it('handles database error during order creation', async () => {
      mockDb.getProduct.mockResolvedValue({ id: 1, price: 19.99 });
      mockPaymentGateway.charge.mockResolvedValue({ id: 'pay_123' });
      mockDb.createOrder.mockRejectedValue(new Error('Database error'));

      await cart.addItem(1, 1);

      await expect(cart.checkout('user_123', 'card_abc'))
        .rejects.toThrow('Database error');

      // Payment was charged but order failed
      // TODO: Add payment rollback logic
      expect(mockPaymentGateway.charge).toHaveBeenCalled();
    });

    it('handles checkout with empty cart', async () => {
      mockPaymentGateway.charge.mockResolvedValue({ id: 'pay_000' });
      mockDb.createOrder.mockResolvedValue({ id: 'order_000' });

      await cart.checkout('user_123', 'card_abc');

      expect(mockPaymentGateway.charge).toHaveBeenCalledWith('card_abc', 0);
    });
  });

  describe('complete user journeys', () => {
    it('handles full shopping experience', async () => {
      // Setup products
      mockDb.getProduct
        .mockResolvedValueOnce({ id: 1, name: 'Widget', price: 19.99 })
        .mockResolvedValueOnce({ id: 2, name: 'Gadget', price: 29.99 })
        .mockResolvedValueOnce({ id: 1, name: 'Widget', price: 19.99 });

      mockPaymentGateway.charge.mockResolvedValue({ id: 'pay_123' });
      mockDb.createOrder.mockResolvedValue({ id: 'order_456' });

      // User journey
      await cart.addItem(1, 2);        // Add 2 widgets
      await cart.addItem(2, 1);        // Add 1 gadget
      await cart.addItem(1, 1);        // Add 1 more widget

      expect(cart.items).toHaveLength(3);
      expect(cart.calculateTotal()).toBe(89.96); // (19.99*2) + 29.99 + 19.99

      const order = await cart.checkout('user_123', 'card_abc');

      expect(order.id).toBe('order_456');
      expect(cart.items).toHaveLength(0);
    });

    it('handles retry after payment failure', async () => {
      mockDb.getProduct.mockResolvedValue({ id: 1, price: 19.99 });

      mockPaymentGateway.charge
        .mockRejectedValueOnce(new Error('Payment declined'))
        .mockResolvedValueOnce({ id: 'pay_456' });

      mockDb.createOrder.mockResolvedValue({ id: 'order_789' });

      await cart.addItem(1, 1);

      // First attempt fails
      await expect(cart.checkout('user_123', 'card_bad'))
        .rejects.toThrow();

      // Items still in cart
      expect(cart.items).toHaveLength(1);

      // Retry with different payment method succeeds
      const order = await cart.checkout('user_123', 'card_good');

      expect(order.id).toBe('order_789');
      expect(cart.items).toHaveLength(0);
    });
  });
});
```

## Example 3: Mock Data Generation

### Request
```
Generate mock data for testing a user management system
```

### Generated Mocks
```javascript
// test/fixtures/users.js

export const mockUsers = {
  admin: {
    id: 1,
    username: 'admin',
    email: 'admin@example.com',
    role: 'admin',
    verified: true,
    createdAt: new Date('2024-01-01'),
  },

  regularUser: {
    id: 2,
    username: 'john_doe',
    email: 'john@example.com',
    role: 'user',
    verified: true,
    createdAt: new Date('2024-01-15'),
  },

  unverifiedUser: {
    id: 3,
    username: 'new_user',
    email: 'new@example.com',
    role: 'user',
    verified: false,
    createdAt: new Date('2024-02-01'),
  },

  suspendedUser: {
    id: 4,
    username: 'bad_actor',
    email: 'suspended@example.com',
    role: 'user',
    verified: true,
    suspended: true,
    suspendedAt: new Date('2024-02-10'),
    suspendReason: 'Terms of service violation',
  },
};

export const mockUserList = Object.values(mockUsers);

// Edge case users
export const edgeCaseUsers = {
  emptyProfile: {
    id: 5,
    username: 'minimal',
    email: 'minimal@example.com',
    role: 'user',
    verified: false,
    // No optional fields
  },

  unicodeUsername: {
    id: 6,
    username: 'user_用户_😀',
    email: 'unicode@example.com',
    role: 'user',
    verified: true,
  },

  longFields: {
    id: 7,
    username: 'a'.repeat(50),
    email: 'very.long.email.address.for.testing@subdomain.example.com',
    bio: 'Lorem ipsum '.repeat(100),
    role: 'user',
    verified: true,
  },
};

// Factory functions
export function createMockUser(overrides = {}) {
  return {
    id: Math.floor(Math.random() * 10000),
    username: `user_${Math.random().toString(36).slice(2, 9)}`,
    email: `${Math.random().toString(36).slice(2, 9)}@example.com`,
    role: 'user',
    verified: false,
    createdAt: new Date(),
    ...overrides,
  };
}

export function createMockUsers(count = 10, overrides = {}) {
  return Array.from({ length: count }, () => createMockUser(overrides));
}
```

## Supported Testing Frameworks

### JavaScript/TypeScript
- Jest
- Vitest
- Mocha + Chai
- Jasmine

### Python
- Pytest
- unittest
- nose2

### Go
- testing package
- testify

### Ruby
- RSpec
- Minitest

### Java
- JUnit 5
- TestNG

## Tips

1. **Provide Context**: Share the function signature and purpose
2. **Specify Framework**: Mention if you use a specific testing library
3. **Request Coverage**: Ask for edge cases explicitly
4. **Review Generated Tests**: Ensure they match your requirements
5. **Run Tests**: Verify generated tests actually pass

## Common Use Cases

### TDD Workflow
```
Write tests for a user registration function that should validate email, check for duplicates, and hash passwords
```

### Edge Case Coverage
```
Generate edge case tests for date parsing including timezones, invalid dates, and leap years
```

### Integration Tests
```
Create integration tests for the authentication flow including login, token refresh, and logout
```

### Mock Generation
```
Generate realistic mock data for testing an e-commerce system
```

## Integration with Workflows

### Test-First Development
```
1. /x-test (or invoke skill) - Generate test structure
2. Run tests (they should fail)
3. Implement functionality
4. Run tests (they should pass)
5. /x-refactor - Improve implementation
6. /x-commit - Commit code + tests
```

### Coverage Improvement
```
1. /x-test-coverage - Identify gaps
2. Invoke x-test-generator for missing tests
3. Run tests to verify
4. /x-test-coverage - Verify improvement
5. /x-commit - Commit new tests
```

## Related Skills & Commands

- [/x-test](../commands/x-test.md) - Command version of test generation
- [/x-test-coverage](../commands/x-test-coverage.md) - Analyze coverage
- [x-code-reviewer](./x-code-reviewer.md) - Review test quality
- [/x-refactor](../commands/x-refactor.md) - Refactor for testability
