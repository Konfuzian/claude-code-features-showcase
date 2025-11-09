# Example 4: Refactoring

How to improve code quality without changing behavior.

## The Workflow (1-2 Prompts)

### Prompt 1: Identify Issues
```
/analyze
```

**Claude finds:**
- Code duplication in [pdf_reader/reader.py](../../packages/pdf-reader/src/pdf_reader/reader.py) and [xlsx_reader/reader.py](../../packages/xlsx-reader/src/xlsx_reader/reader.py)
- Same file validation repeated in multiple functions

---

### Prompt 2: Refactor
```
Refactor the PDF reader to extract file validation into a helper function.
Make sure tests still pass.
```

**Claude automatically:**
- Extracts duplicated logic into `_validate_pdf_path()` helper
- Updates all functions to use the helper
- Runs tests to ensure no behavior changed
- Commits the refactoring

Done! ✅

---

## The Refactoring

**Before (Duplicated):**
```python
def read_pdf(file_path: str | Path) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    # ... rest

def extract_text_by_page(file_path: str | Path) -> List[Dict[str, Any]]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    # ... rest
```

**After (DRY):**
```python
def _validate_pdf_path(file_path: str | Path) -> Path:
    """Validate that PDF file exists."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    return path

def read_pdf(file_path: str | Path) -> str:
    path = _validate_pdf_path(file_path)
    # ... rest

def extract_text_by_page(file_path: str | Path) -> List[Dict[str, Any]]:
    path = _validate_pdf_path(file_path)
    # ... rest
```

---

## Common Refactoring Patterns

**Extract function:**
```
Extract the calculation logic in process_data() into a calculate_value() helper
```

**Extract constant:**
```
Replace magic numbers in validate_age() with named constants
```

**Simplify conditional:**
```
Refactor the nested conditionals in get_discount() using a dictionary
```

**Improve naming:**
```
Improve variable and function names in [file] to be more descriptive
```

**Add type hints:**
```
Add comprehensive type hints to [file]
```

---

## When to Refactor

**Good times:**
- ✅ After `/analyze` identifies issues
- ✅ When tests are all passing
- ✅ Before adding new features to messy code
- ✅ When you notice duplication

**Bad times:**
- ❌ When tests are failing
- ❌ When you don't understand the code
- ❌ Without tests in place

---

## Important Rules

1. **Small steps** - One refactoring at a time
2. **Test between changes** - Run `task test` after each change
3. **Keep commits atomic** - One type of refactoring per commit
4. **Don't change behavior** - Tests must still pass

---

## See Also

- [Example 1: Spec-Driven Development](../01-spec-driven-development/) - Complex features
- [Example 2: Fix Security Issue](../02-fix-security-issue/) - Bug fixes
- [Example 3: Add Feature](../03-add-feature/) - Quick features
