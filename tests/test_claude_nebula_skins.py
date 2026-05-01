"""Regression tests for Claude/Nebula appearance skins."""

from pathlib import Path

REPO = Path(__file__).parent.parent
CSS = (REPO / "static" / "style.css").read_text(encoding="utf-8")
BOOT_JS = (REPO / "static" / "boot.js").read_text(encoding="utf-8")
INDEX_HTML = (REPO / "static" / "index.html").read_text(encoding="utf-8")
CONFIG_PY = (REPO / "api" / "config.py").read_text(encoding="utf-8")


def test_claude_and_nebula_present_in_picker():
    assert "{name:'Claude'" in BOOT_JS, "Claude skin missing from _SKINS picker list"
    assert "{name:'Nebula'" in BOOT_JS, "Nebula skin missing from _SKINS picker list"


def test_claude_and_nebula_in_early_init_allowlist():
    assert "claude:1" in INDEX_HTML, "Claude missing from early-init skin allowlist"
    assert "nebula:1" in INDEX_HTML, "Nebula missing from early-init skin allowlist"


def test_claude_and_nebula_in_server_skin_allowlist():
    assert '"claude"' in CONFIG_PY, "Claude missing from server settings skin allowlist"
    assert '"nebula"' in CONFIG_PY, "Nebula missing from server settings skin allowlist"


def test_claude_skin_has_font_override():
    assert ':root[data-skin="claude"]{' in CSS, "Claude light block missing"
    assert ':root.dark[data-skin="claude"]{' in CSS, "Claude dark block missing"
    assert '--font-ui:Inter,"Avenir Next","SF Pro Text"' in CSS, (
        "Claude skin should override --font-ui to match Claude-like typography"
    )
