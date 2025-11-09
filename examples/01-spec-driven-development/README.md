# Example 1: Spec-Driven Development

How to build complex features using specifications.

## The Workflow (2-3 Prompts)

### Prompt 1: Write the Spec
```
Write a spec for a PDF reader package that extracts text from PDF files.
Include both full-text and page-by-page extraction functions.
Save it to specs/planned/package-pdf-reader.md
```

**Claude creates:**
- Complete specification following template
- Functional requirements
- API design
- Testing strategy
- Error handling

---

### Prompt 2: Implement the Feature
```
Implement the PDF reader package according to specs/planned/package-pdf-reader.md
```

**Claude automatically:**
- Creates package structure (`packages/pdf-reader/`)
- Implements functions from spec
- Writes comprehensive tests
- Moves spec to `specs/implemented/`
- Updates spec status to ✅ Implemented
- Commits with descriptive message

Done! ✅

---

## Optional: Review Before Implementation

If you want to review the spec first:

```
Prompt 1: Write the spec for [feature]
Prompt 2: Review the spec - is anything missing?
Prompt 3: Implement according to the spec
```

---

## Real Example from This Project

### What We Built: PDF Reader Package

**Prompt 1:**
```
Write a spec for a PDF reader package that can extract text from PDFs.
Save to specs/planned/package-pdf-reader.md
```

**Prompt 2:**
```
Implement specs/planned/package-pdf-reader.md
```

**Result:**
- Package created in `packages/pdf-reader/`
- Functions: `read_pdf()`, `extract_text_by_page()`
- 9 comprehensive tests (including approval tests)
- Spec moved to `specs/implemented/package-pdf-reader.md`
- Git commit with full description

---

## When to Use This Workflow

**Use spec-driven development for:**
- ✅ New packages or libraries
- ✅ Complex features with multiple requirements
- ✅ Public APIs that need review
- ✅ Features with security/performance concerns

**Skip the spec for:**
- ❌ Simple bug fixes
- ❌ Adding a single endpoint
- ❌ Configuration changes
- ❌ Quick experiments

---

## The Spec Template

Claude uses [specs/TEMPLATE.md](../../specs/TEMPLATE.md) which includes:
- Requirements (functional & non-functional)
- API design
- Testing strategy
- Error handling
- Dependencies

You don't need to know the template - Claude handles it!

---

## Tips

**Be specific in Prompt 1:**
```
# Good
Write a spec for a CSV reader that handles different delimiters,
quoted fields, and Unicode. Save to specs/planned/package-csv-reader.md

# Too vague
Write a spec for a CSV reader
```

**Trust Claude in Prompt 2:**
```
# Good
Implement specs/planned/package-csv-reader.md

# Unnecessary detail
Implement the CSV reader. Create packages/csv-reader/ with src/
and tests/ directories. Use pytest for testing. Follow PEP 8...
```

Claude knows to:
- Follow the project structure
- Write tests
- Move the spec when done
- Commit the work

---

## See Also

- [Example 2: Fix Security Issue](../02-fix-security-issue/) - No spec needed
- [Example 3: Add Feature](../03-add-feature/) - Quick features, no spec
- [Example 4: Refactoring](../04-refactoring/) - Improving code quality
- [Spec Naming Convention](../../specs/README.md)
