# Example 4: Refactoring Code

This example demonstrates how to refactor code to improve quality, maintainability, and performance.

## Scenario

The `/analyze` command identified code duplication in the PDF and XLSX readers. Let's refactor to follow DRY principles.

## When to Refactor

**Good times to refactor:**
- After `/analyze` identifies issues
- When you notice code duplication
- Before adding new features to messy code
- When tests are all passing (safety net)
- When you understand the code well

**Bad times to refactor:**
- When tests are failing
- When you don't understand the code
- When under time pressure (unless it's blocking you)
- Without tests in place

---

## Refactoring Workflow

```
1. Identify the Problem
2. Ensure Tests Pass
3. Make the Change
4. Verify Tests Still Pass
5. Commit
```

---

## Example: Remove Code Duplication

### Step 1: Identify Duplication

**Prompt to Claude:**
```
/analyze
```

**Claude finds:**
```
Code Quality Issue: Duplicate File Validation
Files: pdf_reader/reader.py (lines 23-26, 56-59)
       xlsx_reader/reader.py (lines 23-26, 62-65)

The same file existence check is duplicated across multiple functions.
```

---

### Step 2: Ensure Tests Pass

**Before refactoring, verify everything works:**

```bash
task test
```

**All 91 tests should pass ✓**

---

### Step 3: Plan the Refactoring

**Prompt to Claude:**
```
Refactor the PDF reader to extract the file validation logic into a helper function.
The helper should:
- Take file_path as input
- Validate the file exists
- Return a Path object
- Have a clear name like _validate_pdf_path()

Make sure all tests still pass after the change.
```

---

### Step 4: Implement Refactoring

**Claude creates helper function:**

```python
# Before - Duplicated in every function
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

```python
# After - Single helper function
def _validate_pdf_path(file_path: str | Path) -> Path:
    """
    Validate that PDF file exists.

    Args:
        file_path: Path to the PDF file

    Returns:
        Resolved Path object

    Raises:
        FileNotFoundError: If file doesn't exist
    """
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

### Step 5: Run Tests

**After refactoring:**

```bash
task test:pdf
```

**Expected:** All tests still pass ✓

If tests fail, the refactoring broke something - investigate and fix!

---

### Step 6: Commit

**Prompt to Claude:**
```
/commit
```

**Claude creates:**
```
refactor: Extract file validation to helper function in PDF reader

Reduce code duplication by extracting file existence check into
a dedicated helper function.

Changes:
- Add _validate_pdf_path() helper function
- Update read_pdf() to use helper
- Update extract_text_by_page() to use helper
- No functional changes, all tests pass

Benefits:
- Reduces duplication
- Easier to maintain validation logic
- Single source of truth for file validation

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Common Refactoring Patterns

### Pattern 1: Extract Function

**Before:**
```python
def process_data(data):
    # 50 lines of complex logic
    result = []
    for item in data:
        # Complex calculation
        value = item * 2 + 10
        if value > 100:
            value = value / 2
        result.append(value)
    return result
```

**Prompt:**
```
Extract the calculation logic into a separate function called calculate_value()
```

**After:**
```python
def calculate_value(item: int) -> float:
    """Calculate processed value for a single item."""
    value = item * 2 + 10
    if value > 100:
        value = value / 2
    return value


def process_data(data: List[int]) -> List[float]:
    """Process list of data items."""
    return [calculate_value(item) for item in data]
```

---

### Pattern 2: Extract Constant

**Before:**
```python
def validate_age(age):
    if age < 0 or age > 150:
        raise ValueError("Invalid age")
```

**Prompt:**
```
Extract the magic numbers into named constants
```

**After:**
```python
MIN_AGE = 0
MAX_AGE = 150


def validate_age(age: int) -> None:
    if age < MIN_AGE or age > MAX_AGE:
        raise ValueError(
            f"Invalid age: {age}. Must be between {MIN_AGE} and {MAX_AGE}"
        )
```

---

### Pattern 3: Simplify Conditional

**Before:**
```python
def get_discount(customer_type, amount):
    if customer_type == "gold":
        if amount > 1000:
            return amount * 0.20
        else:
            return amount * 0.15
    elif customer_type == "silver":
        if amount > 1000:
            return amount * 0.10
        else:
            return amount * 0.05
    else:
        return 0
```

**Prompt:**
```
Refactor the nested conditionals into a clearer structure using a dictionary
```

**After:**
```python
DISCOUNT_RATES = {
    ("gold", True): 0.20,  # amount > 1000
    ("gold", False): 0.15,
    ("silver", True): 0.10,
    ("silver", False): 0.05,
}


def get_discount(customer_type: str, amount: float) -> float:
    is_large_order = amount > 1000
    rate = DISCOUNT_RATES.get((customer_type, is_large_order), 0.0)
    return amount * rate
```

---

### Pattern 4: Improve Naming

**Before:**
```python
def proc(d):
    r = []
    for x in d:
        if x > 0:
            r.append(x * 2)
    return r
```

**Prompt:**
```
Improve the variable and function names to be more descriptive
```

**After:**
```python
def get_doubled_positive_values(numbers: List[int]) -> List[int]:
    """Return doubled values for all positive numbers in the list."""
    doubled_positives = []
    for number in numbers:
        if number > 0:
            doubled_positives.append(number * 2)
    return doubled_positives
```

Or even better:
```python
def get_doubled_positive_values(numbers: List[int]) -> List[int]:
    """Return doubled values for all positive numbers in the list."""
    return [number * 2 for number in numbers if number > 0]
```

---

### Pattern 5: Replace Type Code with Class

**Before:**
```python
STATUS_DRAFT = 0
STATUS_PUBLISHED = 1
STATUS_ARCHIVED = 2

def get_status_name(status):
    if status == STATUS_DRAFT:
        return "Draft"
    elif status == STATUS_PUBLISHED:
        return "Published"
    elif status == STATUS_ARCHIVED:
        return "Archived"
```

**Prompt:**
```
Replace the status codes with an Enum class
```

**After:**
```python
from enum import Enum


class ArticleStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

    @property
    def display_name(self) -> str:
        return self.value.capitalize()


# Usage
status = ArticleStatus.PUBLISHED
print(status.display_name)  # "Published"
```

---

## Refactoring Best Practices

### 1. Small Steps
Refactor one thing at a time. Don't try to fix everything at once.

**Bad:**
```
Refactor the entire codebase to use dependency injection,
add logging, improve error handling, and extract all magic numbers
```

**Good:**
```
Extract the database connection logic into a separate module
```

### 2. Test Between Changes
Run tests after each refactoring step.

```bash
# After each small change
task test
```

### 3. Keep Commits Atomic
One refactoring type per commit.

**Good commits:**
- "refactor: Extract validation helper"
- "refactor: Rename variables for clarity"
- "refactor: Replace magic numbers with constants"

**Bad commit:**
- "refactor: Fix everything"

### 4. Use `/analyze` to Find Issues

```
/analyze
```

Let Claude identify code smells and suggest refactorings.

### 5. Don't Change Behavior
Refactoring should NOT change what the code does, only HOW it does it.

**Refactoring:** Improving code structure
**New Feature:** Changing behavior

---

## Refactoring Checklist

Before refactoring:
- [ ] All tests pass
- [ ] You understand the code
- [ ] You have time to do it properly

During refactoring:
- [ ] Make small, incremental changes
- [ ] Run tests after each change
- [ ] Keep commits atomic

After refactoring:
- [ ] All tests still pass
- [ ] Code is more readable
- [ ] No behavior changes
- [ ] Commit with clear message

---

## Example Prompts

### Find Refactoring Opportunities
```
/analyze
Look for code that could be refactored for better maintainability
```

### Extract Function
```
In [file], extract the [description] logic into a separate function
```

### Simplify
```
Simplify the conditional logic in [function] in [file]
```

### Improve Names
```
Improve the variable and function names in [file] to be more descriptive
```

### Remove Duplication
```
I see the same [pattern] in [file1] and [file2].
Extract this into a shared helper function.
```

### Add Type Hints
```
Add comprehensive type hints to [file]
```

---

## When Refactoring Goes Wrong

### Tests Start Failing

**Stop and debug:**
1. What test is failing?
2. What did you just change?
3. Revert the last change
4. Try a smaller change

### Code Gets More Complex

**Stop and reconsider:**
- Maybe the refactoring approach is wrong
- Ask Claude for a different approach
- Sometimes the original code was actually better

### You Break Something

**Git is your friend:**
```bash
# See what changed
git diff

# Revert specific file
git restore [file]

# Revert everything
git restore .
```

---

## See Also

- [Example 1: Spec-Driven Development](../01-spec-driven-development/)
- [Example 2: Fix Security Issue](../02-fix-security-issue/)
- [Example 3: Add Feature](../03-add-feature/)
- [Refactoring Workflows](../../docs/workflows.md#refactoring)
