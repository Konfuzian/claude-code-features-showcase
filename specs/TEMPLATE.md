# [Feature Name]

**Status:** 📋 Planned | 🚧 In Progress | ✅ Implemented
**Type:** Package | Application | Feature | Integration | Infrastructure
**Created:** YYYY-MM-DD
**Implemented:** YYYY-MM-DD *(if implemented)*
**Version:** X.Y.Z *(if implemented)*
**Location:** `path/to/implementation` *(if implemented)*

---

## Overview

### What
Brief description of what this feature is (1-2 sentences).

### Why
Explain why this feature is needed. What problem does it solve?

### Who
Who is this feature for? (End users, developers, both?)

---

## Requirements

### Functional Requirements

- **FR1:** [First functional requirement]
- **FR2:** [Second functional requirement]
- **FR3:** [Third functional requirement]

### Non-Functional Requirements

- **NFR1:** [Performance requirement]
- **NFR2:** [Security requirement]
- **NFR3:** [Usability requirement]
- **NFR4:** [Maintainability requirement]

### Constraints

- **C1:** [Technical constraint]
- **C2:** [Business constraint]
- **C3:** [Timeline constraint]

---

## Design

### API Design

For packages, describe the public API:

```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief description of what this function does.

    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2

    Returns:
        Description of return value

    Raises:
        ExceptionType: When this exception is raised
    """
```

For applications, describe endpoints:

```
GET /api/endpoint
POST /api/endpoint
PUT /api/endpoint/{id}
DELETE /api/endpoint/{id}
```

### Data Models

Describe any data structures, database schemas, or DTOs:

```python
class ModelName:
    field1: Type1
    field2: Type2
    field3: Type3
```

### Architecture Decisions

- **AD1:** [Key architectural decision and rationale]
- **AD2:** [Another key decision]

---

## Implementation

### Dependencies

List all dependencies:

```toml
[dependencies]
package-name = ">=X.Y.Z"
another-package = ">=A.B.C"
```

### File Structure

Describe the file/directory structure:

```
path/to/implementation/
├── __init__.py
├── module1.py
├── module2.py
└── tests/
    ├── test_module1.py
    └── test_module2.py
```

### Key Components

- **Component 1:** Description of first component
- **Component 2:** Description of second component
- **Component 3:** Description of third component

### Configuration

Any configuration needed:

```python
# Environment variables
API_KEY = "..."
DATABASE_URL = "..."

# Config file
config = {
    "setting1": "value1",
    "setting2": "value2",
}
```

---

## Testing

### Test Strategy

- **Unit Tests:** What needs unit testing
- **Integration Tests:** What needs integration testing
- **End-to-End Tests:** What needs E2E testing

### Test Cases

#### Test Case 1: [Description]
- **Given:** Initial condition
- **When:** Action performed
- **Then:** Expected result

#### Test Case 2: [Description]
- **Given:** Initial condition
- **When:** Action performed
- **Then:** Expected result

### Edge Cases

- **Edge Case 1:** [Description and how to handle]
- **Edge Case 2:** [Description and how to handle]

### Acceptance Criteria

- [ ] All functional requirements met
- [ ] All non-functional requirements met
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Code review passed

---

## Error Handling

### Error Scenarios

| Scenario | Error Type | Error Message | HTTP Code (if API) |
|----------|------------|---------------|-------------------|
| [Scenario 1] | ValueError | "..." | 400 |
| [Scenario 2] | FileNotFoundError | "..." | 404 |
| [Scenario 3] | PermissionError | "..." | 403 |

### Recovery Strategies

- **Scenario 1:** How to recover or fallback
- **Scenario 2:** How to recover or fallback

---

## Performance

### Performance Requirements

- **Latency:** < X ms for Y operation
- **Throughput:** > X requests/second
- **Memory:** < X MB memory usage
- **CPU:** < X% CPU usage

### Optimization Strategies

- **Strategy 1:** [Description]
- **Strategy 2:** [Description]

---

## Security

### Security Considerations

- **Input Validation:** How inputs are validated
- **Authentication:** How users are authenticated (if applicable)
- **Authorization:** How access is controlled (if applicable)
- **Data Protection:** How sensitive data is protected
- **Attack Prevention:** Protection against common attacks (SQL injection, XSS, etc.)

### Threat Model

- **Threat 1:** [Description and mitigation]
- **Threat 2:** [Description and mitigation]

---

## Documentation

### User Documentation

What documentation needs to be written for end users:
- README
- User guide
- API documentation

### Developer Documentation

What documentation needs to be written for developers:
- Code comments
- Architecture documentation
- Contributing guide

### Examples

Provide usage examples:

```python
# Example 1: Basic usage
result = function_name(param1, param2)

# Example 2: Advanced usage
result = function_name(
    param1=value1,
    param2=value2,
)
```

---

## Migration

*(If this spec involves changes to existing functionality)*

### Migration Strategy

- **Step 1:** [Migration step]
- **Step 2:** [Migration step]

### Backwards Compatibility

- Is this backwards compatible?
- If not, what breaks and how to migrate?

### Deprecation Plan

- What gets deprecated?
- When does it get removed?
- Migration timeline

---

## Rollout Plan

### Phase 1: Development
- [ ] Implement core functionality
- [ ] Write tests
- [ ] Code review

### Phase 2: Testing
- [ ] Integration testing
- [ ] Performance testing
- [ ] Security review

### Phase 3: Deployment
- [ ] Deploy to staging
- [ ] User acceptance testing
- [ ] Deploy to production

### Rollback Plan

If something goes wrong:
1. [Rollback step 1]
2. [Rollback step 2]

---

## Open Questions

- **Q1:** [Question that needs to be answered]
- **Q2:** [Another question]

---

## References

- [Related Spec 1](./other-spec.md)
- [External Documentation](https://example.com)
- [Design Inspiration](https://example.com)

---

## Changelog

### YYYY-MM-DD
- Initial spec created

### YYYY-MM-DD
- Updated based on review feedback
- Added [new section/requirement]

### YYYY-MM-DD
- Implemented and moved to implemented/
- Updated status to ✅ Implemented
