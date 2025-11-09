# Using x-code-reviewer Skill

## What It Does

Performs comprehensive code reviews checking for:
- **Correctness**: Logic errors, bugs, type issues
- **Security**: Injection vulnerabilities, XSS, authentication flaws
- **Performance**: Inefficient algorithms, memory leaks, N+1 queries
- **Readability**: Code clarity, naming, structure
- **Test Coverage**: Missing tests, edge cases
- **Best Practices**: Language-specific patterns, maintainability

## When to Use

- Reviewing pull requests
- Analyzing code quality
- Auditing code changes
- Finding security vulnerabilities
- Before merging code
- During code quality improvements

## How to Invoke

Skills are invoked automatically by Claude based on context. Request a code review:

```
Please review this authentication code for security issues
```

```
Can you review my PR and check for any problems?
```

```
Audit this payment processing code for vulnerabilities
```

## Example 1: Security Review

### Request
```
Review this login function for security issues:

function login(username, password) {
  const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
  const user = db.query(query)[0];

  if (user) {
    const token = username + ':' + password;
    res.cookie('auth', token);
    return { success: true };
  }
  return { success: false };
}
```

### Review Response
```
🔍 Code Review: login function

CRITICAL SECURITY ISSUES:

1. ❌ SQL Injection Vulnerability
   Location: Line 2
   Severity: CRITICAL

   Problem:
   - User input directly concatenated into SQL query
   - Attacker can inject: admin'-- to bypass authentication

   Fix:
   ```javascript
   const query = 'SELECT * FROM users WHERE username = ? LIMIT 1';
   const user = await db.query(query, [username])[0];
   ```

2. ❌ Plain Text Password Storage/Comparison
   Location: Line 2
   Severity: CRITICAL

   Problem:
   - Passwords should never be stored in plain text
   - Vulnerable to database breaches

   Fix:
   ```javascript
   // Store passwords hashed
   const isValid = await bcrypt.compare(password, user.password_hash);
   ```

3. ❌ Insecure Session Token
   Location: Line 5
   Severity: HIGH

   Problem:
   - Token is just username:password in plain text
   - Easily guessable and reversible
   - No expiration or cryptographic security

   Fix:
   ```javascript
   const token = jwt.sign(
     { userId: user.id },
     process.env.JWT_SECRET,
     { expiresIn: '1h' }
   );
   ```

4. ❌ Cookie Without Security Flags
   Location: Line 6
   Severity: HIGH

   Problem:
   - Missing httpOnly, secure, sameSite flags
   - Vulnerable to XSS theft

   Fix:
   ```javascript
   res.cookie('auth', token, {
     httpOnly: true,
     secure: true,
     sameSite: 'strict',
     maxAge: 3600000
   });
   ```

ADDITIONAL ISSUES:

5. ⚠️ No Rate Limiting
   - Vulnerable to brute force attacks
   - Add rate limiting middleware

6. ⚠️ Information Disclosure
   - Same response for wrong username/password
   - Consider: "Invalid credentials" (don't specify which)

7. ⚠️ No Input Validation
   - No checks for empty strings, special chars
   - Add validation before database query

8. ⚠️ Timing Attack Vulnerability
   - Different response times for valid/invalid users
   - Use constant-time comparison

SECURITY SCORE: 0/10 🚨

RECOMMENDED SECURE IMPLEMENTATION:

```javascript
async function login(username, password) {
  // Input validation
  if (!username || !password) {
    return { success: false, error: 'Invalid credentials' };
  }

  try {
    // Parameterized query
    const query = 'SELECT id, password_hash FROM users WHERE username = ? LIMIT 1';
    const [user] = await db.query(query, [username]);

    if (!user) {
      // Fake hash comparison for timing attack prevention
      await bcrypt.compare(password, '$2b$10$fake.hash.for.timing');
      return { success: false, error: 'Invalid credentials' };
    }

    // Secure password comparison
    const isValid = await bcrypt.compare(password, user.password_hash);

    if (!isValid) {
      return { success: false, error: 'Invalid credentials' };
    }

    // Generate secure JWT token
    const token = jwt.sign(
      { userId: user.id },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );

    // Set secure cookie
    res.cookie('auth', token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict',
      maxAge: 3600000 // 1 hour
    });

    return { success: true };

  } catch (error) {
    console.error('Login error:', error);
    return { success: false, error: 'Authentication failed' };
  }
}
```

TESTING RECOMMENDATIONS:
- Add tests for SQL injection attempts
- Test brute force protection
- Verify cookie security flags
- Test password hashing
```

## Example 2: Performance Review

### Request
```
Review this code for performance issues:

function findDuplicates(users) {
  const duplicates = [];

  for (let i = 0; i < users.length; i++) {
    for (let j = i + 1; j < users.length; j++) {
      if (users[i].email === users[j].email) {
        duplicates.push(users[i]);
      }
    }
  }

  return duplicates;
}
```

### Review Response
```
🔍 Code Review: findDuplicates function

PERFORMANCE ISSUES:

1. ❌ Inefficient Algorithm - O(n²) Complexity
   Location: Lines 4-10
   Severity: HIGH

   Problem:
   - Nested loops create quadratic time complexity
   - For 10,000 users: 100,000,000 comparisons
   - Slow for large datasets

   Current: O(n²) - Quadratic
   Optimal: O(n) - Linear

   Fix:
   ```javascript
   function findDuplicates(users) {
     const seen = new Map();
     const duplicates = [];

     for (const user of users) {
       if (seen.has(user.email)) {
         duplicates.push(user);
       } else {
         seen.set(user.email, true);
       }
     }

     return duplicates;
   }
   ```

PERFORMANCE COMPARISON:

| Users | Current (O(n²)) | Optimized (O(n)) | Speedup |
|-------|-----------------|------------------|---------|
| 100   | 10,000 ops      | 100 ops          | 100x    |
| 1,000 | 1,000,000 ops   | 1,000 ops        | 1,000x  |
| 10,000| 100,000,000 ops | 10,000 ops       | 10,000x |

ADDITIONAL IMPROVEMENTS:

2. Consider Edge Cases
   ```javascript
   function findDuplicates(users) {
     if (!users || users.length === 0) return [];

     const seen = new Map();
     const duplicates = [];

     for (const user of users) {
       const email = user?.email?.toLowerCase(); // Normalize
       if (!email) continue; // Skip invalid entries

       if (seen.has(email)) {
         duplicates.push(user);
       } else {
         seen.set(email, true);
       }
     }

     return duplicates;
   }
   ```

3. Memory Optimization
   - If only counting duplicates (not returning them):
   ```javascript
   function countDuplicates(users) {
     const seen = new Set();
     let count = 0;

     for (const user of users) {
       const email = user.email;
       if (seen.has(email)) {
         count++;
       } else {
         seen.add(email);
       }
     }

     return count;
   }
   ```

PERFORMANCE SCORE: 3/10 ⚠️
(Correct but inefficient)
```

## Example 3: Code Quality Review

### Request
```
Review this React component for best practices:

function UserProfile(props) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/users/' + props.id)
      .then(res => res.json())
      .then(setData);
  });

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.email}</p>
      <button onClick={() => {
        fetch('/api/users/' + props.id + '/follow', { method: 'POST' });
      }}>Follow</button>
    </div>
  );
}
```

### Review Response
```
🔍 Code Review: UserProfile component

CRITICAL ISSUES:

1. ❌ Infinite Re-render Loop
   Location: Lines 4-8
   Severity: CRITICAL

   Problem:
   - useEffect has no dependency array
   - Runs after every render
   - Each run updates state, causing re-render
   - Creates infinite loop

   Fix:
   ```javascript
   useEffect(() => {
     fetch(`/api/users/${props.id}`)
       .then(res => res.json())
       .then(setData);
   }, [props.id]); // Add dependency array
   ```

2. ❌ No Error Handling
   Location: Lines 4-8, 16-18
   Severity: HIGH

   Problem:
   - Network failures crash the component
   - User sees broken UI

   Fix:
   ```javascript
   const [error, setError] = useState(null);

   useEffect(() => {
     fetch(`/api/users/${props.id}`)
       .then(res => {
         if (!res.ok) throw new Error('Failed to load user');
         return res.json();
       })
       .then(setData)
       .catch(setError);
   }, [props.id]);

   if (error) return <div>Error: {error.message}</div>;
   ```

3. ❌ Missing Cleanup
   Location: Lines 4-8
   Severity: MEDIUM

   Problem:
   - If component unmounts during fetch, setState on unmounted component
   - Memory leak warning

   Fix:
   ```javascript
   useEffect(() => {
     let cancelled = false;

     fetch(`/api/users/${props.id}`)
       .then(res => res.json())
       .then(data => {
         if (!cancelled) setData(data);
       });

     return () => { cancelled = true; };
   }, [props.id]);
   ```

BEST PRACTICE VIOLATIONS:

4. ⚠️ Props Destructuring
   ```javascript
   // Better:
   function UserProfile({ id }) {
     // Use id directly
   }
   ```

5. ⚠️ Loading State Doesn't Handle Re-fetch
   ```javascript
   const [loading, setLoading] = useState(true);

   useEffect(() => {
     setLoading(true);
     // ... fetch
     .then(data => {
       setData(data);
       setLoading(false);
     });
   }, [id]);
   ```

6. ⚠️ Inline Event Handler
   - Re-creates function on every render
   - Should use useCallback or extract

7. ⚠️ No Accessibility
   - Missing ARIA labels
   - No loading announcement

CODE QUALITY SCORE: 4/10 ⚠️

RECOMMENDED IMPLEMENTATION:

```javascript
import { useState, useEffect, useCallback } from 'react';

function UserProfile({ id }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);

    fetch(`/api/users/${id}`)
      .then(res => {
        if (!res.ok) throw new Error('Failed to load user');
        return res.json();
      })
      .then(data => {
        if (!cancelled) {
          setData(data);
          setLoading(false);
        }
      })
      .catch(err => {
        if (!cancelled) {
          setError(err);
          setLoading(false);
        }
      });

    return () => { cancelled = true; };
  }, [id]);

  const handleFollow = useCallback(async () => {
    try {
      const res = await fetch(`/api/users/${id}/follow`, {
        method: 'POST'
      });
      if (!res.ok) throw new Error('Failed to follow');
      // Update UI or refetch data
    } catch (err) {
      console.error('Follow failed:', err);
      // Show error to user
    }
  }, [id]);

  if (loading) {
    return <div role="status" aria-live="polite">Loading user profile...</div>;
  }

  if (error) {
    return <div role="alert">Error: {error.message}</div>;
  }

  if (!data) {
    return <div>No user data found</div>;
  }

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.email}</p>
      <button
        onClick={handleFollow}
        aria-label={`Follow ${data.name}`}
      >
        Follow
      </button>
    </div>
  );
}

export default UserProfile;
```
```

## Review Checklist

The skill checks for:

### Security
- [ ] SQL injection vulnerabilities
- [ ] XSS vulnerabilities
- [ ] Authentication/authorization flaws
- [ ] Insecure data storage
- [ ] CSRF protection
- [ ] Input validation
- [ ] Output encoding

### Performance
- [ ] Algorithm efficiency (Big O)
- [ ] Memory usage
- [ ] Database query optimization
- [ ] Caching opportunities
- [ ] Unnecessary re-renders (React)
- [ ] Bundle size

### Correctness
- [ ] Logic errors
- [ ] Edge cases
- [ ] Type safety
- [ ] Null/undefined handling
- [ ] Error handling
- [ ] Race conditions

### Code Quality
- [ ] Naming conventions
- [ ] Code duplication (DRY)
- [ ] Function length
- [ ] Complexity
- [ ] Comments and documentation
- [ ] Consistent style

### Testing
- [ ] Test coverage
- [ ] Missing test cases
- [ ] Edge case tests
- [ ] Error path tests

## Tips

1. **Be Specific**: "Review for security" vs "Review everything"
2. **Provide Context**: Mention if code handles sensitive data
3. **Share Test Coverage**: Helps identify gaps
4. **Ask Follow-ups**: Request detailed explanations
5. **Iterative**: Review, fix, review again

## Common Use Cases

### Pre-commit Review
```
Please review my changes before I commit
```

### Pull Request Review
```
Review this PR for security and performance issues
```

### Security Audit
```
Audit this authentication system for vulnerabilities
```

### Performance Optimization
```
Review this function - it's running slow with large datasets
```

### Best Practices Check
```
Is this React component following best practices?
```

## Integration with Workflows

### Code Review Workflow
```
1. Make code changes
2. Request code review (x-code-reviewer skill invoked)
3. Fix identified issues
4. /x-test - Add tests for fixes
5. Review again
6. /x-commit - Commit improved code
```

### Security Audit Workflow
```
1. Identify security-critical code
2. Request security audit
3. Address CRITICAL and HIGH severity issues
4. /x-test - Add security tests
5. /x-test-coverage - Verify security test coverage
6. Document security measures
```

## Related Skills & Commands

- [/x-analyze](../commands/x-analyze.md) - Similar automated analysis
- [/x-refactor](../commands/x-refactor.md) - Fix identified issues
- [/x-test](../commands/x-test.md) - Add missing tests
- [x-test-generator](./x-test-generator.md) - Generate comprehensive tests
