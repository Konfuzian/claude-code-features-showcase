# Using Pre-commit Hook

## What It Does

The pre-commit hook runs automatically before each git commit to validate:
- **TODO/FIXME comments**: Ensures they have proper issue references
- **Markdown files**: Validates markdown syntax
- **Trailing whitespace**: Removes trailing whitespace from files
- **Code quality**: Prevents committing code with known issues

Located at: [.claude/hooks/pre-commit.sh](../../../.claude/hooks/pre-commit.sh)

## When It Runs

Automatically triggered when you:
- Run `git commit`
- Use `/x-commit` command
- Create commits through any git interface

## Example 1: Successful Commit

### Scenario: Clean Code

```bash
$ git add src/auth.js
$ git commit -m "feat: Add authentication"
```

### Hook Output
```
Running pre-commit checks...
✓ No TODOs without issue references
✓ Markdown files valid
✓ No trailing whitespace
✓ All checks passed

[main a3f7d21] feat: Add authentication
 1 file changed, 45 insertions(+)
```

Commit proceeds successfully.

## Example 2: Blocked Commit - TODO Without Reference

### Scenario: Code with Incomplete TODO

```javascript
// src/api.js
function processPayment(data) {
  // TODO: add validation
  return payment.process(data);
}
```

### Attempting to Commit
```bash
$ git add src/api.js
$ git commit -m "Add payment processing"
```

### Hook Output
```
Running pre-commit checks...
❌ Found TODO/FIXME without issue reference:

  src/api.js:2  // TODO: add validation

TODOs must reference an issue:
  ✓ // TODO(#123): add validation
  ✓ // FIXME: fix race condition (#456)
  ✓ // TODO: add validation (https://github.com/org/repo/issues/789)

Commit blocked. Please fix the issues above.
```

### Fixing the Issue
```javascript
// src/api.js
function processPayment(data) {
  // TODO(#42): add validation for card number and CVV
  return payment.process(data);
}
```

```bash
$ git add src/api.js
$ git commit -m "Add payment processing"
```

```
Running pre-commit checks...
✓ No TODOs without issue references
✓ Markdown files valid
✓ No trailing whitespace
✓ All checks passed

[main b4e8f32] Add payment processing
 1 file changed, 3 insertions(+)
```

## Example 3: Blocked Commit - Invalid Markdown

### Scenario: Malformed Markdown

```markdown
<!-- docs/api.md -->
# API Documentation

## Endpoints

[Get User](/api/users/{id}

Missing closing bracket!
```

### Attempting to Commit
```bash
$ git add docs/api.md
$ git commit -m "docs: Add API documentation"
```

### Hook Output
```
Running pre-commit checks...
✓ No TODOs without issue references
❌ Markdown validation failed:

  docs/api.md:5 - Unclosed link: [Get User](/api/users/{id}

Please fix markdown syntax errors.
Commit blocked.
```

### Fixing the Issue
```markdown
<!-- docs/api.md -->
# API Documentation

## Endpoints

[Get User](/api/users/{id})
```

Now commit succeeds.

## Example 4: Automatic Fix - Trailing Whitespace

### Scenario: Files with Trailing Whitespace

```javascript
// src/utils.js
function format(text) {
  return text.trim();
}
```
(Spaces at end of lines 1, 2, 3)

### Committing
```bash
$ git add src/utils.js
$ git commit -m "Add formatting utility"
```

### Hook Output
```
Running pre-commit checks...
✓ No TODOs without issue references
✓ Markdown files valid
⚠ Removing trailing whitespace from:
  - src/utils.js

Files modified by pre-commit hook.
Staging automatic fixes...

[main c9d2e41] Add formatting utility
 1 file changed, 3 insertions(+)
```

The hook automatically:
1. Removes trailing whitespace
2. Stages the fixed files
3. Includes fixes in the commit

## TODO/FIXME Reference Formats

### Valid Formats

```javascript
// ✅ Issue number
// TODO(#123): Implement caching

// ✅ Issue URL
// FIXME: Fix race condition (https://github.com/org/repo/issues/456)

// ✅ Multiple issues
// TODO(#789, #790): Refactor authentication and authorization

// ✅ JIRA-style
// TODO(PROJ-123): Add validation
```

### Invalid Formats

```javascript
// ❌ No reference
// TODO: add validation

// ❌ Generic reference
// TODO(later): optimize this

// ❌ Person reference
// FIXME(@john): check this logic
```

## Configuration

### Location
```
.claude/hooks/pre-commit.sh
```

### Customization

Edit the hook to adjust checks:

```bash
#!/bin/bash

# Disable markdown validation
# check_markdown() { return 0; }

# Make trailing whitespace check fail instead of auto-fix
# STRICT_WHITESPACE=true

# Add custom checks
check_custom() {
  # Your custom validation
  if grep -r "console.log" src/; then
    echo "❌ Found console.log statements"
    return 1
  fi
  return 0
}
```

### Disabling the Hook

Temporarily bypass (not recommended):
```bash
git commit --no-verify -m "Emergency fix"
```

Permanently disable:
```bash
# Remove or comment out the hook configuration
# in .claude/hooks.json
```

## Hook Exit Codes

| Code | Meaning | Result |
|------|---------|--------|
| 0 | All checks passed | Commit proceeds |
| 1 | Checks failed | Commit blocked |
| Auto-fix | Files modified | Files staged & commit proceeds |

## Best Practices

### DO
✅ Fix issues found by the hook
✅ Write descriptive issue references
✅ Run `git status` after hook auto-fixes
✅ Keep hooks fast (< 5 seconds)

### DON'T
❌ Use `--no-verify` to bypass hooks
❌ Leave unresolved TODOs in production code
❌ Ignore hook messages
❌ Make hooks too slow or complex

## Common Issues

### Hook Not Running

**Problem:** Commits succeed without hook running

**Solution:**
```bash
# Make sure hook is executable
chmod +x .claude/hooks/pre-commit.sh

# Verify hook configuration
cat .claude/hooks.json

# Check git hooks
ls -la .git/hooks/
```

### Hook Fails on Valid Code

**Problem:** Hook incorrectly flags valid code

**Solution:**
```bash
# Check what pattern triggered failure
# Adjust hook script if needed
# Or adjust code to match expected format
```

### Auto-fix Loop

**Problem:** Hook keeps modifying files

**Solution:**
```bash
# Check git status to see what's changing
git status

# Manually stage auto-fixed files
git add -u

# Try commit again
git commit -m "message"
```

## Integration with Workflows

### Standard Workflow
```
1. Write code
2. git add <files>
3. git commit -m "message"
   → Hook runs automatically
   → Either succeeds or provides fix instructions
4. If blocked: fix issues, commit again
```

### With /x-commit
```
1. Write code
2. /x-commit
   → Stages all changes
   → Creates commit message
   → Hook runs automatically
   → Either succeeds or provides fix instructions
```

## Related Hooks

- [Format Hook](./format-hook.md) - Auto-formats code on file edits
- [Commit Message Hook](./commit-msg-hook.md) - Validates commit messages

## See Also

- [Git Hooks Documentation](https://git-scm.com/docs/githooks)
- [.claude/hooks/README.md](../../../.claude/hooks/README.md) - Hook configuration guide
