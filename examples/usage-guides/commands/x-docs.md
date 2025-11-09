# Using /x-docs

## What It Does

Generates comprehensive documentation including:
- Function/method documentation with parameters and return values
- Usage examples with real code
- API documentation
- Module/class overviews
- README sections

## When to Use

- After implementing new public APIs
- When onboarding new team members
- To document complex algorithms
- Before publishing libraries
- When code lacks clear documentation

## Basic Usage

### Document Current File

```
/x-docs
```

Claude will generate documentation for the open file.

### Document Specific Function

```
Please document the authenticateUser function including all edge cases
```

### Document Entire Module

```
Generate API documentation for all public functions in src/api/users.js
```

## Example

### Input Code (cache.js)

```javascript
export class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }
    this.cache.set(key, value);
    if (this.cache.size > this.capacity) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
  }
}
```

### Generated Documentation

```javascript
/**
 * Least Recently Used (LRU) Cache implementation
 *
 * A cache that stores a limited number of items and evicts the least
 * recently used item when capacity is exceeded. Uses Map to maintain
 * insertion order for efficient LRU tracking.
 *
 * @class LRUCache
 * @example
 * const cache = new LRUCache(2);
 * cache.put(1, 'one');
 * cache.put(2, 'two');
 * console.log(cache.get(1)); // 'one'
 * cache.put(3, 'three');     // Evicts key 2
 * console.log(cache.get(2)); // -1 (not found)
 */
export class LRUCache {
  /**
   * Creates a new LRU cache with specified capacity
   *
   * @param {number} capacity - Maximum number of items to store (must be positive)
   * @throws {Error} If capacity is not a positive integer
   */
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  /**
   * Retrieves a value from the cache and marks it as recently used
   *
   * When a key is accessed, it's moved to the end of the Map to mark
   * it as most recently used. This ensures it won't be evicted unless
   * capacity is exceeded and it becomes the least recently used again.
   *
   * @param {*} key - The key to retrieve
   * @returns {*} The cached value, or -1 if key not found
   *
   * @example
   * cache.put('user:123', { name: 'Alice' });
   * const user = cache.get('user:123'); // { name: 'Alice' }
   * const missing = cache.get('user:999'); // -1
   */
  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  /**
   * Adds or updates a cache entry
   *
   * If the key already exists, it updates the value and marks it as
   * recently used. If adding a new key would exceed capacity, the
   * least recently used item (first in Map) is evicted.
   *
   * @param {*} key - The key to store
   * @param {*} value - The value to cache
   *
   * @example
   * // Basic usage
   * cache.put('config', { theme: 'dark' });
   *
   * // Update existing
   * cache.put('config', { theme: 'light' }); // Updates and refreshes
   *
   * // Eviction on capacity
   * const cache = new LRUCache(2);
   * cache.put(1, 'a');
   * cache.put(2, 'b');
   * cache.put(3, 'c'); // Evicts key 1
   */
  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }
    this.cache.set(key, value);
    if (this.cache.size > this.capacity) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
  }
}
```

## Documentation Styles

### JSDoc (JavaScript/TypeScript)
```javascript
/**
 * @param {string} name - User's name
 * @returns {Promise<User>} Created user object
 * @throws {ValidationError} If name is invalid
 */
```

### Docstrings (Python)
```python
def process_data(data: list[dict]) -> pd.DataFrame:
    """
    Process raw data into a pandas DataFrame.

    Args:
        data: List of dictionaries containing raw records

    Returns:
        Processed DataFrame with cleaned columns

    Raises:
        ValueError: If data is empty or malformed
    """
```

### Godoc (Go)
```go
// FetchUser retrieves a user by ID from the database.
// Returns nil and an error if the user is not found.
//
// Example:
//   user, err := FetchUser(123)
//   if err != nil {
//       log.Fatal(err)
//   }
func FetchUser(id int) (*User, error) {
```

## Tips

1. **Document Public APIs First**: Focus on exported/public functions
2. **Include Examples**: Real usage examples are most valuable
3. **Explain Why, Not Just What**: Document intent and edge cases
4. **Keep It Updated**: Re-generate after significant changes
5. **Use Type Hints**: They help generate better documentation

## Documentation Types

### API Documentation
Complete reference for public interfaces with parameters, return values, and examples.

### Usage Guides
Step-by-step tutorials showing how to accomplish common tasks.

### Architecture Docs
High-level overviews of system design and component interactions.

### README Sections
Quick-start guides, installation instructions, and feature highlights.

## Integration with Workflow

```
# Documentation workflow
1. Implement feature
2. /x-test                 # Generate tests
3. /x-docs                 # Document the API
4. Review and refine docs
5. /x-commit               # Commit code + docs together
```

## Related Commands

- [/x-analyze](./x-analyze.md) - Ensure code quality before documenting
- [/x-test](./x-test.md) - Tests serve as living documentation
- [/x-refactor](./x-refactor.md) - Simpler code needs less documentation
