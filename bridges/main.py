from typing import Callable
from loguru import logger

InputTuple = tuple[int, list[int]]


def stdin_input() -> InputTuple:
    n = int(input("Input n: "))
    arr = [int(x) for x in input(f"Input {n} heights: ").strip().split(" ")][:n]

    return n, arr


def static_input() -> InputTuple:
    return 4, [2, 1, 2, 2]


def get_input(input_func: Callable) -> InputTuple:
    n, arr = input_func()

    if len(arr) != n:
        raise ValueError("Wrong number of numbers input.")

    return n, arr


def solve(n: int, cones: list[int]) -> int:

    active_cones: set[int] = set()
    bridges: dict[int, int] = {}
    previous_cone = -1
    tot = 0

    def prune_cones(cone: int):
        nonlocal active_cones
        todel = {c for c in active_cones if c < cone}
        active_cones -= todel

    for idx, cone in enumerate(cones):

        if cone > previous_cone:
            prune_cones(cone)

        if cone in active_cones:
            tot += idx - bridges[cone] - 1

        active_cones.add(cone)
        bridges[cone] = idx

        previous_cone = cone

    print("Solution: ", tot)
    return tot


def solve_fix(n: int, cones: list[int]) -> int:

    active_cones: set[int] = set()
    bridges: dict[int, int] = {}
    previous_cone = -1
    tot = 0
    lookahead = -1

    def prune_cones(cone: int):
        nonlocal active_cones
        todel = {c for c in active_cones if c < cone}
        active_cones -= todel

    for idx, cone in enumerate(cones):
        lookahead = cones[idx + 1] if idx + 1 < len(cones) else -1

        if cone > previous_cone:
            prune_cones(cone)

        if cone in active_cones:

            #fix - must not finalize bridge too early
            if lookahead == cone:
                previous_cone = cone
                continue
            else:
                tot += idx - bridges[cone] - 1

        active_cones.add(cone)
        bridges[cone] = idx

        previous_cone = cone

    print("Solution: ", tot)
    return tot


def main():
    inp_type: Callable = (
        stdin_input
        if input("Stdin input [y/n] :").strip().lower() == "y"
        else static_input
    )
    # inp_type: Callable = static_input
    solve_fix(*get_input(inp_type))


if __name__ == "__main__":
    main()
