# Model Selection Guide

Choosing the right Claude model for your task optimizes cost, speed, and quality.

## Available Models

### Sonnet 4.5 (claude-sonnet-4-5)
**Best for: Most tasks, balanced performance**

- **Strengths**: Best overall balance of speed, cost, and intelligence
- **Use cases**:
  - General coding tasks
  - Code reviews
  - Documentation
  - Refactoring
  - Bug fixing
- **Cost**: Medium
- **Speed**: Fast

### Haiku (claude-haiku)
**Best for: Quick, simple tasks**

- **Strengths**: Fastest, most cost-effective
- **Use cases**:
  - Simple code generation
  - Quick searches
  - File organization
  - Basic formatting
  - Simple documentation
- **Cost**: Low
- **Speed**: Very fast

### Opus (claude-opus)
**Best for: Complex, mission-critical tasks**

- **Strengths**: Highest intelligence and capability
- **Use cases**:
  - Complex architecture design
  - Critical security reviews
  - Complex refactoring
  - Novel algorithm development
  - Production incident debugging
- **Cost**: High
- **Speed**: Slower

## Decision Matrix

| Task Complexity | Recommended Model | Why |
|----------------|-------------------|-----|
| Fix typo | Haiku | Simple, fast |
| Add feature | Sonnet | Balanced complexity |
| Refactor module | Sonnet | Standard work |
| Design system architecture | Opus | High complexity |
| Review PR | Sonnet | Thorough but efficient |
| Generate tests | Sonnet | Requires good coverage |
| Debug production issue | Opus | Critical, complex |
| Format code | Haiku | Simple transformation |

## Cost Optimization Tips

1. **Start with Haiku** for simple tasks, escalate if needed
2. **Use Sonnet as default** for most coding work
3. **Reserve Opus** for complex or critical situations
4. **Batch simple tasks** to use Haiku efficiently
5. **Break complex tasks** into smaller pieces for Sonnet

## Performance Characteristics

### Context Window
- All models: 200K tokens
- Use context efficiently regardless of model

### Response Quality
- Haiku: Good for straightforward tasks
- Sonnet: Excellent for most coding tasks
- Opus: Best for complex reasoning

### Latency
- Haiku: ~1-2s typical response time
- Sonnet: ~2-4s typical response time
- Opus: ~4-8s typical response time

## Configuration

Specify model in agent tasks:
```yaml
model: haiku  # or sonnet, opus
```

In slash commands:
```yaml
---
description: Quick code format
model: haiku
---
```

## Best Practices

- **Default to Sonnet** - best all-around choice
- **Use Haiku** for speed-critical operations
- **Use Opus** when accuracy is paramount
- **Monitor costs** and adjust model usage
- **Test with Haiku** first, upgrade if quality insufficient
