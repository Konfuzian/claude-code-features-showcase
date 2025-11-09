# Example 1: Spec-Driven Development

This example demonstrates the spec-driven development workflow used in this project.

## Scenario

We want to add a new feature: **PDF Reader Package** that extracts text from PDF files.

## Workflow Overview

```
1. Write Specification
2. Review & Refine Spec
3. Implement Feature
4. Write Tests
5. Verify & Commit
```

## Step-by-Step Process

### Step 1: Write the Specification

**Prompt to Claude:**
```
Write a specification for a PDF reader package that can:
- Extract all text from a PDF file
- Extract text page-by-page with metadata
- Handle errors gracefully
- Be testable

Put the spec in specs/planned/pdf-reader.md
```

**Claude creates:** `specs/planned/pdf-reader.md`

**Spec Content:**
```markdown
# PDF Reader Package

## Overview
Python package for extracting text from PDF files.

## Requirements

### Functional
- FR1: Extract all text from multi-page PDFs
- FR2: Extract text per page with metadata
- FR3: Support both str and Path inputs

### Non-Functional
- NFR1: Handle missing files gracefully
- NFR2: Handle corrupted PDFs gracefully
- NFR3: Provide clear error messages

## API Design

### read_pdf(file_path: str | Path) -> str
Extract all text from PDF.

### extract_text_by_page(file_path: str | Path) -> List[Dict[str, Any]]
Extract text with page metadata.

## Dependencies
- pypdf>=4.0.0

## Testing Strategy
- Unit tests for both functions
- Error handling tests
- Approval tests for consistency
```

---

### Step 2: Review & Refine

**Prompt to Claude:**
```
Review the PDF reader spec. Is anything missing?
Should we add any additional features or considerations?
```

Claude might suggest:
- Empty page handling
- Performance considerations for large files
- Character encoding handling

Update the spec based on feedback.

---

### Step 3: Implement the Feature

**Prompt to Claude:**
```
Implement the PDF reader package according to specs/planned/pdf-reader.md

Create:
- packages/pdf-reader/src/pdf_reader/reader.py
- packages/pdf-reader/pyproject.toml
- Follow the existing package structure
```

**Claude creates:**

`packages/pdf-reader/src/pdf_reader/reader.py`:
```python
from pathlib import Path
from typing import List, Dict, Any
from pypdf import PdfReader


def read_pdf(file_path: str | Path) -> str:
    """Extract all text from a PDF file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    try:
        reader = PdfReader(path)
        text_parts = []

        for page in reader.pages:
            text = page.extract_text()
            if text.strip():
                text_parts.append(text)

        return "\n\n".join(text_parts)
    except Exception as e:
        raise ValueError(f"Failed to read PDF: {e}") from e


def extract_text_by_page(file_path: str | Path) -> List[Dict[str, Any]]:
    """Extract text from PDF with page-by-page metadata."""
    # ... implementation
```

`packages/pdf-reader/pyproject.toml`:
```toml
[project]
name = "pdf-reader"
version = "0.1.0"
dependencies = ["pypdf>=4.0.0"]

[dependency-groups]
dev = ["pytest>=8.0.0", "approvaltests>=15.0.0"]
```

---

### Step 4: Write Tests

**Prompt to Claude:**
```
Write comprehensive tests for the PDF reader package.
Include:
- Happy path tests
- Error handling tests
- Approval tests
- Edge cases (empty PDFs, corrupted files, etc.)

Put tests in packages/pdf-reader/tests/test_pdf_reader.py
```

**Claude creates tests:**

```python
import pytest
from pathlib import Path
from pdf_reader.reader import read_pdf, extract_text_by_page


class TestReadPdf:
    """Tests for read_pdf function."""

    def test_read_pdf_extracts_all_text(self):
        """Test that read_pdf extracts text from all pages."""
        text = read_pdf("fixtures/sample.pdf")
        assert len(text) > 0
        assert isinstance(text, str)

    def test_read_pdf_file_not_found(self):
        """Test that FileNotFoundError is raised for missing files."""
        with pytest.raises(FileNotFoundError):
            read_pdf("nonexistent.pdf")

    # ... more tests
```

---

### Step 5: Run Tests & Verify

**Prompt to Claude:**
```
Run the PDF reader tests and fix any issues
```

**Commands Claude runs:**
```bash
task test:pdf
```

**If tests fail**, Claude fixes the issues and reruns.

---

### Step 6: Move Spec to Implemented

**Prompt to Claude:**
```
The PDF reader is complete and tested.
Move the spec from planned/ to implemented/ and mark it as implemented.
```

**Claude moves file:**
```bash
git mv specs/planned/pdf-reader.md specs/implemented/pdf-reader.md
```

**Updates spec header:**
```markdown
# PDF Reader Package

**Status:** ✅ Implemented
**Version:** 0.1.0
**Location:** packages/pdf-reader/
```

---

### Step 7: Commit

**Prompt to Claude:**
```
/commit
```

**Or manually:**
```
Commit the PDF reader package implementation
```

**Claude creates commit:**
```
feat: Implement PDF reader package

Add PDF text extraction package with comprehensive tests.

Changes:
- Add packages/pdf-reader/ with read_pdf() and extract_text_by_page()
- Implement error handling for missing/corrupted files
- Add 9 comprehensive tests with approval testing
- Move spec from planned/ to implemented/

Implements spec: specs/implemented/pdf-reader.md

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Key Principles

### 1. Spec First, Code Second
Always write the specification before implementation. This ensures:
- Clear requirements
- Agreed-upon API design
- Test criteria defined upfront
- Documentation before coding

### 2. Iterative Refinement
Don't expect the first spec to be perfect:
- Write initial spec
- Review with Claude
- Refine based on feedback
- Update as you discover edge cases

### 3. Test-Driven Implementation
Write tests that match the spec:
- Test happy paths
- Test error conditions
- Test edge cases
- Use approval tests for consistency

### 4. Small, Focused Commits
Each commit should represent one complete feature:
- Spec + Implementation + Tests
- Move spec to implemented/
- Update documentation

### 5. Document the Journey
Move completed specs to `implemented/` and update their status.

---

## Common Patterns

### Pattern 1: New Package
```
1. Write spec in specs/planned/
2. Create package structure (src/, tests/, pyproject.toml)
3. Implement core functionality
4. Write comprehensive tests
5. Move spec to specs/implemented/
6. Commit
```

### Pattern 2: New Feature in Existing Package
```
1. Write spec in specs/planned/
2. Update existing package
3. Add tests for new feature
4. Update package documentation
5. Move spec to specs/implemented/
6. Commit
```

### Pattern 3: API Changes
```
1. Write spec describing the change
2. Update implementation
3. Update ALL tests (ensure backwards compatibility or migration)
4. Update documentation
5. Move spec to specs/implemented/
6. Commit with breaking change notice if needed
```

---

## Example Prompts

### Starting a New Feature
```
I want to add a CSV reader package that can parse CSV files
and return structured data. Write a spec for this in specs/planned/csv-reader.md
```

### Implementing from Spec
```
Implement the CSV reader package according to specs/planned/csv-reader.md
Follow the same structure as the PDF and XLSX readers.
```

### Testing
```
Write comprehensive tests for the CSV reader.
Include edge cases like:
- Empty files
- Different delimiters
- Quoted fields with commas
- Unicode content
```

### Refinement
```
The CSV reader spec needs to handle these additional cases:
- TSV files (tab-separated)
- Custom delimiters
- Header row detection

Update the spec and implementation.
```

---

## Benefits of This Workflow

✅ **Clear Requirements** - Spec defines what success looks like
✅ **Better Design** - Thinking before coding leads to better APIs
✅ **Documentation** - Spec becomes the documentation
✅ **Testability** - Test criteria defined in advance
✅ **Communication** - Spec can be reviewed before coding
✅ **Historical Record** - Specs show why decisions were made

---

## Anti-Patterns to Avoid

❌ **Code First, Spec Later** - Leads to unclear requirements
❌ **Vague Specs** - "Make it work" isn't a spec
❌ **Skipping Tests** - Tests are part of the spec deliverable
❌ **Not Moving Specs** - Keep implemented specs in implemented/
❌ **Massive Specs** - Break large features into smaller specs

---

## See Also

- [Spec Template](../../specs/TEMPLATE.md)
- [Workflows Documentation](../../docs/workflows.md)
- [Other Examples](../)
