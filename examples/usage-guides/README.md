# Usage Guides

Comprehensive guides for using Claude Code features: commands, skills, hooks, and advanced workflows.

## Quick Navigation

### 📋 Commands
Slash commands you invoke directly:

- [/x-analyze](./commands/x-analyze.md) - Code quality and security analysis
- [/x-test](./commands/x-test.md) - Generate comprehensive test suites
- [/x-docs](./commands/x-docs.md) - Generate documentation
- [/x-refactor](./commands/x-refactor.md) - Refactor for quality and maintainability
- [/x-test-coverage](./commands/x-test-coverage.md) - Analyze test coverage
- [/x-commit](./commands/x-commit.md) - Create meaningful git commits

### 🤖 Skills
Capabilities Claude invokes automatically:

- [x-pdf-reader](./skills/x-pdf-reader.md) - Extract text from PDF files
- [x-xlsx-reader](./skills/x-xlsx-reader.md) - Read Excel workbooks
- [x-code-reviewer](./skills/x-code-reviewer.md) - Comprehensive code reviews
- [x-test-generator](./skills/x-test-generator.md) - Generate test suites

### 🔗 Hooks
Event-driven automation:

- [Pre-commit Hook](./hooks/pre-commit-hook.md) - Validate code before commits
- [Format Hook](./hooks/format-hook.md) - Auto-format on file edits

### 🚀 Advanced Workflows
Combining features for powerful workflows:

- [Command Chaining](./advanced-workflows/command-chaining.md) - Chain commands effectively
- [Skill Combinations](./advanced-workflows/skill-combinations.md) - Combine skills for complex tasks

## Understanding the Differences

### Commands vs Skills

**Commands** (`/x-*`)
- You invoke them explicitly
- Start with `/x-`
- Action-oriented (verbs)
- Examples: `/x-analyze`, `/x-test`, `/x-commit`

**Skills** (`x-*`)
- Claude invokes automatically based on context
- No slash prefix
- Role/capability-oriented (nouns)
- Examples: `x-pdf-reader`, `x-code-reviewer`

**Example:**
```
You: "Please analyze this code for issues"
→ You're asking for the /x-analyze command

You: "Read the specification from spec.pdf"
→ Claude automatically uses x-pdf-reader skill
```

### Hooks vs Commands

**Hooks**
- Triggered by events (file edit, pre-commit, etc.)
- Run automatically
- No explicit invocation
- Examples: Format hook runs after Edit tool

**Commands**
- Triggered by explicit user request
- Must be invoked
- Examples: `/x-commit`

## Learning Paths

### Beginner Path

1. **Start with basic commands**
   - [/x-commit](./commands/x-commit.md) - Learn automated committing
   - [/x-test](./commands/x-test.md) - Generate simple tests

2. **Experience skills passively**
   - Ask Claude to read a PDF → `x-pdf-reader` invoked automatically
   - Skills work behind the scenes

3. **Notice hooks in action**
   - Edit a Python file → Format hook auto-formats it
   - Commit code → Pre-commit hook validates it

### Intermediate Path

1. **Combine commands**
   - [Command Chaining](./advanced-workflows/command-chaining.md)
   - `/x-analyze` → fix issues → `/x-test` → `/x-commit`

2. **Leverage skills actively**
   - [Skill Combinations](./advanced-workflows/skill-combinations.md)
   - Read PDF spec → Generate code → Review with x-code-reviewer

3. **Customize hooks**
   - [Pre-commit Hook](./hooks/pre-commit-hook.md) - Add custom checks
   - [Format Hook](./hooks/format-hook.md) - Configure formatters

### Advanced Path

1. **Create workflows**
   - Multi-step command chains
   - Complex skill combinations
   - See [Advanced Workflows](./advanced-workflows/)

2. **Build custom commands**
   - Create your own slash commands
   - Automate repetitive workflows
   - See `.claude/commands/` for examples

3. **Extend with agents**
   - Use specialized agents for complex tasks
   - See `.claude/agents/` for examples

## Common Scenarios

### Scenario: Adding a New Feature

```
1. Implement the feature
   → Code the functionality

2. /x-analyze
   → Check for issues

3. Fix any problems found

4. /x-test
   → Generate comprehensive tests

5. npm test
   → Verify tests pass

6. /x-docs
   → Document the feature

7. /x-commit
   → Commit everything
```

See: [Command Chaining](./advanced-workflows/command-chaining.md)

### Scenario: Working with Documentation

```
User: "Read the API spec from api-spec.pdf and implement the endpoints"

1. x-pdf-reader skill extracts requirements
2. Claude implements endpoints
3. /x-test generates tests
4. /x-docs creates API documentation
5. /x-commit commits implementation
```

See: [x-pdf-reader](./skills/x-pdf-reader.md), [Skill Combinations](./advanced-workflows/skill-combinations.md)

### Scenario: Code Review

```
User: "Review this authentication code for security issues"

1. x-code-reviewer skill performs comprehensive review
2. Identifies security vulnerabilities
3. Claude fixes issues
4. /x-test generates security tests
5. /x-commit commits fixes
```

See: [x-code-reviewer](./skills/x-code-reviewer.md)

### Scenario: Improving Test Coverage

```
1. /x-test-coverage
   → Identifies gaps: auth.js at 45%

2. /x-test
   "Generate tests for uncovered paths in auth.js"

3. npm test
   → Verify new tests pass

4. /x-test-coverage
   → Verify improvement: auth.js now at 87%

5. /x-commit
```

See: [/x-test-coverage](./commands/x-test-coverage.md)

## Tips & Best Practices

### Commands

✅ **DO:**
- Use commands when you need specific actions
- Chain commands for complete workflows
- Let commands automate repetitive tasks

❌ **DON'T:**
- Skip verification steps (always run tests!)
- Commit without analysis
- Bypass hook warnings

### Skills

✅ **DO:**
- Let Claude choose skills automatically
- Provide clear context for what you need
- Trust skills to work in the background

❌ **DON'T:**
- Manually specify skills (Claude knows when to use them)
- Assume skills can handle all file types (check capabilities)

### Hooks

✅ **DO:**
- Configure hooks for your project's needs
- Review hook outputs and fix issues
- Keep hooks fast and focused

❌ **DON'T:**
- Use `--no-verify` to bypass hooks
- Make hooks too complex or slow
- Ignore hook warnings

### Workflows

✅ **DO:**
- Start simple, add complexity as needed
- Verify each step before proceeding
- Document your team's standard workflows

❌ **DON'T:**
- Skip steps to save time
- Assume commands always succeed
- Forget to run tests before committing

## Getting Help

### For Commands
Check individual command guides in [./commands/](./commands/)

### For Skills
Check individual skill guides in [./skills/](./skills/)

### For Hooks
Check hook guides in [./hooks/](./hooks/)

### For Workflows
Check workflow examples in [./advanced-workflows/](./advanced-workflows/)

### For Everything Else
- Main documentation: [../README.md](../README.md)
- Project docs: [../../docs/](../../docs/)
- Workflow examples: [../../examples/](../../)

## Contributing

Found an issue or want to add examples? See the project's contribution guidelines.

## Next Steps

1. **Try a command:** Start with [/x-commit](./commands/x-commit.md)
2. **Experience a skill:** Ask Claude to read a PDF file
3. **See a hook:** Edit a Python file and watch it auto-format
4. **Build a workflow:** Follow [Command Chaining](./advanced-workflows/command-chaining.md)

Happy coding! 🚀
