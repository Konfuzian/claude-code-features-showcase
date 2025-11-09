"""Tests for XLSX reader module using pytest and approval tests."""

from pathlib import Path

import pytest
from approvaltests import verify

from xlsx_reader import extract_sheets, read_xlsx

# Path to test fixtures
FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_XLSX = FIXTURES_DIR / "sample.xlsx"


class TestReadXlsx:
    """Tests for read_xlsx function."""

    def test_read_xlsx_returns_dict(self):
        """Test that read_xlsx returns a dictionary of sheets."""
        data = read_xlsx(SAMPLE_XLSX)

        assert isinstance(data, dict)
        assert len(data) == 3
        assert "Employees" in data
        assert "Projects" in data
        assert "Summary" in data

    def test_read_xlsx_employees_sheet(self):
        """Test that employee data is correctly extracted."""
        data = read_xlsx(SAMPLE_XLSX)
        employees = data["Employees"]

        # Check headers
        assert employees[0] == ["ID", "Name", "Department", "Salary", "Start Date"]

        # Check first employee
        assert employees[1][0] == 1
        assert employees[1][1] == "Alice Smith"
        assert employees[1][2] == "Engineering"
        assert employees[1][3] == 95000

    def test_read_xlsx_with_approval(self):
        """Test Excel extraction using approval tests."""
        data = read_xlsx(SAMPLE_XLSX)

        # Format output for approval
        output = []
        for sheet_name, rows in data.items():
            output.append(f"=== Sheet: {sheet_name} ===")
            for row in rows:
                output.append(str(row))
            output.append("")

        verify("\n".join(output))

    def test_read_xlsx_file_not_found(self):
        """Test that read_xlsx raises FileNotFoundError for missing file."""
        with pytest.raises(FileNotFoundError, match="Excel file not found"):
            read_xlsx("nonexistent.xlsx")

    def test_read_xlsx_invalid_file(self, tmp_path):
        """Test that read_xlsx raises ValueError for invalid Excel file."""
        invalid_xlsx = tmp_path / "invalid.xlsx"
        invalid_xlsx.write_text("This is not an Excel file")

        with pytest.raises(ValueError, match="Failed to read Excel file"):
            read_xlsx(invalid_xlsx)


class TestExtractSheets:
    """Tests for extract_sheets function."""

    def test_extract_sheets_returns_list(self):
        """Test that extract_sheets returns a list of sheet data."""
        sheets = extract_sheets(SAMPLE_XLSX)

        assert isinstance(sheets, list)
        assert len(sheets) == 3

    def test_extract_sheets_structure(self):
        """Test the structure of returned sheet data."""
        sheets = extract_sheets(SAMPLE_XLSX)

        for sheet in sheets:
            assert "name" in sheet
            assert "rows" in sheet
            assert "columns" in sheet
            assert "data" in sheet
            assert isinstance(sheet["name"], str)
            assert isinstance(sheet["rows"], int)
            assert isinstance(sheet["columns"], int)
            assert isinstance(sheet["data"], list)

    def test_extract_sheets_metadata(self):
        """Test that sheet metadata is correct."""
        sheets = extract_sheets(SAMPLE_XLSX)

        # Find Employees sheet
        employees = next(s for s in sheets if s["name"] == "Employees")
        assert employees["rows"] == 5  # Header + 4 employees
        assert employees["columns"] == 5  # ID, Name, Dept, Salary, Date

        # Find Projects sheet
        projects = next(s for s in sheets if s["name"] == "Projects")
        assert projects["rows"] == 4  # Header + 3 projects
        assert projects["columns"] == 4  # Project, Lead, Status, Budget

        # Find Summary sheet
        summary = next(s for s in sheets if s["name"] == "Summary")
        assert summary["rows"] == 4  # Header + 3 metrics
        assert summary["columns"] == 2  # Metric, Value

    def test_extract_sheets_with_approval(self):
        """Test sheet extraction using approval tests."""
        sheets = extract_sheets(SAMPLE_XLSX)

        # Format output for approval
        output = []
        for sheet in sheets:
            output.append(f"=== {sheet['name']} ({sheet['rows']} rows, {sheet['columns']} cols) ===")
            for row in sheet["data"]:
                output.append(str(row))
            output.append("")

        verify("\n".join(output))

    def test_extract_sheets_file_not_found(self):
        """Test that extract_sheets raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="Excel file not found"):
            extract_sheets("nonexistent.xlsx")
