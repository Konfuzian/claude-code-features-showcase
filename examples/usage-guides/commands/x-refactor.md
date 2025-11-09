# Using /x-refactor

## What It Does

Refactors code to improve:
- Readability and maintainability
- Code organization and modularity
- Performance and efficiency
- Adherence to best practices
- DRY (Don't Repeat Yourself) principles

## When to Use

- After identifying code smells with `/x-analyze`
- When code is difficult to understand or modify
- To extract reusable components
- Before adding new features to legacy code
- When test coverage is good (refactoring safety net)

## Basic Usage

### Refactor Current File

```
/x-refactor
```

### Refactor Specific Code

```
Please refactor the nested if statements in validateUser to use early returns
```

### Refactor with Focus

```
Refactor this code to improve performance - it's running slow on large datasets
```

## Example

### Before Refactoring

```javascript
function processOrder(order) {
  if (order) {
    if (order.items) {
      if (order.items.length > 0) {
        let total = 0;
        for (let i = 0; i < order.items.length; i++) {
          if (order.items[i].price) {
            if (order.items[i].quantity) {
              total = total + (order.items[i].price * order.items[i].quantity);
              if (order.items[i].discount) {
                total = total - (order.items[i].price * order.items[i].quantity * order.items[i].discount / 100);
              }
            }
          }
        }
        if (order.shippingCost) {
          total = total + order.shippingCost;
        }
        if (order.taxRate) {
          total = total + (total * order.taxRate / 100);
        }
        return total;
      } else {
        return 0;
      }
    } else {
      return 0;
    }
  } else {
    return 0;
  }
}
```

### After Refactoring

```javascript
function processOrder(order) {
  // Early returns for invalid input
  if (!order?.items?.length) {
    return 0;
  }

  const subtotal = calculateItemsSubtotal(order.items);
  const withShipping = subtotal + (order.shippingCost ?? 0);
  const withTax = applyTax(withShipping, order.taxRate);

  return withTax;
}

function calculateItemsSubtotal(items) {
  return items.reduce((total, item) => {
    const itemTotal = calculateItemTotal(item);
    return total + itemTotal;
  }, 0);
}

function calculateItemTotal(item) {
  const { price = 0, quantity = 0, discount = 0 } = item;
  const subtotal = price * quantity;
  const discountAmount = subtotal * (discount / 100);
  return subtotal - discountAmount;
}

function applyTax(amount, taxRate = 0) {
  return amount * (1 + taxRate / 100);
}
```

### What Changed

**Improvements:**
1. ✅ **Reduced nesting**: From 7 levels to 1-2 levels
2. ✅ **Early returns**: Clearer control flow
3. ✅ **Extracted functions**: Single responsibility principle
4. ✅ **Better naming**: Self-documenting code
5. ✅ **Modern syntax**: Optional chaining, default parameters
6. ✅ **Functional approach**: Reduce instead of loops
7. ✅ **Removed magic numbers**: Clear percentage calculations

## Common Refactoring Patterns

### Extract Function
```javascript
// Before
if (user.age >= 18 && user.country === 'US' && user.verified) {
  // ...
}

// After
if (isEligibleUser(user)) {
  // ...
}

function isEligibleUser(user) {
  return user.age >= 18 && user.country === 'US' && user.verified;
}
```

### Replace Conditional with Polymorphism
```javascript
// Before
function getArea(shape) {
  if (shape.type === 'circle') {
    return Math.PI * shape.radius ** 2;
  } else if (shape.type === 'rectangle') {
    return shape.width * shape.height;
  }
}

// After
class Circle {
  getArea() {
    return Math.PI * this.radius ** 2;
  }
}

class Rectangle {
  getArea() {
    return this.width * this.height;
  }
}
```

### Introduce Parameter Object
```javascript
// Before
function createUser(name, email, age, country, verified) {
  // ...
}

// After
function createUser(userData) {
  const { name, email, age, country, verified } = userData;
  // ...
}
```

### Remove Dead Code
```javascript
// Before
function process(data) {
  const temp = data.map(x => x * 2); // Unused variable
  return data.filter(x => x > 0);
}

// After
function process(data) {
  return data.filter(x => x > 0);
}
```

## Tips

1. **Have Tests First**: Refactoring should preserve behavior
2. **One Change at a Time**: Small, focused refactorings
3. **Run Tests After Each Change**: Ensure nothing breaks
4. **Use Version Control**: Commit before refactoring
5. **Measure Performance**: If optimizing for speed

## Safety Checklist

- [ ] Tests exist and pass before refactoring
- [ ] Refactoring doesn't change external behavior
- [ ] Tests still pass after refactoring
- [ ] Code is more readable than before
- [ ] No new bugs introduced

## Integration with Workflow

```
# Safe refactoring workflow
1. /x-analyze              # Identify code smells
2. /x-test                 # Ensure test coverage
3. npm test                # Verify tests pass
4. /x-refactor             # Refactor the code
5. npm test                # Verify tests still pass
6. /x-commit               # Commit refactoring
```

## Related Commands

- [/x-analyze](./x-analyze.md) - Find refactoring opportunities
- [/x-test](./x-test.md) - Ensure safety net before refactoring
- [/x-docs](./x-docs.md) - Document refactored code
