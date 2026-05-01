"""Regression tests for left chat sidebar collapse support."""

from pathlib import Path

REPO = Path(__file__).parent.parent
BOOT_JS = (REPO / "static" / "boot.js").read_text(encoding="utf-8")
INDEX_HTML = (REPO / "static" / "index.html").read_text(encoding="utf-8")
STYLE_CSS = (REPO / "static" / "style.css").read_text(encoding="utf-8")


def test_sidebar_toggle_button_exists():
    assert 'id="btnSidebarPanelToggle"' in INDEX_HTML, (
        "Missing sidebar panel toggle button in rail"
    )


def test_sidebar_state_early_init_exists():
    assert "dataset.sidebarPanel" in INDEX_HTML, (
        "Missing early-init sidebar panel dataset hydration"
    )


def test_sidebar_toggle_logic_exists():
    assert "function toggleSidebarPanel(force)" in BOOT_JS, (
        "Missing sidebar panel toggle logic"
    )
    assert "hermes-webui-sidebar-panel" in BOOT_JS, (
        "Sidebar panel state should persist in localStorage"
    )


def test_sidebar_collapsed_css_exists():
    assert 'html[data-sidebar-panel="closed"] .sidebar' in STYLE_CSS, (
        "Missing collapsed sidebar CSS selector"
    )


def test_sidebar_and_workspace_shortcuts_exist():
    assert "if(e.key==='\\\\')" in BOOT_JS, (
        "Missing Cmd/Ctrl+\\\\ shortcut for sidebar toggle"
    )
    assert "if(e.key===']')" in BOOT_JS, (
        "Missing Cmd/Ctrl+] shortcut for workspace toggle"
    )
