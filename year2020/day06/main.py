from functools import reduce
from typing import List


def part1(groups: List[str]) -> int:
    # For each group, count the number of questions to which anyone answered "yes"
    # Sum the lengths of the sets of answers for each group
    return sum(len(reduce(lambda x, y: set(x) | set(y), g.split())) for g in groups)


def part2(groups: List[str]) -> int:
    # For each group, count the number of questions to which everyone answered "yes"
    # Sum the lengths of set intersection of each person's answers in each group
    return sum(len(reduce(lambda x, y: set(x) & set(y), g.split())) for g in groups)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        groups = f.read().strip().split("\n\n")

    print(f"Part1: result is {part1(groups)}")
    print(f"Part2: result is {part2(groups)}")
