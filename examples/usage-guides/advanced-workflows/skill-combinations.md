# Skill Combinations

Multiple skills working together automatically.

## Common Combinations

**PDF + Tests:**
"Read test-plan.pdf and generate tests" → x-pdf-reader + x-test-generator

**Excel + Review:**
"Check code against security.xlsx" → x-xlsx-reader + x-code-reviewer

**Multi-source:**
"Validate against spec.pdf and data.xlsx" → All skills work together

## Example
```
"Read API spec from docs.pdf and implement it"

1. x-pdf-reader extracts requirements
2. Claude implements
3. x-code-reviewer validates
4. x-test-generator creates tests
```
