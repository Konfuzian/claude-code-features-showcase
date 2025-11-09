# Working with Claude Code - Examples

This directory contains real-world examples of how to work with Claude Code on this project.

## Overview

Each example demonstrates a different workflow pattern:

| Example | Scenario | Use When |
|---------|----------|----------|
| [01 - Spec-Driven Development](./01-spec-driven-development/) | Add PDF reader package | Building complex features |
| [02 - Fix Security Issue](./02-fix-security-issue/) | Fix CORS configuration | Fixing bugs or security issues |
| [03 - Add Feature](./03-add-feature/) | Add `/api/version` endpoint | Adding simple features quickly |
| [04 - Refactoring](./04-refactoring/) | Remove code duplication | Improving code quality |

---

## Quick Decision Guide

### "I want to add a new feature..."

**Is it complex?** (Multiple requirements, needs design review, long-term maintenance)
→ [Example 1: Spec-Driven Development](./01-spec-driven-development/)

**Is it simple?** (Single clear requirement, straightforward implementation)
→ [Example 3: Add Feature](./03-add-feature/)

---

### "I need to fix something..."

**Is it a bug or security issue?**
→ [Example 2: Fix Security Issue](./02-fix-security-issue/)

**Is the code working but messy?**
→ [Example 4: Refactoring](./04-refactoring/)

---

## Common Workflows

### 1. Spec-Driven Development (Complex Features)

**When:** New packages, major features, API changes

**Steps:**
1. Write specification in `specs/planned/`
2. Review and refine the spec
3. Implement according to spec
4. Write comprehensive tests
5. Move spec to `specs/implemented/`
6. Commit

**Example Prompt:**
```
Write a spec for a CSV reader package that can parse CSV files
and handle different delimiters. Put it in specs/planned/csv-reader.md
```

→ [See Full Example](./01-spec-driven-development/)

---

### 2. Quick Feature Addition (Simple Changes)

**When:** Simple endpoints, configuration changes, small utilities

**Steps:**
1. Describe what you want
2. Implement
3. Test
4. Commit

**Example Prompt:**
```
Add a GET /api/version endpoint that returns app version,
Python version, and FastAPI version.
```

→ [See Full Example](./03-add-feature/)

---

### 3. Bug/Security Fix (Problems)

**When:** Security issues, bugs, errors

**Steps:**
1. Identify issue (via `/analyze` or manually)
2. Understand the fix
3. Implement the fix
4. Test thoroughly
5. Verify with `/analyze`
6. Commit

**Example Prompt:**
```
/analyze
```
Then:
```
Fix the CORS configuration issue identified by the analysis.
Use environment variables for allowed origins.
```

→ [See Full Example](./02-fix-security-issue/)

---

### 4. Refactoring (Improve Code Quality)

**When:** Code duplication, complex conditionals, poor naming

**Steps:**
1. Ensure all tests pass
2. Make small refactoring change
3. Verify tests still pass
4. Commit
5. Repeat

**Example Prompt:**
```
Extract the file validation logic in PDF reader into a helper function
to reduce duplication.
```

→ [See Full Example](./04-refactoring/)

---

## Useful Commands

### Slash Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/x-analyze` | Code quality analysis | Before refactoring, periodic reviews |
| `/x-test` | Generate tests | After implementing features |
| `/x-refactor` | Code refactoring | When code works but is messy |
| `/x-docs` | Generate documentation | For public APIs and complex code |
| `/x-commit` | Auto-generate commit | After completing any work |
| `/x-test-coverage` | Coverage analysis | To identify testing gaps |

### Task Commands

```bash
# Testing
task test              # Run all tests
task test:pdf          # Run PDF reader tests
task test:xlsx         # Run XLSX reader tests
task test:backend      # Run backend tests
task test:frontend     # Run frontend tests

# Development
task backend:dev       # Start backend server
task frontend:dev      # Serve static frontend
```

---

## Best Practices

### ✅ DO

- **Test before committing** - Always run tests
- **Use `/analyze` regularly** - Find issues early
- **Small, focused commits** - One logical change per commit
- **Write specs for complex features** - Saves time in the long run
- **Ask Claude to explain** - "Explain what this code does"
- **Use `/commit` for consistency** - Automated commit messages

### ❌ DON'T

- **Skip tests** - Tests are your safety net
- **Make huge changes** - Small incremental changes are safer
- **Ignore warnings from `/analyze`** - Security issues compound
- **Write specs for everything** - Simple changes don't need specs
- **Commit without understanding** - Review Claude's code
- **Forget to update documentation** - Keep README in sync

---

## Example Prompt Templates

### Starting a New Feature

**Complex (needs spec):**
```
Write a specification for [feature description].
Include functional requirements, API design, error handling,
and testing strategy. Put it in specs/planned/[name].md
```

**Simple (no spec):**
```
Add [feature description] to [file].
It should [what it does].
```

### Fixing Issues

**After `/analyze`:**
```
Fix the [issue name] identified in the analysis.
[Additional requirements or constraints]
```

**Known bug:**
```
Fix the bug in [file] where [description of bug].
The expected behavior is [correct behavior].
```

### Refactoring

**General:**
```
Refactor [file/function] to [improvement goal].
Make sure all tests still pass.
```

**Specific pattern:**
```
In [file], extract the [duplicated code description]
into a helper function called [name].
```

### Testing

**Add tests:**
```
Write comprehensive tests for [feature/file].
Include happy path, error cases, and edge cases.
```

**Fix failing test:**
```
The test [test name] is failing.
Debug and fix the issue.
```

---

## Development Workflow

### Daily Workflow

1. **Start of day:**
   ```
   git pull
   task test  # Verify everything works
   ```

2. **During development:**
   - Make changes
   - Run relevant tests frequently
   - Commit after each complete unit of work

3. **Before committing:**
   ```
   task test  # Run all tests
   /analyze   # Check for new issues (periodically)
   /commit    # Generate commit message
   ```

4. **End of day:**
   ```
   git push   # Push your commits
   ```

### Weekly Workflow

- **Code review:** Use `/analyze` to audit code quality
- **Refactoring:** Address accumulated technical debt
- **Documentation:** Update READMEs and specs
- **Testing:** Review test coverage

---

## Troubleshooting

### "Tests are failing"

1. Read the error message carefully
2. Ask Claude: `The test [name] is failing with error [error]. Help me debug this.`
3. Check recent changes: `git diff`
4. Revert if needed: `git restore [file]`

### "Claude's code doesn't work"

1. Run the code and capture the error
2. Ask: `This code produces error [error]. Fix it.`
3. If still broken, be more specific about what you need

### "I don't know what command to use"

- For complex features: Write a spec first
- For simple changes: Just describe what you want
- For analysis: Use `/analyze`
- For fixes: Describe the problem

### "The commit message isn't what I want"

1. Use `/commit` for automated messages
2. Or write manual commit: `git commit -m "your message"`
3. Amend last commit: `git commit --amend`

---

## Learning Path

### Beginner

1. Start with [Example 3: Add Feature](./03-add-feature/)
2. Try adding a simple endpoint or configuration
3. Use `/commit` to commit your work

### Intermediate

1. Work through [Example 1: Spec-Driven Development](./01-spec-driven-development/)
2. Create a small package with a spec
3. Use `/analyze` to check your code

### Advanced

1. Study [Example 2: Fix Security Issue](./02-fix-security-issue/)
2. Use `/analyze` to find real issues in your code
3. Practice [Example 4: Refactoring](./04-refactoring/)
4. Refactor based on analysis results

---

## Usage Guides

For detailed guides on using individual features:

📚 **[Browse All Usage Guides →](./usage-guides/)**

Quick links:
- **Commands:** [/x-analyze](./usage-guides/commands/x-analyze.md) • [/x-test](./usage-guides/commands/x-test.md) • [/x-docs](./usage-guides/commands/x-docs.md) • [/x-refactor](./usage-guides/commands/x-refactor.md) • [/x-test-coverage](./usage-guides/commands/x-test-coverage.md) • [/x-commit](./usage-guides/commands/x-commit.md)
- **Skills:** [x-pdf-reader](./usage-guides/skills/x-pdf-reader.md) • [x-xlsx-reader](./usage-guides/skills/x-xlsx-reader.md) • [x-code-reviewer](./usage-guides/skills/x-code-reviewer.md) • [x-test-generator](./usage-guides/skills/x-test-generator.md)
- **Hooks:** [Pre-commit Hook](./usage-guides/hooks/pre-commit-hook.md) • [Format Hook](./usage-guides/hooks/format-hook.md)
- **Advanced:** [Command Chaining](./usage-guides/advanced-workflows/command-chaining.md) • [Skill Combinations](./usage-guides/advanced-workflows/skill-combinations.md)

---

## Additional Resources

- [Project Documentation](../docs/)
  - [Workflows](../docs/workflows.md)
  - [Model Selection](../docs/models.md)
  - [Context Management](../docs/context-management.md)
- [Specifications](../specs/)
  - [Implemented Features](../specs/implemented/)
  - [Planned Features](../specs/planned/)
- [Custom Commands](../.claude/commands/)
- [Skills](../.claude/skills/)

---

## Contributing Examples

Have a workflow pattern that isn't covered? Add it!

1. Create a new directory: `examples/05-your-pattern/`
2. Write a comprehensive README.md
3. Include code samples (before/after if applicable)
4. Update this index
5. Submit a PR

---

## Questions?

- Check the [main README](../README.md)
- Review the [documentation](../docs/)
- Ask Claude: "How do I [what you want to do]?"

---

Happy coding with Claude! 🤖
