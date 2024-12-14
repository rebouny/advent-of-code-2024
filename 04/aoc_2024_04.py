#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2024-12-14
Purpose: Solves day 04 from advent of code 2024.
"""

from typing import Final


TEST_DATA: Final = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


XMAS_DIRECTIONS: Final[list[tuple[int, int]]] = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def check_direction(
    grid: dict[tuple[int, int], str], coord: tuple[int, int], direction: tuple[int, int]
) -> bool:
    """Check if string XMAS is setup properly according to given direction."""
    for char in "MAS":
        try:
            coord = (coord[0] + direction[0], coord[1] + direction[1])
            if grid[coord] != char:
                return False
        except KeyError:
            return False
    return True


def get_directions(
    grid: dict[tuple[int, int], str], coord: tuple[int, int]
) -> list[int]:
    """Test for directions which sound reasonable."""
    directions = []
    for i in XMAS_DIRECTIONS:
        try:
            if grid[(coord[0] + i[0], coord[1] + i[1])] == "M":
                directions.append(i)
        except KeyError:
            pass  # ignore direction
    return directions


def check_xmas(grid, coord) -> int:
    """Return amount of "good" directions (aka happy path)."""
    directions = get_directions(grid, coord)

    return len(
        [
            direction
            for direction in directions
            if check_direction(grid, coord, direction)
        ]
    )


def check_x_mas(grid, coord) -> bool:
    """Hard wired check of for fitting variants."""
    try:
        if (
            grid[(coord[0] - 1, coord[1] - 1)] == "M"
            and grid[(coord[0] + 1, coord[1] - 1)] == "S"
            and grid[(coord[0] - 1, coord[1] + 1)] == "M"
            and grid[(coord[0] + 1, coord[1] + 1)] == "S"
        ):
            return True

        if (
            grid[(coord[0] - 1, coord[1] - 1)] == "M"
            and grid[(coord[0] + 1, coord[1] - 1)] == "M"
            and grid[(coord[0] - 1, coord[1] + 1)] == "S"
            and grid[(coord[0] + 1, coord[1] + 1)] == "S"
        ):
            return True

        if (
            grid[(coord[0] - 1, coord[1] - 1)] == "S"
            and grid[(coord[0] + 1, coord[1] - 1)] == "M"
            and grid[(coord[0] - 1, coord[1] + 1)] == "S"
            and grid[(coord[0] + 1, coord[1] + 1)] == "M"
        ):
            return True

        if (
            grid[(coord[0] - 1, coord[1] - 1)] == "S"
            and grid[(coord[0] + 1, coord[1] - 1)] == "S"
            and grid[(coord[0] - 1, coord[1] + 1)] == "M"
            and grid[(coord[0] + 1, coord[1] + 1)] == "M"
        ):
            return True
    except KeyError:
        pass
    return False


# --------------------------------------------------
def load_data(filename: str):
    """Load lines from input."""
    with open(filename, "rt", encoding="utf-8") as file:
        return file.readlines()


def build_grid(data: list[str]) -> dict[tuple[int, int], str]:
    """Build up grid."""
    grid = {}
    for i, y in enumerate(data):
        for j, x in enumerate(y):
            grid[(j, i)] = x
    return grid


def part_01(data) -> str:
    """Solves part 01.

    We filter for occurrances of 'X', find list of possible directions to look
    for and then check each direction. We pass any mismatches or out of bounds
    directions.
    """
    grid = build_grid(data)

    x_es = {x: y for x, y in grid.items() if y == "X"}
    xmas = {(x, y): check_xmas(grid, (x, y)) for x, y in x_es}

    return sum(xmas.values())


def part_02(data) -> str:
    """solves part 02.

    This time we look for 'A' and filter check for each occurrance all four
    possible patterns. We pass on any mismtahces or out of bounds.
    """
    grid = build_grid(data)

    a_es = {x: y for x, y in grid.items() if y == "A"}
    x_mas = {(x, y): check_x_mas(grid, (x, y)) for x, y in a_es}
    good_ones = {k: v for k, v in x_mas.items() if v}

    return len(good_ones)


# --------------------------------------------------
def test_part_01():
    """Tests part 01"""
    data = TEST_DATA
    assert "" == part_01(data)


def test_part_02():
    """Tests part 02"""
    data = TEST_DATA
    assert "" == part_02(data)


# --------------------------------------------------
def main() -> None:
    """Main wrapper."""
    data = load_data("./04/input")
    # data = TEST_DATA.split("\n")
    print(part_01(data))
    print(part_02(data))


if __name__ == "__main__":
    main()
