# /x-analyze

Analyzes code for quality issues, security vulnerabilities, and performance problems.

## Usage
```
/x-analyze
```

## Example
```javascript
const query = `SELECT * FROM users WHERE id='${userId}'`;
```
→ `❌ SQL Injection - Use parameterized queries`

## Workflow
`/x-analyze` → fix → `/x-test` → `/x-commit`
