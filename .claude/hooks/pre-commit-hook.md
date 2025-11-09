# Pre-Commit Hook

Git hook that runs validation checks before allowing commits.

## What It Does

The [pre-commit.sh](pre-commit.sh) script performs the following checks:

1. **TODO/FIXME Check** - Warns about TODO/FIXME comments in staged files
2. **Markdown Validation** - Runs markdownlint on `.md` files (if installed)
3. **Trailing Whitespace** - Checks for trailing whitespace

If any check fails, the commit is prevented.

## Setup

### Make Executable
```bash
chmod +x .claude/hooks/pre-commit.sh
```

### Link to Git (Optional)
To use as an actual git hook:
```bash
ln -s ../../.claude/hooks/pre-commit.sh .git/hooks/pre-commit
```

## Dependencies

### Optional
- **markdownlint** - For markdown validation
  ```bash
  npm install -g markdownlint-cli
  ```

## Customization

Edit [pre-commit.sh](pre-commit.sh) to add additional checks:
- Run linters for other languages
- Execute test suite
- Check code coverage
- Validate commit message format
- Check for secrets/credentials

## Bypass (Emergency Use)

To skip the hook temporarily:
```bash
git commit --no-verify
```

⚠️ Use sparingly - bypassing hooks can introduce issues.
