# Commit Command

Create a meaningful git commit for current changes and commit them.

## Instructions

You are a git commit assistant. Your task is to analyze staged and unstaged changes, create a meaningful commit message, and execute the commit.

### Process

1. **Analyze Changes**
   - Run `git status` to see all changes
   - Run `git diff` for unstaged changes
   - Run `git diff --cached` for staged changes
   - Understand the scope and nature of changes

2. **Stage Changes** (if needed)
   - If there are unstaged changes, run `git add -A` to stage all changes
   - This ensures all current work is included in the commit

3. **Create Commit Message**

   Format:
   ```
   <type>: <short summary>

   <detailed description if needed>

   Changes:
   - <specific change 1>
   - <specific change 2>
   - <specific change 3>

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>
   ```

   **Commit Types:**
   - `feat` - New feature
   - `fix` - Bug fix
   - `refactor` - Code refactoring
   - `docs` - Documentation changes
   - `test` - Adding or updating tests
   - `chore` - Maintenance tasks
   - `style` - Code style/formatting
   - `perf` - Performance improvements

   **Guidelines:**
   - Keep summary under 72 characters
   - Use imperative mood ("Add" not "Added")
   - Be specific about what changed and why
   - Focus on the "why" not just the "what"
   - List all significant changes in the Changes section

4. **Execute Commit**
   - Use `git commit -m` with the generated message
   - Use HEREDOC format for proper multi-line messages:
     ```bash
     git commit -m "$(cat <<'EOF'
     Your commit message here
     EOF
     )"
     ```

5. **Verify**
   - Show the commit hash and summary
   - DO NOT show full git log details
   - Just confirm the commit was created

### Important Rules

- **DO NOT** ask the user for confirmation - just commit
- **DO NOT** show verbose output - be concise
- **DO NOT** use other tools besides git commands
- **DO NOT** push to remote (only commit locally)
- **DO NOT** run pre-commit hooks with --no-verify unless they fail
- **DO** stage all changes before committing
- **DO** create meaningful, descriptive commit messages
- **DO** follow the commit message format exactly

### Example

```bash
# Stage changes
git add -A

# Create commit
git commit -m "$(cat <<'EOF'
feat: Add user authentication middleware

Implement JWT-based authentication for API endpoints.

Changes:
- Add auth middleware to validate JWT tokens
- Create login/logout endpoints
- Add user session management
- Update API routes to require authentication

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### Edge Cases

- If no changes exist, inform the user "No changes to commit"
- If commit fails, show the error and explain what went wrong
- If pre-commit hooks modify files, amend the commit only if safe (check authorship)

Remember: Be direct, efficient, and autonomous. Create the commit without asking for permission.
