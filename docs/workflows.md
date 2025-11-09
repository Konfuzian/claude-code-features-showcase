# Common Workflows

Proven patterns for effective Claude Code usage.

## Feature Development Workflow (Spec-Driven)

This project follows a **spec-driven development workflow** where specifications are written before implementation.

### 1. Write the Specification
**Location:** `specs/planned/feature-name.md`

```markdown
# Feature Name Specification

**Status**: 📝 Planned
**Version**: 1.0
**Last Updated**: YYYY-MM-DD

## Overview
Brief description of what the feature does

## Purpose
Why this feature exists and what problems it solves

## Features
### Core Functionality
- List of key capabilities

### Error Handling
- How errors are handled

## API
Document the intended API surface

## Implementation Details
### Dependencies
List required libraries and tools

### Design Decisions
Explain key architectural choices

## Testing
What needs to be tested

## Usage Examples
Show how it will be used

## Future Enhancements
Ideas for later improvements
```

**Best practices:**
- Write specs in `specs/planned/` first
- Include API design and examples
- Document why decisions are made
- Keep specs concise but thorough
- Use TodoWrite to track spec writing

### 2. Implement the Code
**Location:** `src/feature_name/`

```
- Read the spec to understand requirements
- Read existing code to understand patterns
- Write implementation following conventions
- Keep code simple and focused
- Add inline comments for complex logic
```

**Best practices:**
- Follow the spec's API design
- Implement one function/method at a time
- Commit after each logical step
- Keep changes focused and atomic

### 3. Write Tests
**Location:** `tests/test_feature_name.py`

```
- Test all functions/methods from the spec
- Cover happy path cases
- Cover error cases
- Test edge cases
- Use fixtures for test data
```

**Best practices:**
- Run tests after each implementation step
- Aim for comprehensive coverage
- Use descriptive test names
- Keep tests simple and readable

### 4. Verify & Document
```
- Run full test suite
- Verify all spec requirements are met
- Move spec from planned/ to implemented/
- Update spec status to ✅ Implemented
- Update CHANGELOG.md
- Commit the completed feature
```

**Best practices:**
- Use `/analyze` for quality check
- Use code review skill
- Check git diff before committing
- Write clear commit message

### Example End-to-End Flow

```
User: Add JSON file reader feature

1. Write spec:
   - Create specs/planned/json-reader.md
   - Document API: read_json(), parse_json()
   - Include usage examples
   - Commit: "Add JSON reader specification"

2. Implement code:
   - Create src/json_reader/__init__.py
   - Create src/json_reader/reader.py
   - Implement read_json() function
   - Commit: "Implement JSON reader core functionality"

3. Write tests:
   - Create tests/test_json_reader.py
   - Add happy path tests
   - Add error handling tests
   - Create test fixtures
   - Run: task test
   - Commit: "Add JSON reader tests"

4. Finalize:
   - Move specs/planned/json-reader.md → specs/implemented/
   - Update status to ✅ Implemented
   - Update CHANGELOG.md
   - Run full test suite
   - Commit: "Complete JSON reader feature"
```

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

See [Context Management Guide](context-management.md) for comprehensive strategies.

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
