# Hooks

Event-driven automation that responds to specific actions in your development workflow.

## Available Hooks

### Git Hooks

**[pre-commit.sh](pre-commit.sh)** - Pre-commit validation
- Checks for TODO/FIXME comments
- Validates markdown files (if markdownlint installed)
- Checks for trailing whitespace
- Prevents commits if checks fail

See [pre-commit-hook.md](pre-commit-hook.md) for details.

### Claude Code Hooks

**[format-file.sh](format-file.sh)** - Automatic formatting after edits
- Triggered by PostToolUse events (Edit/Write)
- Auto-formats Python files with ruff
- Auto-formats Markdown, JSON, YAML with prettier
- Configured via [hooks.json](hooks.json)

See [format-hook.md](format-hook.md) for details.

## Hook Types

### Git Hooks
Traditional git hooks that run during git operations:
- **pre-commit**: Before committing changes
- **post-commit**: After successful commit
- **pre-push**: Before pushing to remote
- **post-merge**: After merging branches

### Claude Code Hooks
Hooks that integrate with Claude Code events:
- **PostToolUse**: After tool use (Edit, Write, etc.)
- **PreToolUse**: Before tool use
- **UserPromptSubmit**: When user submits a prompt

## Setup

### Git Hooks
Make hooks executable:
```bash
chmod +x .claude/hooks/*.sh
```

Link to git hooks (optional):
```bash
ln -s ../../.claude/hooks/pre-commit.sh .git/hooks/pre-commit
```

### Claude Code Hooks
Hooks are automatically configured via [hooks.json](hooks.json). No additional setup required.
