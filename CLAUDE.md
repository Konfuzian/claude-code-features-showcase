# Claude Code Features Showcase

This repository demonstrates advanced Claude Code capabilities through practical examples and documentation.

## Project Purpose

A comprehensive learning resource and playground for Claude Code features, including:
- Custom commands, skills, and hooks
- MCP server integrations
- Context management strategies
- Workflow patterns and best practices

## Development Guidelines

### Code Quality
- Write clear, self-documenting code
- Follow existing patterns and conventions
- Keep implementations simple and focused
- Add inline comments for complex logic

### Testing
- Run test suite after code changes
- Fix failing tests before committing
- Add tests for new functionality

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
│   ├── agents/               # Specialized subagents
│   └── hooks/                # Event-driven automation
│
├── docs/                      # AI: Documentation for Claude
│   ├── models.md             # Model selection guide
│   ├── file-formats.md       # .md vs .yml guidance
│   ├── workflows.md          # Common patterns
│   └── context-management.md
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
```

## Key Concepts

### Slash Commands
Custom commands that extend Claude Code functionality. Defined as markdown or YAML files in `.claude/commands/`.

### Skills
Reusable capabilities that can be invoked within conversations. Stored in `.claude/skills/`.

### Hooks
Event-driven automation that responds to specific actions (e.g., before commit, after file save).

### MCP Servers
Model Context Protocol servers that provide additional tools and context to Claude.

### Context Management
Strategies for efficient token usage and maintaining relevant context throughout sessions.
