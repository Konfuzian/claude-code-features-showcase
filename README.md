# Claude Code Features Showcase

A repository demonstrating advanced features of Claude Code. Built exclusively with Claude - no other AI coding tools.

## Core Principles

- **Be succinct and concise** - Users want to learn quickly and efficiently
- **Don't repeat yourself** - Keep complexity low by avoiding redundancy
- **Make it simple** - Use clear, straightforward language
- **Describe thoroughly** - This is a learning resource; explain what, why, and how
- **Commit often** - Git commit after every meaningful step with succinct, meaningful messages
- **Test often** - Run test suite after code changes to catch bugs early

## Monorepo Structure

This project is organized as a monorepo with three main areas:

### AI-Focused Documentation
- [.claude/](.claude/) - Claude Code configuration (commands, skills, hooks)
- [docs/](docs/) - Guides for models, workflows, context management
- [specs/](specs/) - Feature specifications (implemented & planned)
- [examples/](examples/) - **Real-world workflow examples** (How to work with Claude on this project)
- [CLAUDE.md](CLAUDE.md) - Project context for Claude

### Applications
- [apps/backend/](apps/backend/) - FastAPI REST API (pure API, no templates)
- [apps/frontend/](apps/frontend/) - Static HTML with Tailwind CSS + Datastar (zero-build)

### Shared Packages
- [packages/](packages/) - Reusable libraries and tools
- [packages/pdf-reader/](packages/pdf-reader/) - PDF text extraction
- [packages/xlsx-reader/](packages/xlsx-reader/) - Excel data extraction

## Key Features

- **Custom Commands** - Slash commands for common tasks (/x-analyze, /x-test, /x-refactor, /x-docs, /x-commit, /x-test-coverage)
- **Skills** - Reusable capabilities (x-code-reviewer, x-test-generator, x-pdf-reader, x-xlsx-reader)
- **Agents** - Specialized subagents (test-coverage-auditor)
- **Hooks** - Automated formatting and validation
- **Spec-Driven Development** - Write specs first, then implement
- **Comprehensive Testing** - pytest with approval tests
- **Monorepo Workflow** - Multiple packages, shared tooling

## Quick Start

### Run Tests
```bash
task test              # Run all 76 tests
task test:pdf          # Run PDF reader tests only
task test:xlsx         # Run XLSX reader tests only
task test:backend      # Run backend API tests only
task test:frontend     # Run frontend HTML validation tests only
```

### Run Applications
```bash
# Backend API
task backend:dev       # Start FastAPI server on port 8000

# Frontend
task frontend:dev      # Serve static HTML on port 8080
```

Visit:
- Frontend: http://localhost:8080
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Learning Resources

### Start Here: [Workflow Examples](examples/)

Learn how to work with Claude on this project through real-world examples:

- **[Spec-Driven Development](examples/01-spec-driven-development/)** - Build complex features (e.g., PDF reader)
- **[Fix Security Issues](examples/02-fix-security-issue/)** - Fix critical bugs (e.g., CORS config)
- **[Add Features](examples/03-add-feature/)** - Quick feature additions (e.g., new endpoints)
- **[Refactoring](examples/04-refactoring/)** - Improve code quality (e.g., remove duplication)

Each example includes step-by-step workflows, prompts, and best practices.
