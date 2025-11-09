# Using x-xlsx-reader Skill

## What It Does

Reads Excel workbooks (.xlsx) and extracts:
- Data from all sheets
- Multiple data types (text, numbers, dates)
- Cell formatting information
- Structured data as tables

Uses Python with the `openpyxl` library.

## When to Use

- Reading Excel spreadsheets
- Extracting workbook data
- Analyzing Excel files
- Converting Excel to structured format (JSON, CSV)
- Processing reports and datasets

## How to Invoke

Skills are invoked automatically by Claude based on context. Ask Claude to work with Excel files:

```
Can you read the sales data from reports/sales-q4.xlsx?
```

```
Extract all customer information from customers.xlsx
```

```
Analyze the budget spreadsheet and summarize the expenses
```

## Example 1: Reading Data

### Request
```
Please read the sales data from data/sales-2024.xlsx and show me the total revenue
```

### What Happens
1. Claude invokes the `x-xlsx-reader` skill
2. Skill runs Python script with openpyxl
3. Reads all sheets and extracts data
4. Claude analyzes and calculates totals

### Response
```
📊 Reading Excel: data/sales-2024.xlsx

Found 3 sheets: Sales, Returns, Summary

=== Sales Sheet ===
Columns: Date, Product, Quantity, Price, Revenue
Rows: 1,247

=== Revenue Analysis ===

Total Revenue: $1,245,678.50

Top Products:
1. Widget Pro - $345,890.00 (28%)
2. Gadget Plus - $289,450.00 (23%)
3. Service Premium - $187,234.00 (15%)
4. Widget Basic - $156,789.00 (13%)
5. Others - $266,315.50 (21%)

Monthly Breakdown:
- Q1: $287,450.00
- Q2: $312,890.00
- Q3: $298,123.00
- Q4: $347,215.50
```

## Example 2: Multi-Sheet Analysis

### Request
```
Read inventory.xlsx and tell me which items are low stock
```

### Response
```
📊 Reading Excel: inventory.xlsx

Found 2 sheets: Current Stock, Reorder Levels

=== Low Stock Alert ===

Items below reorder level:

CRITICAL (< 10 units):
- SKU-1234: Widget Pro - 3 units (reorder: 50)
- SKU-5678: Gadget Mini - 7 units (reorder: 25)

WARNING (< 25% of reorder level):
- SKU-2345: Cable USB-C - 8 units (reorder: 100)
- SKU-6789: Adapter HDMI - 12 units (reorder: 75)

ATTENTION (< 50% of reorder level):
- SKU-3456: Battery Pack - 18 units (reorder: 40)
- SKU-7890: Charger Wireless - 22 units (reorder: 50)

Total items needing reorder: 6
Estimated reorder cost: $4,567.80
```

## Example 3: Data Transformation

### Request
```
Convert the customer data from customers.xlsx to JSON format
```

### Response
```
📊 Reading Excel: customers.xlsx

Sheet: Customer Data (142 rows)

Converted to JSON:

```json
[
  {
    "id": 1001,
    "name": "Acme Corporation",
    "email": "contact@acme.com",
    "phone": "(555) 123-4567",
    "status": "active",
    "total_orders": 23,
    "lifetime_value": 45678.90
  },
  {
    "id": 1002,
    "name": "TechStart Inc",
    "email": "info@techstart.com",
    "phone": "(555) 234-5678",
    "status": "active",
    "total_orders": 15,
    "lifetime_value": 32450.00
  },
  // ... 140 more records
]
```

Data saved to: customers.json
```

## Example 4: Financial Analysis

### Request
```
Analyze the expense report in finances/expenses-2024.xlsx and categorize spending
```

### Response
```
📊 Reading Excel: finances/expenses-2024.xlsx

Found 1 sheet: Expenses (365 rows)

=== Expense Analysis for 2024 ===

Total Spending: $234,567.89

By Category:
1. Payroll - $125,000.00 (53.3%)
2. Office Rent - $36,000.00 (15.4%)
3. Software/SaaS - $28,450.00 (12.1%)
4. Marketing - $18,900.00 (8.1%)
5. Travel - $12,345.00 (5.3%)
6. Equipment - $8,872.89 (3.8%)
7. Miscellaneous - $5,000.00 (2.1%)

Monthly Average: $19,547.32

Highest Month: December - $28,934.56
Lowest Month: February - $15,678.23

Trends:
- Marketing spend increased 40% in Q4
- Travel expenses decreased 25% year-over-year
- SaaS costs growing steadily (~$200/month increase)
```

## Example 5: Data Validation

### Request
```
Check the test-results.xlsx file for any failing tests
```

### Response
```
📊 Reading Excel: test-results.xlsx

Sheet: Test Results (487 rows)

=== Test Execution Summary ===

Total Tests: 487
✅ Passed: 452 (92.8%)
❌ Failed: 28 (5.7%)
⚠️  Skipped: 7 (1.4%)

Failed Tests by Module:

Authentication (8 failures):
- test_login_invalid_credentials
- test_password_reset_expired_token
- test_2fa_invalid_code
- ... (5 more)

Payment Processing (12 failures):
- test_process_declined_card
- test_refund_partial_amount
- test_payment_timeout_handling
- ... (9 more)

API Endpoints (8 failures):
- test_rate_limiting
- test_invalid_json_payload
- ... (6 more)

Flaky Tests (failed intermittently):
- test_websocket_connection (failed 3/10 runs)
- test_cache_invalidation (failed 2/10 runs)
```

## Supported Features

### ✅ Fully Supported
- Reading all sheets in a workbook
- Text, numbers, dates, booleans
- Formulas (evaluated values)
- Multiple data formats
- Empty cells
- Large files (thousands of rows)

### ⚠️ Limited Support
- Cell formatting (colors, fonts) - basic info only
- Charts and graphs - metadata only
- Merged cells - first cell value only
- Protected sheets - read-only if unlocked

### ❌ Not Supported
- Macros (VBA code)
- Pivot tables (data only)
- External links
- Password-protected workbooks
- Binary .xls format (use .xlsx)

## Tips

1. **Use .xlsx Format**: Not .xls (old format)
2. **Clean Data**: Remove unnecessary formatting
3. **Header Rows**: Use first row for column names
4. **Date Formats**: Ensure dates are properly formatted in Excel
5. **Large Files**: May take time for 10,000+ rows

## Common Use Cases

### Data Import
```
Read the user data from import.xlsx and add it to the database
```

### Report Analysis
```
Analyze the monthly report and highlight key metrics
```

### Data Validation
```
Check for duplicate entries in contacts.xlsx
```

### Format Conversion
```
Convert budget.xlsx to CSV format
```

### Cross-Reference
```
Compare the inventory.xlsx with sales.xlsx and find discrepancies
```

## Integration with Workflows

### Data Processing Pipeline
```
1. Read data from source.xlsx
2. Validate and clean data
3. Transform to required format
4. Generate code to import data
5. /x-test - Create validation tests
```

### Report Automation
```
1. Read monthly-report.xlsx
2. Extract key metrics
3. Generate summary visualization
4. /x-docs - Document the data structure
```

### Testing with Data
```
1. Read test-cases.xlsx
2. Generate test code from scenarios
3. /x-test - Create comprehensive test suite
4. Run tests with data from spreadsheet
```

## Working with Multiple Sheets

### Request
```
The workbook has 3 sheets: Customers, Orders, Products. Show me customers who placed orders over $1000
```

### Response
```
📊 Reading Excel: sales-data.xlsx

Cross-referencing Customers, Orders, and Products sheets...

=== High-Value Customers ===

1. Acme Corp (ID: 1001)
   - Total Orders: $23,456.78
   - Order Count: 12
   - Avg Order: $1,954.73

2. TechStart Inc (ID: 1005)
   - Total Orders: $18,900.00
   - Order Count: 8
   - Avg Order: $2,362.50

... (15 more customers)

Total: 17 customers with orders over $1,000
Combined revenue: $187,234.56
```

## Troubleshooting

### File Not Found
```
Error: Cannot open inventory.xlsx

→ Check file path
→ Ensure file exists
→ Verify file permissions
```

### Invalid Format
```
Error: File is not a valid .xlsx workbook

→ File may be .xls (old format)
→ Try re-saving as .xlsx
→ Check file isn't corrupted
```

### Empty Data
```
Warning: Sheet 'Data' appears to be empty

→ Check correct sheet name
→ Verify data exists in spreadsheet
→ Check for hidden rows/columns
```

### Large File Performance
```
Reading large file (50,000 rows)...

→ This may take 30-60 seconds
→ Consider filtering data in Excel first
→ Split into smaller files if possible
```

## Related Skills

- [x-pdf-reader](./x-pdf-reader.md) - For PDF documents
- [x-code-reviewer](./x-code-reviewer.md) - For code analysis
- [x-test-generator](./x-test-generator.md) - For test creation
