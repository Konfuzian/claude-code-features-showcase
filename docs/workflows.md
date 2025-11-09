# Common Workflows

Proven patterns for effective Claude Code usage.

## Feature Development Workflow

### 1. Planning Phase
```
User: Add user authentication feature
Claude: Creates todo list and plans implementation
```

**Best practices:**
- Break down into small tasks
- Use TodoWrite to track progress
- Identify dependencies early

### 2. Implementation Phase
```
- Read existing code to understand patterns
- Write new code following conventions
- Add tests as you go
- Update documentation
```

**Best practices:**
- Commit after each logical step
- Run tests frequently
- Keep changes focused

### 3. Review Phase
```
- Use /analyze command for quality check
- Review test coverage
- Check for security issues
- Verify documentation
```

**Best practices:**
- Run full test suite
- Use code review skill
- Check git diff before committing

## Bug Fix Workflow

### 1. Reproduce
```
- Read error logs/reports
- Identify failing test or create one
- Understand the issue
```

### 2. Fix
```
- Locate problematic code
- Implement fix
- Verify test passes
```

### 3. Validate
```
- Run full test suite
- Check for regressions
- Update related docs
```

## Refactoring Workflow

### 1. Assess
```
User: /analyze
Claude: Identifies improvement opportunities
```

### 2. Plan
```
- Create refactoring checklist
- Identify affected areas
- Plan backwards compatibility
```

### 3. Execute
```
- Refactor incrementally
- Keep tests green
- Commit small changes
- Update documentation
```

### 4. Verify
```
- Run all tests
- Check performance
- Review diff
```

## Code Review Workflow

### 1. Context Gathering
```
- Read changed files
- Understand purpose of changes
- Review related code
```

### 2. Review
```
- Check correctness
- Verify test coverage
- Look for security issues
- Assess performance
- Review documentation
```

### 3. Feedback
```
- Provide specific suggestions
- Include file:line references
- Explain reasoning
- Offer alternatives
```

## Documentation Workflow

### 1. Analyze Code
```
- Read implementation
- Understand purpose and behavior
- Identify public API
```

### 2. Generate Docs
```
- Add inline comments
- Write function/class docs
- Create usage examples
- Document edge cases
```

### 3. Organize
```
- Update README
- Add to docs/ folder
- Link related docs
- Update CHANGELOG
```

## Testing Workflow

### 1. Understand Code
```
- Read implementation
- Identify edge cases
- Note dependencies
```

### 2. Write Tests
```
- Start with happy path
- Add edge cases
- Test error handling
- Mock dependencies
```

### 3. Verify Coverage
```
- Run test suite
- Check coverage report
- Add missing tests
- Refactor tests if needed
```

## Context Management Workflow

### Managing Large Codebases

**Use agents for exploration:**
```
- Use Task tool with Explore agent
- Let agents search and summarize
- Gather context incrementally
```

**Read strategically:**
```
- Start with high-level files (README, package.json)
- Use Grep to find relevant code
- Read only necessary files
```

**Leverage tools:**
```
- Glob for file patterns
- Grep for code search
- Read for specific files
- Task for complex searches
```

### Token Efficiency

**Do:**
- ✓ Use agents for multi-step searches
- ✓ Read files only when needed
- ✓ Use Grep with focused patterns
- ✓ Commit frequently to checkpoint progress

**Don't:**
- ✗ Read entire large files unnecessarily
- ✗ Re-read files already in context
- ✗ Use Bash for file operations
- ✗ Search without focused patterns

## Git Workflow

### Committing

**Good commit:**
```bash
git add specific-files
git commit -m "Add user authentication

- Implement login/logout endpoints
- Add JWT token generation
- Create user session management

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Best practices:**
- Commit after each feature/fix
- Write clear, concise messages
- Stage related changes together
- Run tests before committing

### Pull Requests

**Creating PR:**
```
1. Review all changes
2. Check commit history
3. Create PR with summary
4. Include test plan
```

**PR description template:**
```markdown
## Summary
- Bullet points of changes

## Test Plan
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

🤖 Generated with Claude Code
```

## Model Selection Workflow

### Task Analysis
```
1. Assess complexity
2. Check time sensitivity
3. Consider cost constraints
```

### Model Choice
```
Simple task → Haiku
Standard task → Sonnet
Complex task → Opus
```

### Escalation
```
Start with Haiku
↓ (if insufficient)
Try Sonnet
↓ (if still insufficient)
Use Opus
```

## Multi-Agent Workflow

### Parallel Tasks
```
Run multiple agents simultaneously:
- One for testing
- One for documentation
- One for code search
```

### Sequential Tasks
```
Agent 1: Explore codebase
↓
Agent 2: Implement feature
↓
Agent 3: Generate tests
```

**Best practice:** Use parallel agents when tasks are independent

## Emergency Debugging Workflow

### 1. Gather Context
```
- Read error messages
- Check recent changes
- Review relevant code
```

### 2. Hypothesize
```
- Identify likely causes
- Check similar issues
- Review related systems
```

### 3. Test & Fix
```
- Create reproduction test
- Implement fix
- Verify resolution
- Add regression test
```

### 4. Post-Mortem
```
- Document root cause
- Update docs
- Add monitoring
- Share learnings
```

## Tips for Efficient Workflows

1. **Use slash commands** for common tasks
2. **Create custom skills** for repeated patterns
3. **Set up hooks** for automation
4. **Track with todos** for complex work
5. **Commit frequently** to checkpoint progress
6. **Run tests often** to catch issues early
7. **Read strategically** to manage context
8. **Use appropriate models** for cost/quality balance
