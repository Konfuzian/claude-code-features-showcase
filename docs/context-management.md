# Context Management

Strategies for efficient token usage and maintaining relevant context in Claude Code.

## Understanding Context

### Token Budget
- **Total available**: 200,000 tokens
- **System prompt**: ~2-12k tokens
- **Messages**: Accumulates over conversation
- **Free space**: Remaining for your work
- **Auto-compact buffer**: 22.5% reserved

### Context Composition
```
System prompt + Tools + Messages = Used tokens
200k - Used tokens = Available tokens
```

## Token Usage Strategies

### 1. Read Strategically

**Do:**
```javascript
// Read specific files you need
Read("src/auth/login.js")
Read("src/auth/session.js")
```

**Don't:**
```javascript
// Read entire directories unnecessarily
Read("src/**/*.js")  // Wasteful
```

### 2. Use Agents for Exploration

**Instead of:**
```
Read file1, file2, file3...
Grep pattern1, pattern2...
Read more files...
```

**Do:**
```
Task(Explore, "Find authentication implementation")
// Agent searches and returns summary
```

**Benefits:**
- Agent context is isolated
- Only results returned to main context
- More efficient token usage

### 3. Targeted Searching

**Efficient Grep:**
```javascript
// Specific pattern with file type
Grep("authenticate", {type: "js"})

// With glob filter
Grep("login", {glob: "src/auth/**/*.js"})
```

**Inefficient:**
```javascript
// Too broad
Grep("user")  // Returns too many results
```

### 4. Incremental Reading

**Start broad, get specific:**
```
1. Read README.md (project overview)
2. Read package.json (dependencies/scripts)
3. Grep for specific functionality
4. Read only relevant files
```

## Context Management Patterns

### Pattern 1: Top-Down Exploration

```
README.md → Understanding project
    ↓
package.json → Understanding structure
    ↓
Key entry files → Understanding architecture
    ↓
Specific modules → Implementation details
```

### Pattern 2: Feature-Focused

```
Grep for feature name
    ↓
Read top 2-3 matches
    ↓
Understand implementation
    ↓
Make changes
```

### Pattern 3: Agent-Assisted

```
Task(Explore, "How does X work?")
    ↓
Review agent summary
    ↓
Read specific files if needed
    ↓
Implement changes
```

## Tool Selection for Context Efficiency

### File Discovery

**Use Glob for patterns:**
```javascript
Glob("**/*test*.js")  // Find test files
Glob("src/components/**/*.tsx")  // Find React components
```

**Not Bash:**
```bash
# Avoid: ls -la src/**/*.js
# Use Glob instead
```

### Content Search

**Use Grep for code search:**
```javascript
Grep("class UserAuth", {type: "py"})
```

**Not Bash:**
```bash
# Avoid: grep -r "class" src/
# Use Grep tool instead
```

### File Reading

**Use Read:**
```javascript
Read("src/main.js")
```

**Not Bash:**
```bash
# Avoid: cat src/main.js
# Use Read tool instead
```

## Monitoring Context Usage

### Check Context
```
Use /context command to see:
- Total tokens used
- Breakdown by category
- Free space available
- Auto-compact buffer
```

### Warning Signs
- Context usage > 70%: Consider wrapping up or starting new conversation
- Free space < 50k: Be selective about new reads
- Many tool results: Consider using agents

## Context-Saving Techniques

### 1. Commit Frequently
```
Benefits:
- Checkpoints your progress
- Clears working memory
- Enables fresh start if needed
```

### 2. Use Agent Isolation
```
Task tool creates isolated context
Agent returns only summary
Main context stays lean
```

### 3. Be Selective
```
Only read files you need
Use head_limit with Grep
Read specific line ranges when possible
```

### 4. Batch Operations
```
// Efficient: Single Read
Read("config.js", {offset: 100, limit: 50})

// Inefficient: Multiple Reads
Read entire file just for one function
```

## Large Codebase Strategies

### Strategy 1: Architecture First
```
1. Read architectural docs
2. Understand high-level structure
3. Use agents to explore modules
4. Read only necessary implementation files
```

### Strategy 2: Grep-Then-Read
```
1. Grep for functionality
2. Review match count and files
3. Read most relevant 2-3 files
4. Grep again for specifics if needed
```

### Strategy 3: Iterative Deepening
```
Level 1: README, package.json
Level 2: Main entry points
Level 3: Module of interest
Level 4: Specific functions
```

## Anti-Patterns to Avoid

### ❌ Reading Everything
```javascript
// Don't do this
Read("src/file1.js")
Read("src/file2.js")
Read("src/file3.js")
// ... 20 more files
```

### ❌ Re-reading Files
```javascript
// File already in context
Read("config.js")  // First time - OK
// ... later ...
Read("config.js")  // Again - wasteful
```

### ❌ Using Bash for File Ops
```bash
# Inefficient
cat file.js
grep "pattern" *.js
find . -name "*.js"

# Use dedicated tools instead
Read("file.js")
Grep("pattern", {type: "js"})
Glob("**/*.js")
```

### ❌ Broad Searches
```javascript
// Too broad - many results
Grep("user")

// Better - specific
Grep("class UserAuth")
```

## Best Practices Summary

### Do:
1. ✓ Use Task/Explore for open-ended searches
2. ✓ Read strategically, not exhaustively
3. ✓ Use Grep with filters (type, glob)
4. ✓ Commit frequently to checkpoint
5. ✓ Monitor context with /context
6. ✓ Use appropriate tools for each job
7. ✓ Start broad, narrow down

### Don't:
1. ✗ Read files unnecessarily
2. ✗ Re-read files already in context
3. ✗ Use Bash for file operations
4. ✗ Run overly broad searches
5. ✗ Ignore context warnings
6. ✗ Read entire files for small info
7. ✗ Explore without direction

## Example: Efficient Feature Addition

```
Task: Add logging to authentication module

Efficient approach:
1. Grep("authenticate", {glob: "src/**/*.js"})
   → Found in: auth/login.js, auth/session.js
2. Read("auth/login.js")
   → Understand implementation
3. Add logging to login.js
4. Read("auth/session.js")
   → Understand session handling
5. Add logging to session.js
6. Commit changes

Total files read: 2
Token usage: Minimal
```

## Recovery Strategies

### When Context is Full

**Option 1: Commit and Continue**
```
1. Commit current work
2. Note what's left to do
3. Continue in same conversation
```

**Option 2: Start Fresh**
```
1. Commit current work
2. Start new conversation
3. Provide brief context of what was done
```

**Option 3: Use Agents**
```
1. Offload searches to agents
2. Get summaries only
3. Continue with reduced context
```

## Context Hygiene

### Regular Maintenance
- Commit after each feature/fix
- Start new conversations for new features
- Use agents for exploratory work
- Monitor context regularly

### Conversation Boundaries
- New major feature → New conversation
- Bug fix in progress → Same conversation
- Research/exploration → Use agents
- Quick changes → Same conversation

## Advanced Techniques

### Parallel Agents
```
Run multiple agents in parallel:
- Each has isolated context
- Results merged back
- Efficient for independent tasks
```

### Strategic Checkpoints
```
Every 3-5 file reads:
- Assess if more reading needed
- Consider using agent instead
- Check context usage
```

### Lazy Loading
```
Don't read until you need to modify
Use Grep to identify files first
Read only when implementing
```

## Measuring Efficiency

### Good Indicators
- Files read: < 10 per feature
- Context usage: < 70% for most tasks
- Agent usage: For complex searches
- Commits: Frequent and focused

### Warning Signs
- Reading > 20 files for simple feature
- Context > 80% early in task
- Re-reading same files
- No agents used for large codebase

## Tools Summary

| Task | Tool | Why |
|------|------|-----|
| Find files | Glob | Fast pattern matching |
| Search code | Grep | Efficient content search |
| Read file | Read | Direct file access |
| Explore codebase | Task(Explore) | Isolated context |
| Complex search | Task(Explore) | Multi-step with isolation |
| File operations | Specialized tools | Not Bash |
| Monitor usage | /context | Track token usage |
