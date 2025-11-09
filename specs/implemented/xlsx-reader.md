# XLSX Reader Specification

**Status**: ✅ Implemented
**Version**: 1.0
**Last Updated**: 2025-11-09

## Overview

Extract data from Excel (.xlsx) workbooks with support for multiple sheets, various data types, and structured output.

## Purpose

Enables Claude Code to read and analyze Excel spreadsheets by extracting data from workbooks and converting them to structured Python data formats.

## Features

### Core Functionality
- Read Excel workbooks (.xlsx format)
- Extract data from all sheets in a workbook
- Handle multiple data types (text, numbers, dates)
- Skip empty rows automatically
- Provide sheet-level metadata (row count, column count)
- Return structured data as dictionaries and lists

### Error Handling
- Validate file existence before processing
- Handle invalid Excel files gracefully
- Provide clear error messages for troubleshooting

## API

### Functions

#### `read_xlsx(file_path: str | Path) -> Dict[str, List[List[Any]]]`
Extracts all data from an Excel file as a dictionary mapping sheet names to their data.

**Parameters:**
- `file_path`: Path to the Excel file (string or Path object)

**Returns:**
- Dictionary where:
  - Keys are sheet names (strings)
  - Values are lists of rows, where each row is a list of cell values

**Raises:**
- `FileNotFoundError`: If the Excel file doesn't exist
- `ValueError`: If the file is not a valid Excel file

**Example:**
```python
from xlsx_reader import read_xlsx

data = read_xlsx("workbook.xlsx")
for sheet_name, rows in data.items():
    print(f"Sheet '{sheet_name}' has {len(rows)} rows")
    print(f"Headers: {rows[0]}")
```

#### `extract_sheets(file_path: str | Path) -> List[Dict[str, Any]]`
Extracts data from an Excel file, organized by sheet with metadata.

**Parameters:**
- `file_path`: Path to the Excel file (string or Path object)

**Returns:**
- List of dictionaries, each containing:
  - `name`: Sheet name
  - `rows`: Number of rows (excluding empty rows)
  - `columns`: Number of columns
  - `data`: List of rows, where each row is a list of cell values

**Raises:**
- `FileNotFoundError`: If the Excel file doesn't exist
- `ValueError`: If the file is not a valid Excel file

**Example:**
```python
from xlsx_reader import extract_sheets

sheets = extract_sheets("workbook.xlsx")
for sheet in sheets:
    print(f"Sheet: {sheet['name']}")
    print(f"Size: {sheet['rows']} rows × {sheet['columns']} columns")
    print(f"First row: {sheet['data'][0]}")
```

## Implementation Details

### Dependencies
- **openpyxl**: Comprehensive Excel file handling library
- **Python**: 3.10+
- **uv**: Package manager

### Module Structure
```
src/xlsx_reader/
├── __init__.py       # Public API exports
└── reader.py         # Core implementation
```

### Design Decisions

**Why openpyxl?**
- Industry standard for Excel file handling in Python
- Supports .xlsx format (modern Excel)
- Read and write capabilities
- Handles formulas, formatting, and data types
- Actively maintained

**Why data_only=True?**
- Returns calculated values instead of formulas
- More useful for data extraction use cases
- Simplifies the output structure

**Why skip empty rows?**
- Reduces noise in the output
- Focuses on actual data
- Easier to process and analyze

**Why two functions?**
- `read_xlsx()`: Simple dictionary structure for direct data access
- `extract_sheets()`: Includes metadata for more advanced use cases

## Claude Code Integration

### Skill Definition
Located at [.claude/skills/xlsx-reader/SKILL.md](.claude/skills/xlsx-reader/SKILL.md)

**Skill Name**: `xlsx-reader`

**When to Use**:
- Reading Excel spreadsheets
- Extracting workbook data
- Analyzing Excel files
- Converting Excel to structured format

**Allowed Tools**: Bash, Read

## Testing

### Test Coverage
- File not found error handling
- Invalid Excel file error handling
- Single sheet workbook reading
- Multiple sheet workbook reading
- Empty row handling
- Various data types (text, numbers, dates)
- Sheet metadata validation
- Data structure validation
- Row and column counting

### Test Location
[tests/test_xlsx_reader.py](tests/test_xlsx_reader.py)

### Test Fixtures
- [tests/fixtures/sample.xlsx](tests/fixtures/sample.xlsx)
  - Contains three sheets: Employees, Projects, Summary
  - Includes various data types and realistic data

### Running Tests
```bash
task test
# or
pytest tests/test_xlsx_reader.py -v
```

## Usage Examples

### From Claude Code Skill
```
User: Read the Excel file at data/sales.xlsx
Claude: [Invokes xlsx-reader skill to extract and display content]
```

### From Python Code
```python
from xlsx_reader import read_xlsx, extract_sheets

# Simple extraction
data = read_xlsx("workbook.xlsx")
employee_data = data["Employees"]
headers = employee_data[0]
employees = employee_data[1:]

# With metadata
sheets = extract_sheets("workbook.xlsx")
for sheet in sheets:
    print(f"\n{sheet['name']}: {sheet['rows']}×{sheet['columns']}")
    if sheet['rows'] > 0:
        print(f"Headers: {sheet['data'][0]}")
```

### Real-World Example
```python
from xlsx_reader import read_xlsx

# Read employee data
data = read_xlsx("employees.xlsx")
employee_rows = data["Employees"]

# Parse headers and data
headers = employee_rows[0]
employees = employee_rows[1:]

# Find specific information
for row in employees:
    employee_dict = dict(zip(headers, row))
    if employee_dict["Department"] == "Engineering":
        print(f"{employee_dict['Name']} - {employee_dict['Role']}")
```

## Supported Data Types

The reader handles these Excel data types:
- **Text**: Strings and formatted text
- **Numbers**: Integers and floats
- **Dates**: Python datetime objects
- **Booleans**: True/False values
- **None**: Empty cells

## Future Enhancements

Potential improvements (not yet implemented):
- Support for .xls (older Excel format)
- Cell formatting extraction (colors, fonts, borders)
- Formula extraction (in addition to calculated values)
- Named range support
- Chart and image extraction
- Header detection and parsing
- Data type inference and validation
- CSV export functionality
- Sheet filtering by name patterns
