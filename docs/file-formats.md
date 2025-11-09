# File Format Guide

When to use `.md` (Markdown) vs `.yml` (YAML) for Claude Code configuration.

## Markdown (.md)

**Best for: Content-heavy configurations**

### Characteristics
- Human-readable text format
- Supports rich formatting
- Can include code examples
- Better for longer content
- Easier to read and edit

### Use Cases
- **Slash commands** with detailed instructions
- **Skills** requiring extensive descriptions
- **Documentation** and guides
- **Prompts** with examples and context

### Example: Slash Command
```markdown
---
description: Generate comprehensive tests
model: sonnet
---

Generate tests for the selected code:
- Unit tests for all functions
- Edge case coverage
- Mock dependencies as needed

Example test structure:
\`\`\`javascript
describe('MyFunction', () => {
  it('should handle valid input', () => {
    // test code
  });
});
\`\`\`
```

### Advantages
- ✓ Can include examples and formatting
- ✓ More expressive and readable
- ✓ Supports YAML frontmatter for metadata
- ✓ Easy to document complex workflows

## YAML (.yml)

**Best for: Structured configuration**

### Characteristics
- Structured data format
- Clear hierarchy
- Machine-readable
- Compact and concise
- Type-safe values

### Use Cases
- **Configuration files** with many options
- **Agent definitions** with structured parameters
- **MCP server configs**
- **Settings** and preferences

### Example: Agent Configuration
```yaml
name: test-generator
description: Generate comprehensive test suites
model: sonnet
tools:
  - Read
  - Write
  - Grep
parameters:
  framework: auto-detect
  coverage_threshold: 80
  include_integration_tests: true
```

### Advantages
- ✓ Clear structure for complex configs
- ✓ Easy to parse programmatically
- ✓ Good for key-value pairs
- ✓ Compact for settings

## Decision Matrix

| Scenario | Format | Reason |
|----------|--------|--------|
| Slash command with examples | `.md` | Needs code examples |
| Simple slash command | `.md` | Convention |
| Agent configuration | `.yml` | Structured data |
| MCP server setup | `.yml` | Complex settings |
| Skill with instructions | `.md` | Descriptive content |
| Project settings | `.yml` | Key-value pairs |
| Hook documentation | `.md` | Usage examples |
| Tool configuration | `.yml` | Structured options |

## Hybrid Approach: Markdown with YAML Frontmatter

**Best of both worlds**

```markdown
---
description: Code review assistant
model: sonnet
tags: [review, quality, security]
auto_run: false
---

# Code Review Process

Reviews code for:
- Security vulnerabilities
- Performance issues
- Best practice violations

Provides actionable feedback with file locations.
```

### Benefits
- YAML frontmatter for metadata
- Markdown body for content
- Clean separation of config and instructions
- Standard pattern in Claude Code

## Best Practices

### For Markdown Files
1. Use YAML frontmatter for metadata
2. Include usage examples
3. Format with headers and lists
4. Add code blocks for clarity
5. Keep instructions clear and concise

### For YAML Files
1. Use consistent indentation (2 spaces)
2. Comment complex configurations
3. Group related settings
4. Use quotes for strings with special chars
5. Validate syntax before committing

### General Guidelines
- **Prefer `.md`** for slash commands and skills
- **Use `.yml`** for settings and configs
- **Be consistent** within your project
- **Document** non-obvious choices
- **Validate** files before use

## Examples by Type

### Slash Commands → `.md`
```
.claude/commands/
├── analyze.md
├── test.md
└── refactor.md
```

### Skills → `.md`
```
.claude/skills/
├── code-reviewer.md
└── test-generator.md
```

### Agents → `.yml`
```
.claude/agents/
├── reviewer.yml
└── tester.yml
```

### MCP Servers → `.yml`
```
mcp/
├── filesystem.yml
└── database.yml
```

## Migration

When converting between formats:

**Markdown → YAML**
- Extract frontmatter as top-level keys
- Convert content to `prompt` or `description` field

**YAML → Markdown**
- Move config to frontmatter
- Move prompt/description to body
- Add formatting and examples
