"""Smoke test only — note there are NO evals for any prompt's behavior."""
from app.language_detector import detect_language


def test_detect_language_returns_dict():
    out = detect_language("hello world")
    assert isinstance(out, dict)
    assert "language" in out
