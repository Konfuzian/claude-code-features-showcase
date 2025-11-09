"""Tests for PDF reader module using pytest and approval tests."""

from pathlib import Path

import pytest
from approvaltests import verify
from approvaltests.reporters import GenericDiffReporterFactory

from pdf_reader import extract_text_by_page, read_pdf

# Path to test fixtures
FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_PDF = FIXTURES_DIR / "sample.pdf"


class TestReadPdf:
    """Tests for read_pdf function."""

    def test_read_pdf_extracts_all_text(self):
        """Test that read_pdf extracts text from all pages."""
        text = read_pdf(SAMPLE_PDF)

        # Verify basic content is present
        assert "Claude Code Features Showcase" in text
        assert "Text extraction" in text
        assert "Page 2: Testing Data" in text
        assert "multi-page extraction" in text

    def test_read_pdf_with_approval(self):
        """Test PDF extraction using approval tests."""
        text = read_pdf(SAMPLE_PDF)
        verify(text)

    def test_read_pdf_file_not_found(self):
        """Test that read_pdf raises FileNotFoundError for missing file."""
        with pytest.raises(FileNotFoundError, match="PDF file not found"):
            read_pdf("nonexistent.pdf")

    def test_read_pdf_invalid_file(self, tmp_path):
        """Test that read_pdf raises ValueError for invalid PDF."""
        invalid_pdf = tmp_path / "invalid.pdf"
        invalid_pdf.write_text("This is not a PDF")

        with pytest.raises(ValueError, match="Failed to read PDF"):
            read_pdf(invalid_pdf)


class TestExtractTextByPage:
    """Tests for extract_text_by_page function."""

    def test_extract_text_by_page_returns_list(self):
        """Test that extract_text_by_page returns a list of page data."""
        pages = extract_text_by_page(SAMPLE_PDF)

        assert isinstance(pages, list)
        assert len(pages) == 2

    def test_extract_text_by_page_structure(self):
        """Test the structure of returned page data."""
        pages = extract_text_by_page(SAMPLE_PDF)

        for page in pages:
            assert "page" in page
            assert "text" in page
            assert "char_count" in page
            assert isinstance(page["page"], int)
            assert isinstance(page["text"], str)
            assert isinstance(page["char_count"], int)

    def test_extract_text_by_page_content(self):
        """Test that page content is correctly extracted."""
        pages = extract_text_by_page(SAMPLE_PDF)

        # Page 1
        assert pages[0]["page"] == 1
        assert "Claude Code Features Showcase" in pages[0]["text"]
        assert pages[0]["char_count"] > 0

        # Page 2
        assert pages[1]["page"] == 2
        assert "Page 2: Testing Data" in pages[1]["text"]
        assert pages[1]["char_count"] > 0

    def test_extract_text_by_page_with_approval(self):
        """Test page extraction using approval tests."""
        pages = extract_text_by_page(SAMPLE_PDF)

        # Format output for approval
        output = []
        for page in pages:
            output.append(f"=== Page {page['page']} ({page['char_count']} chars) ===")
            output.append(page["text"])
            output.append("")

        verify("\n".join(output))

    def test_extract_text_by_page_file_not_found(self):
        """Test that extract_text_by_page raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="PDF file not found"):
            extract_text_by_page("nonexistent.pdf")
