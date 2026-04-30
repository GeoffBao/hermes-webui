"""Static checks for the assistant chat avatar."""
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent
UI_JS = (REPO_ROOT / "static" / "ui.js").read_text(encoding="utf-8")
STYLE_CSS = (REPO_ROOT / "static" / "style.css").read_text(encoding="utf-8")


def test_assistant_role_uses_image_avatar_with_fallback():
    assert 'src="/static/hermes-agent-avatar.png"' in UI_JS
    assert "assistant-avatar-img" in UI_JS
    assert "assistant-avatar-fallback" in UI_JS
    assert "onerror=" in UI_JS


def test_user_role_uses_image_avatar_with_fallback():
    assert 'src="/static/user-avatar.png"' in UI_JS
    assert "_userRoleHtml" in UI_JS
    assert "user-avatar-img" in UI_JS
    assert "user-avatar-fallback" in UI_JS


def test_assistant_avatar_asset_and_css_exist():
    assert (REPO_ROOT / "static" / "hermes-agent-avatar.png").exists()
    assert (REPO_ROOT / "static" / "user-avatar.png").exists()
    assert ".assistant-avatar-img" in STYLE_CSS
    assert ".user-avatar-img" in STYLE_CSS
    assert "object-fit:cover" in STYLE_CSS
