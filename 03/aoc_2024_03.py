#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2024-12-03
Purpose: Solves day 03 from advent of code 2024.
"""

from typing import Final
from operator import mul
import re

RE_MUL_PATTERN: Final[re.Pattern] = re.compile(r"mul\((?P<left>\d+),(?P<right>\d+)\)")
RE_DO_PATTERN: Final[re.Pattern] = re.compile(r"(do(n\'t)?\(\))")

TEST_DATA: Final = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)

TEST_DATA_2: Final = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


# --------------------------------------------------
def load_data(filename: str):
    with open(filename, "rt", encoding="utf-8") as file:
        return file.readlines()


def part_01(data) -> str:
    """Solves part 01"""
    inputdata = "".join(data)

    return sum(
        mul(*list(map(int, m.groups()))) for m in RE_MUL_PATTERN.finditer(inputdata)
    )


def part_02(data) -> str:
    """solves part 02"""
    inputdata = "".join(data)

    use = True
    end = 0

    candidates = []

    for m in RE_MUL_PATTERN.finditer(inputdata):
        start = m.span()[0]
        op_matches = RE_DO_PATTERN.findall(inputdata[end:start])
        if len(op_matches) > 0:
            op = op_matches[-1][0]
            use = {"do()": True, "don't()": False}.get(op)

        end = m.span()[1]
        if use:
            candidates.append(tuple(map(int, m.groups())))

    return sum(mul(a, b) for a, b in candidates)


# --------------------------------------------------
def test_part_01():
    """Tests part 01"""
    data = TEST_DATA
    assert 161 == part_01(data)


def test_part_02():
    """Tests part 02"""
    data = TEST_DATA
    assert 48 == part_02(data)


# --------------------------------------------------
def main() -> None:
    """Main wrapper."""
    data = load_data("./03/input")
    # data = TEST_DATA.split("\n")
    # data = TEST_DATA_2.split("\n")
    print(part_01(data))
    print(part_02(data))


if __name__ == "__main__":
    main()
