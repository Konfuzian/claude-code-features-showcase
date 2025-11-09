# Claude Code Features Showcase

This repository demonstrates advanced Claude Code capabilities through practical examples and documentation.

## Project Purpose

A comprehensive learning resource and playground for Claude Code features, including:
- Custom commands, skills, and hooks
- MCP server integrations
- Context management strategies
- Workflow patterns and best practices

## Development Guidelines

### Python & Dependencies
- **ALWAYS use `uv` for running Python commands** - never use `python`, `python3`, or `pip` directly
- Examples:
  - ✅ `uv run pytest`
  - ✅ `uv run python script.py`
  - ✅ `uv sync` to install dependencies
  - ❌ `python3 -m pytest`
  - ❌ `pip install package`

### Code Quality
- Write clear, self-documenting code
- Follow existing patterns and conventions
- Keep implementations simple and focused
- Add inline comments for complex logic

### Testing
- Run test suite after code changes: `task test`
- Fix failing tests before committing
- Add tests for new functionality
- Use sanity checks for basic browser tests: `task test:sanity`
- Use comprehensive E2E tests for thorough testing: `task test:e2e`

### Git Workflow
- Commit after each meaningful step
- Write succinct, descriptive commit messages
- Keep commits atomic and focused

### Documentation
- Explain what each feature does
- Provide usage examples
- Document why certain approaches are used
- Keep docs concise and scannable

## Project Structure

This is a **monorepo** organized into AI-focused docs, applications, and shared packages:

```
.
├── CLAUDE.md                  # This file - project context
├── README.md                  # User-facing documentation
├── CHANGELOG.md               # Project history
│
├── .claude/                   # AI: Claude Code configuration
│   ├── commands/             # Custom slash commands
│   ├── skills/               # Reusable skills
│   ├── agents/               # Specialized agents
│   └── hooks/                # Event-driven automation
│
├── docs/                      # AI: Documentation for Claude
│   ├── models.md             # Model selection guide
│   ├── file-formats.md       # .md vs .yml guidance
│   ├── workflows.md          # Common patterns
│   ├── context-management.md # Token efficiency strategies
│   └── code-style.md         # Code style & guidelines
│
├── specs/                     # AI: Feature specifications
│   ├── implemented/          # Completed features
│   └── planned/              # Future features
│
├── apps/                      # Applications (deployable)
│   ├── backend/              # Example: API server
│   └── frontend/             # Example: Web UI
│
├── packages/                  # Shared libraries & tools
│   ├── pdf-reader/           # PDF text extraction
│   └── xlsx-reader/          # Excel data extraction
│
└── examples/                  # Working examples
    ├── usage-guides/         # Feature usage documentation
    ├── 01-spec-driven-development/
    ├── 02-fix-security-issue/
    ├── 03-add-feature/
    └── 04-refactoring/
```

## Key Concepts

### Slash Commands
Custom commands that extend Claude Code functionality. Defined as markdown or YAML files in [.claude/commands/](.claude/commands/).

**Available commands:**
- [/x-analyze](.claude/commands/x-analyze.md) - Code quality analysis
- [/x-test](.claude/commands/x-test.md) - Generate tests
- [/x-docs](.claude/commands/x-docs.md) - Generate documentation
- [/x-refactor](.claude/commands/x-refactor.md) - Refactor code
- [/x-test-coverage](.claude/commands/x-test-coverage.md) - Coverage analysis
- [/x-commit](.claude/commands/x-commit.md) - Auto-commit

[→ Usage guides](examples/usage-guides/commands/)

### Skills
Reusable capabilities that can be invoked within conversations. Stored in [.claude/skills/](.claude/skills/).

**Available skills:**
- [x-pdf-reader](.claude/skills/x-pdf-reader/) - Extract text from PDFs
- [x-xlsx-reader](.claude/skills/x-xlsx-reader/) - Read Excel files
- [x-code-reviewer](.claude/skills/x-code-reviewer/) - Comprehensive code reviews
- [x-test-generator](.claude/skills/x-test-generator/) - Generate test suites

[→ Usage guides](examples/usage-guides/skills/)

### Hooks
Event-driven automation that responds to specific actions. Configured in [.claude/hooks.json](.claude/hooks.json).

**Available hooks:**
- [Pre-commit hook](.claude/hooks/pre-commit.sh) - Validates TODOs, markdown, whitespace
- [Format hook](.claude/hooks/format-file.sh) - Auto-formats Python, Markdown, JSON, YAML

[→ Hook documentation](.claude/hooks/README.md) | [→ Usage guides](examples/usage-guides/hooks/)

### Agents
Specialized agents for complex autonomous tasks. Stored in [.claude/agents/](.claude/agents/).

**Available agents:**
- [test-coverage-auditor](.claude/agents/test-coverage-auditor.md) - Comprehensive coverage analysis

### MCP Servers
Model Context Protocol servers that provide additional tools and context to Claude.

(MCP server integration can be configured via Claude Code settings)

### Context Management
Strategies for efficient token usage and maintaining relevant context throughout sessions.

[→ Context management guide](docs/context-management.md)

---

## Quick Reference

### Documentation
- [Code Style Guide](docs/code-style.md) - Conventions and best practices
- [Workflows](docs/workflows.md) - Common development patterns
- [Model Selection](docs/models.md) - Choosing the right model
- [File Formats](docs/file-formats.md) - When to use .md vs .yml
- [Context Management](docs/context-management.md) - Token efficiency

### Examples
- [Usage Guides](examples/usage-guides/) - How to use commands, skills, hooks
- [Workflow Examples](examples/) - Real-world development scenarios
- [Specifications](specs/) - Feature specs (implemented & planned)

### Configuration
- [Commands](.claude/commands/) - Custom slash commands
- [Skills](.claude/skills/) - Reusable capabilities
- [Hooks](.claude/hooks/) - Event-driven automation
- [Agents](.claude/agents/) - Specialized subagents
