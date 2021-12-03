from typing import List


def part1(commands: List[str]) -> int:
    horizontal_position = 0
    depth = 0

    for command in commands:
        action, amount = command.split()
        amount = int(amount)

        if action == "forward":
            horizontal_position += amount
        if action == "down":
            depth += amount
        if action == "up":
            depth -= amount

    return horizontal_position * depth


def part2(commands: List[str]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        action, amount = command.split()
        amount = int(amount)

        if action == "forward":
            horizontal_position += amount
            depth += aim * amount
        if action == "down":
            aim += amount
        if action == "up":
            aim -= amount

    return horizontal_position * depth


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        entries = f.read().strip().splitlines()

    print(f"Part1: result is {part1(entries)}")
    print(f"Part2: result is {part2(entries)}")
