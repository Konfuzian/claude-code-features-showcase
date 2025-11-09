# PDF Reader Skill

Extracts and analyzes text content from PDF files.

## Capabilities

- Extracts text from PDF files
- Preserves document structure
- Handles multi-page PDFs
- Provides page-by-page content
- Summarizes PDF contents

## Usage

Invoke this skill when you need to:
- Read PDF documentation
- Extract text from PDF reports
- Analyze PDF content
- Convert PDF to text format

## Implementation

Uses Python with pypdf library for robust PDF parsing.

## Example

```
User: Read the PDF file at tests/fixtures/sample.pdf
Claude: [Uses pdf-reader skill to extract and display content]
```

## Requirements

- Python 3.10+
- pypdf library
- Managed via uv package manager
