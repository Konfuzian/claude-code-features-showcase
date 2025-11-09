# Pre-commit Hook

Validates before commits:
- TODOs have issue references
- Markdown syntax valid  
- No trailing whitespace

## Example
```javascript
// TODO: fix this  ❌
// TODO(#42): fix this  ✅
```

Runs on `git commit` or `/x-commit`.
