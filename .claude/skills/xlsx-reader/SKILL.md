---
name: xlsx-reader
description: Reads Excel workbooks (.xlsx), extracts data from all sheets, handles multiple data types (text, numbers, dates), and returns structured data. Uses Python with openpyxl library. Use when reading Excel spreadsheets, extracting workbook data, analyzing Excel files, or converting Excel to structured format.
allowed-tools: [Bash, Read]
---

# XLSX Reader Skill

Reads and extracts data from Excel (.xlsx) files.

## Capabilities

- Reads Excel workbooks
- Extracts data from all sheets
- Provides sheet-by-sheet access
- Handles multiple data types (text, numbers, dates)
- Returns structured data as dictionaries or lists

## Usage

Invoke this skill when you need to:
- Read Excel spreadsheets
- Extract data from workbooks
- Analyze Excel data
- Convert Excel to structured format

## Implementation

Uses Python with openpyxl library for robust Excel parsing.

## Example

```
User: Read the Excel file at tests/fixtures/sample.xlsx
Claude: [Uses xlsx-reader skill to extract and display content]
```

## Requirements

- Python 3.10+
- openpyxl library
- Managed via uv package manager
