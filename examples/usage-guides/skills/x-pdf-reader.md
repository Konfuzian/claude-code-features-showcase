# Using x-pdf-reader Skill

## What It Does

Extracts text from PDF files with:
- Multi-page document handling
- Structure preservation (headings, paragraphs)
- Page-by-page content extraction
- Text cleanup and formatting

Uses Python with the `pypdf` library.

## When to Use

- Reading PDF documentation
- Extracting text from PDF reports
- Analyzing PDF content
- Converting PDF to text format
- Processing forms and invoices

## How to Invoke

Skills are invoked automatically by Claude based on context. Simply ask Claude to work with PDFs:

```
Can you read the API documentation from docs/api-reference.pdf?
```

```
Please extract all the data from the invoice.pdf file
```

```
Summarize the contents of the technical-spec.pdf
```

## Example 1: Reading Documentation

### Request
```
Please read the user guide from docs/user-guide.pdf and summarize the authentication section
```

### What Happens
1. Claude invokes the `x-pdf-reader` skill
2. Skill runs Python script to extract PDF text
3. Text is parsed page by page
4. Claude analyzes the content and provides summary

### Response
```
📄 Reading PDF: docs/user-guide.pdf

Extracted 15 pages successfully.

=== Authentication Section Summary ===

The user guide covers three authentication methods:

1. **API Key Authentication** (Pages 3-4)
   - Generate API key from dashboard
   - Include in Authorization header: `Bearer YOUR_API_KEY`
   - Keys can be rotated without downtime

2. **OAuth 2.0** (Pages 5-7)
   - Supports authorization code flow
   - Redirect URIs must be whitelisted
   - Access tokens expire after 1 hour
   - Refresh tokens valid for 30 days

3. **JWT Tokens** (Pages 8-9)
   - Self-contained authentication
   - Signature verification required
   - Custom claims supported

Key requirements:
- All requests must use HTTPS
- Rate limiting: 1000 requests/hour
- Invalid tokens return 401 Unauthorized
```

## Example 2: Extracting Structured Data

### Request
```
Extract all the product prices from catalog.pdf
```

### Response
```
📄 Reading PDF: catalog.pdf

Found product pricing information:

Page 2:
- Widget Pro: $49.99
- Widget Enterprise: $99.99

Page 3:
- Gadget Basic: $29.99
- Gadget Plus: $59.99
- Gadget Premium: $89.99

Page 5:
- Service Plan Monthly: $19.99/mo
- Service Plan Annual: $199.99/yr (save 17%)

Total: 7 products found
```

## Example 3: Processing Forms

### Request
```
Read the job application from applications/john-doe.pdf and extract the candidate information
```

### Response
```
📄 Reading PDF: applications/john-doe.pdf

=== Candidate Information ===

Personal Details:
- Name: John Doe
- Email: john.doe@email.com
- Phone: (555) 123-4567
- Location: San Francisco, CA

Position Applied: Senior Software Engineer

Experience:
- 8 years in software development
- 5 years with Python, JavaScript
- 3 years team lead experience

Education:
- BS Computer Science, Stanford University (2015)

Notable Projects (from page 2):
- Led migration of monolith to microservices
- Reduced API response time by 60%
- Implemented CI/CD pipeline reducing deploy time from 2hrs to 15min
```

## Example 4: Multi-Document Analysis

### Request
```
Compare the requirements in spec-v1.pdf and spec-v2.pdf and tell me what changed
```

### Response
```
📄 Reading PDF: spec-v1.pdf
Extracted 8 pages.

📄 Reading PDF: spec-v2.pdf
Extracted 12 pages.

=== Changes from v1 to v2 ===

NEW REQUIREMENTS:
1. Authentication now requires 2FA (Section 3.2, v2)
2. Added real-time notifications via WebSocket (Section 5.1, v2)
3. Support for file uploads up to 100MB (Section 4.3, v2)

MODIFIED REQUIREMENTS:
1. API rate limit increased from 100/hr to 1000/hr (Section 2.1)
2. Session timeout reduced from 24hrs to 2hrs (Section 3.1)

REMOVED REQUIREMENTS:
1. RSS feed support discontinued (was Section 6.2 in v1)

The spec also expanded from 8 to 12 pages, with new sections covering:
- Section 7: Mobile App Requirements (new)
- Section 8: Analytics Integration (new)
```

## Supported PDF Features

### ✅ Supported
- Text extraction from searchable PDFs
- Multi-page documents
- Tables (extracted as plain text)
- Headers and footers
- Basic formatting preservation

### ⚠️ Limited Support
- Complex tables (may lose structure)
- Images (text only, no OCR)
- Forms with fillable fields (text extraction only)
- Multi-column layouts (may reorder text)

### ❌ Not Supported
- Scanned documents without OCR
- Password-protected PDFs
- Digital signatures extraction
- Embedded multimedia

## Tips

1. **Check PDF Quality**: Searchable PDFs work best
2. **Large Files**: Processing may take time for 100+ page documents
3. **Scanned Documents**: Use OCR tools before reading
4. **Structured Data**: Be specific about what you want extracted
5. **Multiple Files**: Process one at a time for clarity

## Common Use Cases

### Documentation Analysis
```
Read the API docs and create a quick-start guide
```

### Data Extraction
```
Extract all email addresses from the contact-list.pdf
```

### Content Summarization
```
Summarize the key points from the research-paper.pdf
```

### Comparison
```
Compare the terms in contract-v1.pdf and contract-v2.pdf
```

### Validation
```
Check if the requirements.pdf mentions database encryption
```

## Integration with Workflows

### Spec-Driven Development
```
1. Read specification from spec.pdf
2. Implement features based on requirements
3. /x-test - Generate tests matching spec
4. Validate implementation against spec
```

### Documentation Generation
```
1. Read API reference from old-docs.pdf
2. Extract endpoint descriptions
3. /x-docs - Generate new markdown docs
4. Update with latest changes
```

## Troubleshooting

### PDF Not Found
```
Error: File not found: docs/guide.pdf

→ Check file path is correct
→ Use absolute or relative path from project root
```

### Empty Content
```
Extracted 10 pages but content is empty

→ PDF may be scanned/image-based
→ Try using OCR tool first
```

### Garbled Text
```
Extracted text contains unusual characters

→ PDF may have encoding issues
→ Try re-exporting PDF with standard settings
```

## Related Skills

- [x-xlsx-reader](./x-xlsx-reader.md) - For spreadsheet data
- [x-code-reviewer](./x-code-reviewer.md) - For code analysis
- [x-test-generator](./x-test-generator.md) - For test creation
