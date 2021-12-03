import itertools
import math
from functools import reduce
from typing import List


def part1(depths: List[int]) -> int:
    """Find the number of depth readings that are greater than the previous one"""
    larger_count = 0
    for x in range(0, len(depths) - 1):
        if depths[x + 1] > depths[x]:
            larger_count += 1
    return larger_count


def part2(depths: List[int]) -> int:
    """Like part 1, but using a sliding window"""
    window_size = 3
    larger_count = 0
    for x in range(0, len(depths) - window_size):
        previous_window = depths[x : x + window_size]
        current_window = depths[x + 1 : x + 1 + window_size]
        if sum(current_window) > sum(previous_window):
            larger_count += 1
    return larger_count


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        depths = list(map(int, f.read().strip().split()))

    print(f"Part1: result is {part1(depths)}")
    print(f"Part2: result is {part2(depths)}")
