"""Blank cell coordinates on the grid (1-index, row-major order)."""

from entity.constants import BLANK_CELL, COORD_INDEX_BASE, GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return (row, col) of each blank cell, 1-index, row-major."""
    coords: list[tuple[int, int]] = []
    for row_idx in range(GRID_SIZE):
        for col_idx in range(GRID_SIZE):
            if grid[row_idx][col_idx] == BLANK_CELL:
                coords.append((row_idx + COORD_INDEX_BASE, col_idx + COORD_INDEX_BASE))
    return coords
