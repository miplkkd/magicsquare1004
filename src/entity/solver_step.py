"""Solver step helpers (int[6] output, 1-index coordinates)."""

from entity.blank_loc import find_blank_coords
from entity.constants import BLANK_CELL, COORD_INDEX_BASE, GRID_SIZE, LINE_SUM_TARGET


def solve_step_a(grid: list[list[int]]) -> list[int]:
    """Step A: row-sum fill for each blank → [r1, c1, n1, r2, c2, n2] (1-index)."""
    result: list[int] = []
    for row, col in find_blank_coords(grid):
        row_idx = row - COORD_INDEX_BASE
        col_idx = col - COORD_INDEX_BASE
        others = sum(
            grid[row_idx][c]
            for c in range(GRID_SIZE)
            if not (c == col_idx and grid[row_idx][col_idx] == BLANK_CELL)
        )
        value = LINE_SUM_TARGET - others
        result.extend([row, col, value])
    return result


def format_int6_golden(values: list[int]) -> str:
    """Fixed golden line for int[6] (1-index coords embedded in tuple)."""
    return f"int[6]: {values}\n"
