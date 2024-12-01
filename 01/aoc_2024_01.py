#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2024-12-01
Purpose: Solves day 01 from advent of code 2024.
"""

from typing import Final
from collections import Counter


TEST_DATA: Final = """3   4
4   3
2   5
1   3
3   9
3   3"""


# --------------------------------------------------
def load_data(filename: str):
    """Split input into lines."""
    with open(filename, "rt", encoding="utf-8") as file:
        return file.readlines()


def build_input(lines: list[str]) -> tuple[list[int], list[int]]:
    """Parse input into pair of list of int."""
    return (
        [int(line.split(maxsplit=2)[0]) for line in lines],
        [int(line.split(maxsplit=2)[1]) for line in lines],
    )


def part_01(data) -> str:
    """Solves part 01"""
    first, second = build_input(data)

    return sum(max(pair) - min(pair) for pair in zip(sorted(first), sorted(second)))


def part_02(data) -> str:
    """solves part 02"""
    first, second = build_input(data)

    counter = Counter(second)
    return sum(x * counter[x] for x in first)


# --------------------------------------------------
def test_part_01():
    """Tests part 01"""
    data = TEST_DATA.split("\n")
    assert 11 == part_01(data)


def test_part_02():
    """Tests part 02"""
    data = TEST_DATA.split("\n")
    assert 31 == part_02(data)


# --------------------------------------------------
def main() -> None:
    """Main wrapper."""
    data = load_data("./01/input")
    # data = load_testdata(TEST_DATA)
    print(part_01(data))
    print(part_02(data))


if __name__ == "__main__":
    main()
