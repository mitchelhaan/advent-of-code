import math
from typing import List


def part1(map_lines: List[str], slope_x=3, slope_y=1) -> int:
    x = 0
    trees = 0

    for y in range(0, len(map_lines), slope_y):
        if map_lines[y][x % len(map_lines[y])] == "#":
            trees += 1
        x += slope_x

    return trees


def part2(map_lines: List[str]) -> int:
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    return math.prod(part1(map_lines, *slope) for slope in slopes)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        entries = f.read().strip().splitlines()

    print(f"Part1: result is {part1(entries)}")
    print(f"Part2: result is {part2(entries)}")
