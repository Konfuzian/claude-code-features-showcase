# PDF Reader Specification

**Status**: ✅ Implemented
**Version**: 1.0
**Last Updated**: 2025-11-09

## Overview

Extract text content from PDF files with support for multi-page documents and structured output.

## Purpose

Enables Claude Code to read and analyze PDF documentation, reports, and other PDF content by converting them to text format.

## Features

### Core Functionality
- Extract all text from PDF files in a single string
- Extract text organized by page with metadata
- Preserve document structure during extraction
- Handle multi-page documents
- Provide page-level statistics (character count)

### Error Handling
- Validate file existence before processing
- Handle invalid PDF files gracefully
- Provide clear error messages for troubleshooting

## API

### Functions

#### `read_pdf(file_path: str | Path) -> str`
Extracts all text from a PDF file as a single concatenated string.

**Parameters:**
- `file_path`: Path to the PDF file (string or Path object)

**Returns:**
- String containing all extracted text, with pages separated by double newlines

**Raises:**
- `FileNotFoundError`: If the PDF file doesn't exist
- `ValueError`: If the file is not a valid PDF

**Example:**
```python
from pdf_reader import read_pdf

text = read_pdf("report.pdf")
print(text)
```

#### `extract_text_by_page(file_path: str | Path) -> List[Dict[str, any]]`
Extracts text from a PDF file, organized by page with metadata.

**Parameters:**
- `file_path`: Path to the PDF file (string or Path object)

**Returns:**
- List of dictionaries, each containing:
  - `page`: Page number (1-indexed)
  - `text`: Extracted text content
  - `char_count`: Number of characters on the page

**Raises:**
- `FileNotFoundError`: If the PDF file doesn't exist
- `ValueError`: If the file is not a valid PDF

**Example:**
```python
from pdf_reader import extract_text_by_page

pages = extract_text_by_page("report.pdf")
for page_data in pages:
    print(f"Page {page_data['page']}: {page_data['char_count']} characters")
```

## Implementation Details

### Dependencies
- **pypdf**: Robust PDF parsing library
- **Python**: 3.10+
- **uv**: Package manager

### Module Structure
```
src/pdf_reader/
├── __init__.py       # Public API exports
└── reader.py         # Core implementation
```

### Design Decisions

**Why pypdf?**
- Actively maintained
- Pure Python (no external dependencies)
- Good text extraction capabilities
- Handles various PDF formats

**Why two functions?**
- `read_pdf()`: Simple use case - just get all the text
- `extract_text_by_page()`: Advanced use case - need page-level control and metadata

## Claude Code Integration

### Skill Definition
Located at [.claude/skills/pdf-reader/SKILL.md](.claude/skills/pdf-reader/SKILL.md)

**Skill Name**: `pdf-reader`

**When to Use**:
- Reading PDF documentation
- Extracting text from PDF reports
- Analyzing PDF content
- Converting PDF to text format

**Allowed Tools**: Bash, Read

## Testing

### Test Coverage
- File not found error handling
- Invalid PDF error handling
- Single-page PDF extraction
- Multi-page PDF extraction
- Empty text handling
- Page-by-page extraction with metadata

### Test Location
[tests/test_pdf_reader.py](tests/test_pdf_reader.py)

### Test Fixtures
- [tests/fixtures/sample.pdf](tests/fixtures/sample.pdf)

### Running Tests
```bash
task test
# or
pytest tests/test_pdf_reader.py -v
```

## Usage Examples

### From Claude Code Skill
```
User: Read the PDF file at docs/specification.pdf
Claude: [Invokes pdf-reader skill to extract and display content]
```

### From Python Code
```python
from pdf_reader import read_pdf, extract_text_by_page

# Simple extraction
full_text = read_pdf("document.pdf")

# Page-by-page with metadata
pages = extract_text_by_page("document.pdf")
for page in pages:
    if page['char_count'] > 1000:
        print(f"Page {page['page']} has substantial content")
```

## Future Enhancements

Potential improvements (not yet implemented):
- Support for extracting images from PDFs
- Support for extracting tables with structure preservation
- Support for password-protected PDFs
- Metadata extraction (author, title, creation date)
- OCR integration for scanned PDFs
- Page range selection (e.g., pages 5-10)
