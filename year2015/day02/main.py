from typing import List


def part1(dimensions: List[str]) -> int:
    total_paper = 0

    for dim in dimensions:
        l, w, h = map(int, dim.split("x"))
        side_areas = 2 * [l * w, w * h, h * l]
        total_paper += sum(side_areas) + min(side_areas)

    return total_paper


def part2(dimensions: List[str]) -> int:
    total_ribbon = 0

    for dim in dimensions:
        l, w, h = map(int, dim.split("x"))
        perimeters = [2 * x for x in [l + w, w + h, h + l]]
        total_ribbon += min(perimeters) + l * w * h

    return total_ribbon


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        data = f.read().strip().split()

    print(f"Part1: result is {part1(data)}")
    print(f"Part2: result is {part2(data)}")
