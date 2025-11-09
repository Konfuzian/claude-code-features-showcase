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
        page.wait_for_load_state("networkidle")  # Wait for Datastar to load
        page.wait_for_timeout(1000)  # Wait for Datastar to fully initialize

        # Find counter display (shows just the number)
        counter_display = page.locator('[data-text="$count"]')

        # Check initial state
        expect(counter_display).to_have_text("0")

        # Click increment button and wait for update
        increment_btn = page.get_by_role("button", name="Increment")
        increment_btn.click()
        page.wait_for_timeout(500)  # Wait for Datastar reactivity
        expect(counter_display).to_have_text("1")

        increment_btn.click()
        page.wait_for_timeout(500)
        expect(counter_display).to_have_text("2")

        # Click decrement button
        decrement_btn = page.get_by_role("button", name="Decrement")
        decrement_btn.click()
        page.wait_for_timeout(500)
        expect(counter_display).to_have_text("1")

        # Click reset button
        reset_btn = page.get_by_role("button", name="Reset")
        reset_btn.click()
        page.wait_for_timeout(500)
        expect(counter_display).to_have_text("0")

    def test_feature_cards_visible(self, page: Page):
        """Test that all feature cards are visible."""
        page.goto(f"{BASE_URL}/index.html")

        # Use more specific selectors to avoid strict mode violations
        expect(page.get_by_role("heading", name="Custom Commands")).to_be_visible()
        expect(page.get_by_role("heading", name="Skills")).to_be_visible()
        expect(page.get_by_role("heading", name="Hooks")).to_be_visible()
        expect(page.get_by_role("heading", name="Documentation")).to_be_visible()

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
        page.wait_for_load_state("networkidle")  # Wait for Datastar to load
        page.wait_for_timeout(1000)  # Wait for Datastar to fully initialize

        # Find todo input and add button
        todo_input = page.locator('input[data-model="$newTodo"]')
        add_button = page.get_by_role("button", name="Add Todo")

        # Add a todo
        todo_input.fill("Test task 1")
        add_button.click()
        page.wait_for_timeout(500)  # Wait for Datastar reactivity

        # Verify todo appears
        expect(page.locator("text=Test task 1")).to_be_visible()

        # Add another todo
        todo_input.fill("Test task 2")
        add_button.click()
        page.wait_for_timeout(500)
        expect(page.locator("text=Test task 2")).to_be_visible()

    def test_contact_form_validation(self, page: Page):
        """Test that contact form validation works."""
        page.goto(f"{BASE_URL}/demo.html")
        page.wait_for_load_state("networkidle")  # Wait for Datastar to load
        page.wait_for_timeout(1000)  # Wait for Datastar to fully initialize

        # The submit button should be disabled when form is empty
        submit_button = page.get_by_role("button", name="Submit")
        page.wait_for_timeout(500)  # Wait for Datastar to apply bindings
        expect(submit_button).to_be_disabled()

        # Fill in the form fields
        page.locator('input[data-model="$name"]').fill("Test User")
        page.locator('input[data-model="$email"]').fill("test@example.com")
        page.locator('textarea[data-model="$message"]').fill("Test message")
        page.wait_for_timeout(500)  # Wait for Datastar to update

        # Now button should be enabled
        expect(submit_button).to_be_enabled()

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
        page.wait_for_load_state("networkidle")  # Wait for Datastar to load
        page.wait_for_timeout(1000)  # Wait for Datastar to fully initialize

        # Find first accordion button
        first_button = page.locator('button:has-text("Custom Slash Commands")').first

        # Get the corresponding content div
        content = page.locator('div[data-bind-class\\.hidden="$openSection !== 1"]').first

        # Initially, accordion should be closed (hidden class present)
        expect(content).to_have_class(re.compile("hidden"))

        # Click to open
        first_button.click()
        page.wait_for_timeout(500)  # Wait for Datastar to update

        # Should be visible now (no hidden class)
        expect(content).not_to_have_class(re.compile("hidden"))

        # Click to close
        first_button.click()
        page.wait_for_timeout(500)

        # Should be hidden again
        expect(content).to_have_class(re.compile("hidden"))

    def test_all_accordion_sections_exist(self, page: Page):
        """Test that all accordion sections are present."""
        page.goto(f"{BASE_URL}/about.html")

        # Use more specific selectors to avoid strict mode violations
        expect(page.get_by_role("button", name="Custom Slash Commands")).to_be_visible()
        expect(page.get_by_role("button", name="Specialized Skills")).to_be_visible()
        expect(page.get_by_role("button", name="Automated Hooks")).to_be_visible()
        expect(page.get_by_role("button", name="Zero-Build Frontend")).to_be_visible()

    def test_accordion_exclusive_opening(self, page: Page):
        """Test that opening one accordion closes others."""
        page.goto(f"{BASE_URL}/about.html")
        page.wait_for_load_state("networkidle")  # Wait for Datastar to load
        page.wait_for_timeout(1000)  # Wait for Datastar to fully initialize

        # Open first accordion
        first_button = page.locator('button:has-text("Custom Slash Commands")').first
        first_button.click()
        page.wait_for_timeout(500)  # Wait for Datastar to update

        # Verify first is open
        first_content = page.locator('div[data-bind-class\\.hidden="$openSection !== 1"]').first
        expect(first_content).not_to_have_class(re.compile("hidden"))

        # Open second accordion
        second_button = page.locator('button:has-text("Specialized Skills")').first
        second_button.click()
        page.wait_for_timeout(500)  # Wait for Datastar to update

        # First content should be hidden again (exclusive behavior)
        expect(first_content).to_have_class(re.compile("hidden"))

        # Second content should be visible
        second_content = page.locator('div[data-bind-class\\.hidden="$openSection !== 2"]').first
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
