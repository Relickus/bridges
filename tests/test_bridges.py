import pytest
from bridges.main import solve_fix as solve


@pytest.mark.parametrize(
    "n, cones, expected_output",
    [
        (6, [1, 2, 2, 3, 5, 3], 0),
        (4, [1, 3, 2, 3, 5], 1),
        (10, [2, 1, 2, 5, 3, 1, 2, 3, 5, 2], 7),
        # additional tests
        (0, [], 0),
        (1, [2], 0),
        (2, [2, 2], 0),
        (2, [2, 2], 0),
        (3, [2, 1, 2], 1),
        (4, [2, 1, 1, 2], 2),
        (4, [1, 2, 2, 1], 0),
        (5, [1, 2, 5, 2, 1], 0),
        # hotfixed the following
        (3, [2, 2, 2], 1),
        (4, [2, 2, 2, 2], 2),
        (4, [2, 1, 2, 2], 2),
        (20, [1, 2, 3, 7, 5, 3, 1, 1, 2, 3, 4, 5, 1, 3, 2, 3, 7, 3, 2, 1], 22),
    ],
    ids=lambda x: f"{x}",
)
def test_solve(n: int, cones: list[int], expected_output: int):
    assert solve(n, cones) == expected_output
