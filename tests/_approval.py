"""Golden Master approval helpers."""

from __future__ import annotations

import os
from pathlib import Path

_TESTS_ROOT = Path(__file__).resolve().parent


def assert_matches_golden(actual: str, relative: str) -> None:
    """Compare actual text to tests/<relative> golden file.

    Set UPDATE_GOLDEN=1 to (re)write the approved file from actual.
    """
    golden_path = _TESTS_ROOT / relative
    normalized = actual if actual.endswith("\n") else f"{actual}\n"

    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(normalized, encoding="utf-8", newline="\n")
        return

    if not golden_path.is_file():
        raise AssertionError(
            f"Golden file missing: {golden_path}. "
            "Run with UPDATE_GOLDEN=1 to create it."
        )

    expected = golden_path.read_text(encoding="utf-8")
    if expected != normalized:
        raise AssertionError(
            f"Golden mismatch for {relative}\n"
            f"--- expected ({golden_path})\n{expected}"
            f"--- actual\n{normalized}"
        )
