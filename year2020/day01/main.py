import math
from itertools import combinations
from typing import List


def part1(entries: List[int]) -> int:
    """Find the two entries that sum to 2020 and then multiply those numbers together"""
    for choice in combinations(entries, 2):
        if sum(choice) == 2020:
            print(f"Part1: found solution {choice}")
            return math.prod(choice)


def part2(entries: List[int]) -> int:
    """Find the three entries that sum to 2020 and then multiply those numbers together"""
    for choice in combinations(entries, 3):
        if sum(choice) == 2020:
            print(f"Part2: found solution {choice}")
            return math.prod(choice)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        expenses = list(map(int, f.read().strip().split()))

    print(f"Part1: result is {part1(expenses)}")
    print(f"Part2: result is {part2(expenses)}")
