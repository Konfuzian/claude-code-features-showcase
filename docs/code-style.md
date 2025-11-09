# Code Style & Guidelines

## Philosophy

- **Clarity over cleverness** - Write code that's easy to understand
- **Consistency over personal preference** - Follow project patterns
- **Simple over complex** - Solve problems in straightforward ways

## Language-Specific

### Python

**Formatting:** Use `ruff` (auto-formatted by hooks)

**Style:**
```python
# Good - clear and simple
def calculate_total(items: list[dict]) -> float:
    return sum(item['price'] * item['quantity'] for item in items)

# Bad - overly clever
def calculate_total(items):
    return reduce(lambda a,b:a+b['price']*b['quantity'],items,0)
```

**Naming:**
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

### JavaScript/TypeScript

**Formatting:** Use `prettier` (auto-formatted by hooks)

**Style:**
```javascript
// Good - explicit and safe
function processUser(user) {
  if (!user?.email) return null;
  return user.email.toLowerCase();
}

// Bad - assumes structure
function processUser(user) {
  return user.email.toLowerCase();
}
```

**Naming:**
- Functions/variables: `camelCase`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

## General Principles

### Early Returns

```javascript
// Good
function validate(data) {
  if (!data) return false;
  if (!data.email) return false;
  if (!data.name) return false;
  return true;
}

// Bad
function validate(data) {
  if (data) {
    if (data.email) {
      if (data.name) {
        return true;
      }
    }
  }
  return false;
}
```

### Extract Functions

```javascript
// Good
function processOrder(order) {
  if (!isValidOrder(order)) return;
  const total = calculateTotal(order.items);
  return createInvoice(order, total);
}

// Bad
function processOrder(order) {
  if (!order || !order.items || order.items.length === 0) return;
  let total = 0;
  for (let i = 0; i < order.items.length; i++) {
    total += order.items[i].price * order.items[i].quantity;
  }
  return { orderId: order.id, total: total, date: new Date() };
}
```

### Descriptive Names

```python
# Good
def send_welcome_email(user_email: str) -> bool:
    pass

# Bad
def swe(e: str) -> bool:
    pass
```

### Comments

```javascript
// Good - explain WHY
// Using exponential backoff to avoid overwhelming the API during outages
const delay = Math.pow(2, retryCount) * 1000;

// Bad - explain WHAT (code already shows this)
// Multiply 2 to the power of retryCount and multiply by 1000
const delay = Math.pow(2, retryCount) * 1000;
```

## Error Handling

### Python

```python
# Good - specific exceptions
try:
    user = get_user(user_id)
except UserNotFoundError:
    return None
except DatabaseError as e:
    logger.error(f"Database error: {e}")
    raise

# Bad - catch all
try:
    user = get_user(user_id)
except:
    return None
```

### JavaScript

```javascript
// Good - specific handling
async function fetchUser(id) {
  try {
    const response = await api.get(`/users/${id}`);
    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      return null;
    }
    throw error;
  }
}

// Bad - swallow all errors
async function fetchUser(id) {
  try {
    return (await api.get(`/users/${id}`)).data;
  } catch (error) {
    return null;
  }
}
```

## Testing

### Test Organization

```javascript
describe('UserService', () => {
  describe('createUser', () => {
    it('creates user with valid data', () => {
      // arrange
      const userData = { name: 'Alice', email: 'alice@example.com' };

      // act
      const user = userService.createUser(userData);

      // assert
      expect(user.name).toBe('Alice');
    });

    it('throws error for invalid email', () => {
      expect(() => userService.createUser({ email: 'invalid' }))
        .toThrow('Invalid email');
    });
  });
});
```

### Test Names

```python
# Good - describes behavior
def test_user_creation_fails_with_duplicate_email():
    pass

# Bad - vague
def test_user():
    pass
```

## Security

### Input Validation

```python
# Good - validate and sanitize
def get_user(user_id: int) -> User:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("Invalid user ID")
    return db.query("SELECT * FROM users WHERE id = ?", [user_id])

# Bad - trust input
def get_user(user_id):
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

### Secrets

```javascript
// Good - use environment variables
const apiKey = process.env.API_KEY;

// Bad - hardcode
const apiKey = 'sk-1234567890abcdef';
```

## Documentation

### Functions

```python
# Good
def calculate_discount(price: float, percent: float) -> float:
    """Calculate discounted price.

    Args:
        price: Original price (must be positive)
        percent: Discount percentage (0-100)

    Returns:
        Discounted price

    Raises:
        ValueError: If price is negative or percent out of range
    """
    if price < 0:
        raise ValueError("Price must be positive")
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be 0-100")
    return price * (1 - percent / 100)
```

### TODOs

```javascript
// Good - with issue reference
// TODO(#123): Add rate limiting to prevent abuse

// Bad - vague and no tracking
// TODO: fix this later
```

## File Organization

### Project Structure

```
src/
  ├── api/          # API routes
  ├── services/     # Business logic
  ├── models/       # Data models
  ├── utils/        # Shared utilities
  └── tests/        # Tests mirror src structure
```

### Import Order

```python
# 1. Standard library
import os
from datetime import datetime

# 2. Third-party
import requests
from fastapi import FastAPI

# 3. Local
from .models import User
from .services import UserService
```

## Common Patterns

### Configuration

```python
# Good - centralized config
from config import settings

DATABASE_URL = settings.database_url
API_KEY = settings.api_key

# Bad - scattered magic values
DATABASE_URL = "postgresql://localhost/db"
```

### Dependency Injection

```python
# Good
class UserService:
    def __init__(self, db: Database, email_service: EmailService):
        self.db = db
        self.email_service = email_service

# Bad - hard dependencies
class UserService:
    def __init__(self):
        self.db = Database()
        self.email_service = EmailService()
```

## What to Avoid

❌ **Magic numbers**
```javascript
// Bad
if (user.age > 18) { ... }

// Good
const MINIMUM_AGE = 18;
if (user.age >= MINIMUM_AGE) { ... }
```

❌ **Deep nesting**
```python
# Refactor nested code using early returns or extraction
```

❌ **Long functions**
```javascript
// If function > 50 lines, consider extracting
```

❌ **Premature optimization**
```python
# Write clear code first, optimize only if needed
```

❌ **Commented code**
```javascript
// Delete it - use git history if needed
// function oldImplementation() { ... }
```

## Enforcement

### Automated

- **Pre-commit hooks** validate TODOs, markdown, whitespace
- **Format hooks** auto-format Python, JS, JSON, YAML
- **CI/CD** runs linters and tests

### Manual

- **Code reviews** catch patterns and design issues
- **`/x-analyze`** identifies problems before commit
- **Team discussion** for new patterns or exceptions

## When to Break Rules

Rules are guidelines, not laws. Break them when:
- Performance critically requires it (measure first)
- External API forces different style
- Existing codebase uses different convention (be consistent)
- Rule makes code less clear (rare)

Always document why you're breaking a rule.
