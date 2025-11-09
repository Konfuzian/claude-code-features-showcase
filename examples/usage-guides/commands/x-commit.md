# Using /x-commit

## What It Does

Automatically creates meaningful git commits by:
- Analyzing staged and unstaged changes
- Generating descriptive commit messages
- Following conventional commit format
- Including detailed change lists
- Staging all changes before committing

## When to Use

- After completing a logical unit of work
- When you want to commit without manually writing messages
- To maintain consistent commit message format
- At natural stopping points in development

## Basic Usage

### Commit All Changes

```
/x-commit
```

Claude will:
1. Analyze all staged and unstaged changes
2. Stage everything with `git add -A`
3. Generate a descriptive commit message
4. Create the commit

**Note:** This command is autonomous - it doesn't ask for confirmation.

## Example

### Before Commit

```bash
$ git status
On branch feature/user-auth
Changes not staged for commit:
  modified:   src/auth/login.js
  modified:   src/auth/middleware.js
  modified:   tests/auth.test.js

Untracked files:
  src/auth/session.js
```

### Command

```
/x-commit
```

### Generated Commit

```
feat: Add session management to authentication system

Implement JWT-based session handling with refresh tokens.

Changes:
- Add session.js with token generation and validation
- Update login.js to create sessions on successful auth
- Add middleware.js for protected route authentication
- Add comprehensive tests for session lifecycle

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### After Commit

```bash
$ git log -1 --oneline
a3f7d21 feat: Add session management to authentication system
```

## Commit Message Format

```
<type>: <short summary>

<detailed description>

Changes:
- <change 1>
- <change 2>
- <change 3>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Commit Types

| Type | When to Use | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: Add user authentication` |
| `fix` | Bug fix | `fix: Resolve memory leak in cache` |
| `refactor` | Code refactoring | `refactor: Simplify validation logic` |
| `docs` | Documentation | `docs: Update API reference` |
| `test` | Add/update tests | `test: Add edge cases for parser` |
| `chore` | Maintenance | `chore: Update dependencies` |
| `style` | Formatting | `style: Apply prettier formatting` |
| `perf` | Performance | `perf: Optimize database queries` |

## Real Examples

### Feature Addition
```
feat: Implement password reset functionality

Add email-based password reset flow with secure tokens.

Changes:
- Add password reset request endpoint
- Implement secure token generation and validation
- Create password reset email template
- Add rate limiting to prevent abuse
- Add tests for complete reset flow

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Bug Fix
```
fix: Prevent duplicate user creation on concurrent requests

Add database unique constraint and handle race conditions.

Changes:
- Add unique index on users.email column
- Add error handling for duplicate key violations
- Update user creation to return existing user if duplicate
- Add integration test for concurrent signups

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Refactoring
```
refactor: Extract authentication logic into reusable middleware

Reduce code duplication across route handlers.

Changes:
- Create requireAuth middleware for protected routes
- Create requireRole middleware for role-based access
- Update all route handlers to use new middleware
- Remove duplicated auth checks from individual handlers
- Add middleware tests

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## What Gets Committed

### All Changes
- Modified files
- New files (untracked)
- Deleted files
- Renamed files

### Excluded Files
Files in `.gitignore` are automatically excluded:
- `node_modules/`
- `.env`
- Build artifacts
- IDE settings

## Tips

1. **Commit Often**: Small, focused commits are better than large ones
2. **Complete Logical Units**: Finish a feature/fix before committing
3. **Review Before Committing**: Check `git status` and `git diff` first
4. **Keep Related Changes Together**: Don't mix unrelated changes
5. **Run Tests First**: Ensure code works before committing

## Integration with Workflow

### Basic Workflow
```
1. Make code changes
2. /x-test                 # Generate/update tests
3. npm test                # Verify tests pass
4. /x-commit               # Commit changes
```

### Quality-Focused Workflow
```
1. Make code changes
2. /x-analyze              # Check for issues
3. Fix any problems
4. /x-test                 # Add tests
5. npm test                # Verify tests pass
6. /x-commit               # Commit changes
```

### Documentation Workflow
```
1. Implement feature
2. /x-test                 # Add tests
3. /x-docs                 # Generate documentation
4. Review and refine
5. /x-commit               # Commit code + tests + docs
```

## Edge Cases

### No Changes
```
/x-commit
→ "No changes to commit"
```

### Pre-commit Hook Failure
If pre-commit hooks modify files:
```
1. Hook runs and formats code
2. Claude detects file changes
3. Amends commit with formatted code
```

### Merge Conflicts
```
/x-commit will fail during merge conflicts
→ Resolve conflicts manually first
→ Then use /x-commit
```

## Best Practices

### DO
✅ Commit working code (tests pass)
✅ Group related changes together
✅ Commit before switching tasks
✅ Use descriptive changes list

### DON'T
❌ Commit broken code
❌ Mix unrelated changes
❌ Commit secrets or credentials
❌ Skip testing before committing

## Related Commands

- [/x-analyze](./x-analyze.md) - Check quality before committing
- [/x-test](./x-test.md) - Add tests before committing
- [/x-docs](./x-docs.md) - Document before committing

## Git Best Practices

### After Committing

```bash
# View commit
git show

# View commit history
git log --oneline

# Push to remote (when ready)
git push origin feature-branch
```

### Amending Commits

If you need to modify the last commit:
```bash
# Make additional changes
git add .
git commit --amend --no-edit
```

**Note:** Only amend commits that haven't been pushed to shared branches.
