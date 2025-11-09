# Hooks

Event-driven automation that responds to specific actions in your development workflow.

## Available Hooks

### pre-commit.sh
Runs before git commits to ensure code quality:
- Checks for TODO/FIXME comments
- Runs linter on staged files
- Executes test suite
- Prevents commits if checks fail

## Setup

Make hooks executable:
```bash
chmod +x .claude/hooks/*.sh
```

Link to git hooks (optional):
```bash
ln -s ../../.claude/hooks/pre-commit.sh .git/hooks/pre-commit
```

## Custom Hooks

Create custom hooks for:
- Code formatting
- Documentation generation
- Dependency checks
- Security scanning
- Performance benchmarks

## Hook Types

- **pre-commit**: Before committing changes
- **post-commit**: After successful commit
- **pre-push**: Before pushing to remote
- **post-merge**: After merging branches
