"""Comprehensive end-to-end tests for frontend pages using Playwright.

These tests are more comprehensive and slower than sanity checks.
Run with: task test:e2e or pytest -m e2e
"""

import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

FRONTEND_DIR = Path(__file__).parent.parent
BASE_URL = "http://localhost:8080"

# Mark all tests in this file as e2e (not run by default)
pytestmark = pytest.mark.e2e


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


class TestIndexPageE2E:
    """End-to-end tests for index.html."""

    def test_page_loads(self, page: Page):
        """Test that index page loads successfully."""
        page.goto(f"{BASE_URL}/index.html")
        expect(page).to_have_title(re.compile("Claude Code Features"))

    def test_navigation_links_work(self, page: Page):
        """Test that navigation links are clickable."""
        page.goto(f"{BASE_URL}/index.html")

        # Test Demo link
        page.click('a[href="demo.html"]')
        expect(page).to_have_url(re.compile("demo.html"))
        page.go_back()

        # Test About link
        page.click('a[href="about.html"]')
        expect(page).to_have_url(re.compile("about.html"))

    def test_interactive_counter(self, page: Page):
        """Test that counter buttons work."""
        page.goto(f"{BASE_URL}/index.html")

        # Find counter display
        counter_display = page.locator('text=/Count: \\d+/')

        # Check initial state
        expect(counter_display).to_have_text("Count: 0")

        # Click increment button
        increment_btn = page.get_by_role("button", name="+")
        increment_btn.click()
        expect(counter_display).to_have_text("Count: 1")

        increment_btn.click()
        expect(counter_display).to_have_text("Count: 2")

        # Click decrement button
        decrement_btn = page.get_by_role("button", name="-")
        decrement_btn.click()
        expect(counter_display).to_have_text("Count: 1")

        # Click reset button
        reset_btn = page.get_by_role("button", name="Reset")
        reset_btn.click()
        expect(counter_display).to_have_text("Count: 0")

    def test_feature_cards_visible(self, page: Page):
        """Test that all feature cards are visible."""
        page.goto(f"{BASE_URL}/index.html")

        expect(page.locator("text=Custom Commands")).to_be_visible()
        expect(page.locator("text=Skills")).to_be_visible()
        expect(page.locator("text=Hooks")).to_be_visible()
        expect(page.locator("text=Documentation")).to_be_visible()

    def test_responsive_design(self, page: Page):
        """Test that page is responsive."""
        page.goto(f"{BASE_URL}/index.html")

        # Test mobile viewport
        page.set_viewport_size({"width": 375, "height": 667})
        expect(page.locator("nav")).to_be_visible()

        # Test desktop viewport
        page.set_viewport_size({"width": 1920, "height": 1080})
        expect(page.locator("nav")).to_be_visible()


class TestDemoPageE2E:
    """End-to-end tests for demo.html."""

    def test_page_loads(self, page: Page):
        """Test that demo page loads successfully."""
        page.goto(f"{BASE_URL}/demo.html")
        expect(page).to_have_title(re.compile("Datastar Demo"))

    def test_todo_list_functionality(self, page: Page):
        """Test that todo list works."""
        page.goto(f"{BASE_URL}/demo.html")

        # Find todo input and add button
        todo_input = page.locator('input[type="text"]').first
        add_button = page.get_by_role("button", name="Add").first

        # Add a todo
        todo_input.fill("Test task 1")
        add_button.click()

        # Verify todo appears
        expect(page.locator("text=Test task 1")).to_be_visible()

        # Add another todo
        todo_input.fill("Test task 2")
        add_button.click()
        expect(page.locator("text=Test task 2")).to_be_visible()

    def test_contact_form_validation(self, page: Page):
        """Test that contact form validation works."""
        page.goto(f"{BASE_URL}/demo.html")

        # Try to submit empty form
        submit_button = page.get_by_role("button", name="Send Message")
        submit_button.click()

        # HTML5 validation should prevent submission
        # Check that page doesn't navigate away
        expect(page).to_have_url(re.compile("demo.html"))

    def test_tabbed_content_switching(self, page: Page):
        """Test that tab switching works."""
        page.goto(f"{BASE_URL}/demo.html")

        # Click different tabs and verify content changes
        tab1 = page.get_by_role("button", name="Tab 1")
        tab2 = page.get_by_role("button", name="Tab 2")

        # Click tab 2
        if tab2.is_visible():
            tab2.click()
            # Verify active state changes
            expect(tab2).to_have_class(re.compile("blue"))

            # Click tab 1
            tab1.click()
            expect(tab1).to_have_class(re.compile("blue"))


class TestAboutPageE2E:
    """End-to-end tests for about.html."""

    def test_page_loads(self, page: Page):
        """Test that about page loads successfully."""
        page.goto(f"{BASE_URL}/about.html")
        expect(page).to_have_title(re.compile("About"))

    def test_accordion_toggles(self, page: Page):
        """Test that accordion sections toggle correctly."""
        page.goto(f"{BASE_URL}/about.html")

        # Find accordion buttons
        accordion_buttons = page.locator('button:has-text("Custom Slash Commands")')
        first_button = accordion_buttons.first

        # Get the corresponding content div
        # The content is the next sibling after the button's parent
        content = page.locator(
            'div[data-bind-class\\.hidden*="openSection"]'
        ).first

        # Initially, accordion should be closed (hidden class present)
        expect(content).to_have_class(re.compile("hidden"))

        # Click to open
        first_button.click()
        page.wait_for_timeout(100)  # Wait for animation

        # Should be visible now
        expect(content).not_to_have_class(re.compile("hidden"))

        # Click to close
        first_button.click()
        page.wait_for_timeout(100)

        # Should be hidden again
        expect(content).to_have_class(re.compile("hidden"))

    def test_all_accordion_sections_exist(self, page: Page):
        """Test that all accordion sections are present."""
        page.goto(f"{BASE_URL}/about.html")

        expect(page.locator("text=Custom Slash Commands")).to_be_visible()
        expect(page.locator("text=Specialized Skills")).to_be_visible()
        expect(page.locator("text=Automated Hooks")).to_be_visible()
        expect(page.locator("text=Zero-Build Frontend")).to_be_visible()

    def test_accordion_exclusive_opening(self, page: Page):
        """Test that opening one accordion closes others."""
        page.goto(f"{BASE_URL}/about.html")

        # Open first accordion
        first_button = page.locator('button:has-text("Custom Slash Commands")').first
        first_button.click()
        page.wait_for_timeout(100)

        # Open second accordion
        second_button = page.locator('button:has-text("Specialized Skills")').first
        second_button.click()
        page.wait_for_timeout(100)

        # First content should be hidden again
        first_content = page.locator(
            'div[data-bind-class\\.hidden="$openSection !== 1"]'
        ).first
        expect(first_content).to_have_class(re.compile("hidden"))

        # Second content should be visible
        second_content = page.locator(
            'div[data-bind-class\\.hidden="$openSection !== 2"]'
        ).first
        expect(second_content).not_to_have_class(re.compile("hidden"))

    def test_architecture_section_visible(self, page: Page):
        """Test that architecture section is visible."""
        page.goto(f"{BASE_URL}/about.html")

        expect(page.locator("text=Project Architecture")).to_be_visible()
        expect(page.locator("text=.claude/")).to_be_visible()
        expect(page.locator("text=packages/")).to_be_visible()


class TestCrossBrowserNavigation:
    """Tests for navigation across all pages."""

    @pytest.mark.parametrize(
        "start_page,link_text,expected_url",
        [
            ("index.html", "Demo", "demo.html"),
            ("index.html", "About", "about.html"),
            ("demo.html", "Home", "index.html"),
            ("demo.html", "About", "about.html"),
            ("about.html", "Home", "index.html"),
            ("about.html", "Demo", "demo.html"),
        ],
    )
    def test_navigation_between_pages(
        self, page: Page, start_page, link_text, expected_url
    ):
        """Test navigation works from all pages."""
        page.goto(f"{BASE_URL}/{start_page}")
        page.click(f'a:has-text("{link_text}")')
        expect(page).to_have_url(re.compile(expected_url))

    def test_all_pages_have_consistent_footer(self, page: Page):
        """Test that footer is consistent across pages."""
        pages = ["index.html", "demo.html", "about.html"]

        for html_page in pages:
            page.goto(f"{BASE_URL}/{html_page}")
            footer = page.locator("footer")
            expect(footer).to_be_visible()
            expect(footer).to_contain_text("Claude Code")


class TestAccessibility:
    """Basic accessibility tests."""

    @pytest.mark.parametrize("html_page", ["index.html", "demo.html", "about.html"])
    def test_page_has_proper_heading_structure(self, page: Page, html_page):
        """Test that pages have proper heading hierarchy."""
        page.goto(f"{BASE_URL}/{html_page}")

        # Should have at least one h1
        h1_count = page.locator("h1").count()
        assert h1_count >= 1, f"{html_page} should have at least one h1"

    @pytest.mark.parametrize("html_page", ["index.html", "demo.html", "about.html"])
    def test_buttons_are_keyboard_accessible(self, page: Page, html_page):
        """Test that buttons can be focused with keyboard."""
        page.goto(f"{BASE_URL}/{html_page}")

        # Get first button
        first_button = page.locator("button").first
        if first_button.count() > 0:
            first_button.focus()
            # Verify button is focused
            expect(first_button).to_be_focused()
