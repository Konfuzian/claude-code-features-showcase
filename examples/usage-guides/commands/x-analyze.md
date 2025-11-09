# Using /x-analyze

## What It Does

Performs comprehensive code analysis checking for:
- Code quality issues (complexity, duplication, style)
- Security vulnerabilities (injection, XSS, insecure patterns)
- Performance problems (inefficient algorithms, memory leaks)
- Best practice violations

## When to Use

- Before committing significant changes
- When reviewing unfamiliar code
- To identify refactoring opportunities
- As part of code quality audits

## Basic Usage

### Analyze Current File

```
/x-analyze
```

When you have a file open, Claude will analyze it and provide detailed feedback.

### Analyze Specific File

```
Can you analyze src/auth/login.js for security issues?
```

### Analyze Multiple Files

```
Please analyze all files in src/api/ for code quality issues
```

## Example Output

### Input Code (auth.js)
```javascript
function authenticate(username, password) {
  const query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
  const result = db.query(query);
  return result.length > 0;
}
```

### Analysis Result

```
🔍 Code Analysis Results for auth.js

CRITICAL ISSUES:
1. SQL Injection Vulnerability (Line 2)
   - Concatenating user input directly into SQL query
   - Recommendation: Use parameterized queries

2. Plain Text Password Comparison (Line 2)
   - Passwords should never be stored in plain text
   - Recommendation: Use bcrypt or argon2 for password hashing

SECURITY SCORE: 2/10 ⚠️

Suggested Fix:
```javascript
async function authenticate(username, password) {
  const query = "SELECT * FROM users WHERE username = ? LIMIT 1";
  const result = await db.query(query, [username]);

  if (result.length === 0) return false;

  return await bcrypt.compare(password, result[0].password_hash);
}
```
```

## Common Patterns Found

### Code Quality Issues
- **High Complexity**: Functions with too many branches
- **Code Duplication**: Repeated logic across files
- **Magic Numbers**: Unexplained constants
- **Long Functions**: Functions exceeding 50 lines

### Security Issues
- **SQL Injection**: Unsanitized database queries
- **XSS Vulnerabilities**: Unescaped user input in HTML
- **Path Traversal**: Unsafe file path handling
- **Hardcoded Secrets**: API keys or passwords in code

### Performance Issues
- **N+1 Queries**: Database queries in loops
- **Memory Leaks**: Unreleased resources
- **Inefficient Algorithms**: O(n²) when O(n log n) possible
- **Unnecessary Re-renders**: React components without memoization

## Tips

1. **Run Before Committing**: Make it part of your workflow
2. **Focus on Critical Issues First**: Address security before style
3. **Combine with /x-refactor**: Fix issues systematically
4. **Use with Git Diff**: Analyze only changed files

## Integration with Workflow

```
# Typical workflow
1. Make code changes
2. /x-analyze              # Check for issues
3. Fix critical problems
4. /x-test                 # Generate/update tests
5. /x-commit               # Commit with good message
```

## Related Commands

- [/x-refactor](./x-refactor.md) - Fix identified issues
- [/x-test](./x-test.md) - Add tests for fixed code
- [/x-docs](./x-docs.md) - Document improvements
