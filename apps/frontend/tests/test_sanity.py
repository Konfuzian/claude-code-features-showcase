"""Sanity check tests - lightweight browser tests that always run.

These tests ensure pages load without errors and basic functionality works.
They run quickly and are part of the standard test suite.
"""

import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

FRONTEND_DIR = Path(__file__).parent.parent


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context for sanity checks."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the frontend server."""
    return "http://localhost:8080"


class TestPageSanity:
    """Sanity checks - ensure pages load without errors."""

    @pytest.mark.parametrize("page_name", ["index.html", "demo.html", "about.html"])
    def test_page_loads_without_errors(self, page: Page, base_url, page_name):
        """Test that page loads and has no console errors."""
        console_errors = []

        # Listen for console messages
        page.on("console", lambda msg: console_errors.append(msg.text()) if msg.type == "error" else None)

        # Navigate to page
        response = page.goto(f"{base_url}/{page_name}")

        # Check response is successful
        assert response.status == 200, f"{page_name} returned status {response.status}"

        # Wait for page to be fully loaded
        page.wait_for_load_state("networkidle")

        # Check no console errors
        assert len(console_errors) == 0, f"{page_name} has console errors: {console_errors}"

    @pytest.mark.parametrize("page_name", ["index.html", "demo.html", "about.html"])
    def test_page_has_title(self, page: Page, base_url, page_name):
        """Test that page has a title."""
        page.goto(f"{base_url}/{page_name}")
        title = page.title()
        assert len(title) > 0, f"{page_name} has no title"
        assert "Claude Code" in title, f"{page_name} title doesn't mention Claude Code"

    def test_navigation_works(self, page: Page, base_url):
        """Test that navigation between pages works."""
        page.goto(f"{base_url}/index.html")

        # Click demo link
        page.click('a[href="demo.html"]')
        expect(page).to_have_url(re.compile("demo.html"))

        # Click about link
        page.click('a[href="about.html"]')
        expect(page).to_have_url(re.compile("about.html"))

        # Click home link
        page.click('a[href="index.html"]')
        expect(page).to_have_url(re.compile("index.html"))

    def test_counter_works(self, page: Page, base_url):
        """Test that interactive counter on index page works."""
        page.goto(f"{base_url}/index.html")

        # Find and click increment button
        increment_btn = page.get_by_role("button", name="+")
        increment_btn.click()

        # Check counter updated
        counter_display = page.locator('text=/Count: \\d+/')
        expect(counter_display).to_have_text("Count: 1")

    def test_accordion_works(self, page: Page, base_url):
        """Test that accordion on about page toggles."""
        page.goto(f"{base_url}/about.html")

        # Find first accordion button
        accordion_button = page.locator('button:has-text("Custom Slash Commands")').first
        content = page.locator('div[data-bind-class\\.hidden*="openSection"]').first

        # Initially closed
        expect(content).to_have_class(re.compile("hidden"))

        # Click to open
        accordion_button.click()
        page.wait_for_timeout(100)

        # Should be visible
        expect(content).not_to_have_class(re.compile("hidden"))
