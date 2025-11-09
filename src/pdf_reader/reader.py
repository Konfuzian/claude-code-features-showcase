"""Core PDF reading functionality."""

from pathlib import Path
from typing import Dict, List

from pypdf import PdfReader


def read_pdf(file_path: str | Path) -> str:
    """
    Extract all text from a PDF file.

    Args:
        file_path: Path to the PDF file

    Returns:
        Extracted text from all pages

    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        ValueError: If the file is not a valid PDF
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    try:
        reader = PdfReader(path)
        text_parts = []

        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text.strip():
                text_parts.append(text)

        return "\n\n".join(text_parts)
    except Exception as e:
        raise ValueError(f"Failed to read PDF: {e}") from e


def extract_text_by_page(file_path: str | Path) -> List[Dict[str, any]]:
    """
    Extract text from a PDF file, organized by page.

    Args:
        file_path: Path to the PDF file

    Returns:
        List of dictionaries with page number and text content

    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        ValueError: If the file is not a valid PDF
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    try:
        reader = PdfReader(path)
        pages = []

        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            pages.append({
                "page": page_num,
                "text": text,
                "char_count": len(text),
            })

        return pages
    except Exception as e:
        raise ValueError(f"Failed to read PDF: {e}") from e
