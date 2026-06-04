"""D-SOL-01: solver step A output — GREEN assert + Golden Master (int[6], 1-index)."""

from entity.solver_step import format_int6_golden, solve_step_a

from tests._approval import assert_matches_golden

_GOLDEN_REL = "golden/d_sol_01_g1_step_a.approved.txt"

# G1 step A: row-sum fill, 1-index (설계표 Then)
_G1_STEP_A_INT6 = [2, 2, 14, 3, 3, 3]


def test_d_sol_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # Given: G1 격자
    # When: solve_step_a(grid_g1)
    result = solve_step_a(grid_g1)
    # Then: int[6] [r1, c1, n1, r2, c2, n2] (1-index)
    assert result == _G1_STEP_A_INT6
    # Golden Master: 포맷 고정 회귀
    assert_matches_golden(format_int6_golden(result), _GOLDEN_REL)
