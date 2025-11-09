"""Tests for static HTML frontend pages."""

import re
from pathlib import Path

import pytest

FRONTEND_DIR = Path(__file__).parent.parent


class TestIndexPage:
    """Tests for index.html."""

    @pytest.fixture
    def index_html(self):
        """Load index.html content."""
        return (FRONTEND_DIR / "index.html").read_text()

    def test_index_exists(self):
        """Test that index.html exists."""
        assert (FRONTEND_DIR / "index.html").exists()

    def test_has_doctype(self, index_html):
        """Test that index.html has DOCTYPE declaration."""
        assert "<!DOCTYPE html>" in index_html

    def test_has_title(self, index_html):
        """Test that index.html has a title."""
        assert "<title>Claude Code Features Showcase</title>" in index_html

    def test_has_tailwind_cdn(self, index_html):
        """Test that Tailwind CSS CDN is included."""
        assert "cdn.tailwindcss.com" in index_html

    def test_has_datastar_cdn(self, index_html):
        """Test that Datastar CDN is included."""
        assert "@sudodevnull/datastar" in index_html

    def test_has_navigation(self, index_html):
        """Test that navigation is present."""
        assert "<nav" in index_html
        assert 'href="index.html"' in index_html
        assert 'href="demo.html"' in index_html
        assert 'href="about.html"' in index_html

    def test_has_hero_section(self, index_html):
        """Test that hero section is present."""
        assert "Welcome to Claude Code Features" in index_html

    def test_has_feature_cards(self, index_html):
        """Test that feature cards are present."""
        assert "Custom Commands" in index_html
        assert "Skills" in index_html
        assert "Hooks" in index_html
        assert "Documentation" in index_html
        assert "Packages" in index_html
        assert "Applications" in index_html

    def test_has_interactive_counter(self, index_html):
        """Test that interactive counter demo is present."""
        assert "Interactive Counter Demo" in index_html
        assert 'data-store=\'{"count": 0}\'' in index_html
        assert "data-on-click" in index_html

    def test_has_repository_stats(self, index_html):
        """Test that repository stats are present."""
        assert "Repository Stats" in index_html
        assert "Slash Commands" in index_html
        assert "Tests Passing" in index_html

    def test_has_footer(self, index_html):
        """Test that footer is present."""
        assert "<footer" in index_html
        assert "Claude Code" in index_html

    def test_has_responsive_classes(self, index_html):
        """Test that responsive Tailwind classes are used."""
        assert "max-w-7xl" in index_html
        assert "md:" in index_html or "lg:" in index_html


class TestDemoPage:
    """Tests for demo.html."""

    @pytest.fixture
    def demo_html(self):
        """Load demo.html content."""
        return (FRONTEND_DIR / "demo.html").read_text()

    def test_demo_exists(self):
        """Test that demo.html exists."""
        assert (FRONTEND_DIR / "demo.html").exists()

    def test_has_doctype(self, demo_html):
        """Test that demo.html has DOCTYPE declaration."""
        assert "<!DOCTYPE html>" in demo_html

    def test_has_title(self, demo_html):
        """Test that demo.html has a title."""
        assert "<title>Datastar Demo" in demo_html

    def test_has_tailwind_cdn(self, demo_html):
        """Test that Tailwind CSS CDN is included."""
        assert "cdn.tailwindcss.com" in demo_html

    def test_has_datastar_cdn(self, demo_html):
        """Test that Datastar CDN is included."""
        assert "@sudodevnull/datastar" in demo_html

    def test_has_todo_list_demo(self, demo_html):
        """Test that todo list demo is present."""
        assert "Todo List" in demo_html
        assert "todos" in demo_html
        assert "data-model" in demo_html

    def test_has_contact_form_demo(self, demo_html):
        """Test that contact form demo is present."""
        assert "Contact Form" in demo_html
        assert "name" in demo_html.lower()
        assert "email" in demo_html.lower()
        assert "message" in demo_html.lower()

    def test_has_tabbed_content_demo(self, demo_html):
        """Test that tabbed content demo is present."""
        assert "Tabbed Content" in demo_html
        assert "selectedTab" in demo_html

    def test_has_datastar_bindings(self, demo_html):
        """Test that Datastar bindings are present."""
        assert "data-on-click" in demo_html
        assert "data-model" in demo_html or "data-bind" in demo_html


class TestAboutPage:
    """Tests for about.html."""

    @pytest.fixture
    def about_html(self):
        """Load about.html content."""
        return (FRONTEND_DIR / "about.html").read_text()

    def test_about_exists(self):
        """Test that about.html exists."""
        assert (FRONTEND_DIR / "about.html").exists()

    def test_has_doctype(self, about_html):
        """Test that about.html has DOCTYPE declaration."""
        assert "<!DOCTYPE html>" in about_html

    def test_has_title(self, about_html):
        """Test that about.html has a title."""
        assert "<title>About" in about_html

    def test_has_tailwind_cdn(self, about_html):
        """Test that Tailwind CSS CDN is included."""
        assert "cdn.tailwindcss.com" in about_html

    def test_has_datastar_cdn(self, about_html):
        """Test that Datastar CDN is included."""
        assert "@sudodevnull/datastar" in about_html

    def test_has_overview_section(self, about_html):
        """Test that overview section is present."""
        assert "Overview" in about_html or "About This Project" in about_html

    def test_has_architecture_section(self, about_html):
        """Test that architecture section is present."""
        assert "Architecture" in about_html or "Project Architecture" in about_html
        assert ".claude/" in about_html
        assert "packages/" in about_html

    def test_has_technology_stack(self, about_html):
        """Test that technology stack is documented."""
        assert "Technology" in about_html
        assert "Tailwind" in about_html
        assert "Datastar" in about_html

    def test_has_accordion_demo(self, about_html):
        """Test that accordion/interactive feature is present."""
        assert "data-on-click" in about_html or "openSection" in about_html


class TestAllPages:
    """Tests that apply to all HTML pages."""

    @pytest.fixture(params=["index.html", "demo.html", "about.html"])
    def html_file(self, request):
        """Parametrized fixture for all HTML files."""
        filepath = FRONTEND_DIR / request.param
        return filepath, filepath.read_text()

    def test_valid_html_structure(self, html_file):
        """Test that HTML has basic valid structure."""
        filepath, content = html_file
        assert "<!DOCTYPE html>" in content
        assert "<html" in content
        assert "</html>" in content
        assert "<head>" in content
        assert "</head>" in content
        assert "<body" in content
        assert "</body>" in content

    def test_has_meta_charset(self, html_file):
        """Test that charset meta tag is present."""
        _, content = html_file
        assert 'charset="UTF-8"' in content

    def test_has_viewport_meta(self, html_file):
        """Test that viewport meta tag is present."""
        _, content = html_file
        assert "viewport" in content

    def test_no_inline_scripts(self, html_file):
        """Test that there are no inline scripts (except CDN includes)."""
        _, content = html_file
        # Should only have CDN script tags, not inline JavaScript
        inline_scripts = re.findall(r"<script(?![^>]*src=)[^>]*>[\s\S]*?</script>", content)
        assert len(inline_scripts) == 0, "Found unexpected inline scripts"

    def test_consistent_navigation(self, html_file):
        """Test that navigation links are consistent across pages."""
        _, content = html_file
        if "<nav" in content:
            assert 'href="index.html"' in content
            assert 'href="demo.html"' in content
            assert 'href="about.html"' in content

    def test_has_consistent_footer(self, html_file):
        """Test that footer is present and consistent."""
        _, content = html_file
        assert "<footer" in content
        assert "Claude Code" in content


class TestHTMLValidation:
    """Validation tests for HTML content."""

    def test_all_html_files_parseable(self):
        """Test that all HTML files can be read without errors."""
        html_files = ["index.html", "demo.html", "about.html"]
        for filename in html_files:
            filepath = FRONTEND_DIR / filename
            assert filepath.exists(), f"{filename} does not exist"
            content = filepath.read_text()
            assert len(content) > 0, f"{filename} is empty"

    def test_no_broken_image_references(self):
        """Test that there are no img tags with broken src."""
        html_files = ["index.html", "demo.html", "about.html"]
        for filename in html_files:
            content = (FRONTEND_DIR / filename).read_text()
            # Find all img tags
            img_tags = re.findall(r'<img[^>]+>', content)
            for img in img_tags:
                # If img tag exists, it should have src attribute
                if img:
                    assert 'src=' in img, f"Image tag without src in {filename}"

    def test_tailwind_and_datastar_loaded(self):
        """Test that Tailwind and Datastar are properly loaded in all pages."""
        html_files = ["index.html", "demo.html", "about.html"]
        for filename in html_files:
            content = (FRONTEND_DIR / filename).read_text()
            assert "cdn.tailwindcss.com" in content, f"Tailwind CDN missing in {filename}"
            assert "@sudodevnull/datastar" in content, f"Datastar CDN missing in {filename}"
