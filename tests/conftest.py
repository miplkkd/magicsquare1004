"""Shared pytest fixtures."""

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_SRC = _ROOT / "src"
_src_str = str(_SRC)
if _src_str not in sys.path:
    sys.path.insert(0, _src_str)

from entity.constants import BLANK_COUNT, GRID_SIZE

# G1: row-major 4×4, blanks at (2,2) and (3,3) — 1-index
_G1_GRID: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 0, 12],
    [13, 14, 15, 16],
]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1 격자 — 0이 2개, row-major."""
    grid = [row[:] for row in _G1_GRID]
    if len(grid) != GRID_SIZE:
        raise ValueError("G1: row count != GRID_SIZE")
    if sum(cell == 0 for row in grid for cell in row) != BLANK_COUNT:
        raise ValueError("G1: blank count != BLANK_COUNT")
    return grid
