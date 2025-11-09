# Command Chaining

Combining commands in sequence.

## Common Chains

**Quality Assurance:**
`/x-analyze` → fix → `/x-test` → `/x-commit`

**Full Feature:**
Implement → `/x-analyze` → `/x-test` → `/x-docs` → `/x-commit`

**Safe Refactoring:**
`/x-test` → `/x-refactor` → `npm test` → `/x-commit`

## Example
```
1. Add password reset
2. /x-analyze → finds missing rate limiting
3. Add rate limiting
4. /x-test
5. /x-commit
```
