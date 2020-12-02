from typing import List


def part1(entries: List[str]) -> int:
    valid_passwords = 0

    for entry in entries:
        rule, password = entry.split(": ")
        count, letter = rule.split()
        count_min, count_max = map(int, count.split("-"))

        if count_min <= password.count(letter) <= count_max:
            valid_passwords += 1

    return valid_passwords


def part2(entries: List[str]) -> int:
    valid_passwords = 0

    for entry in entries:
        rule, password = entry.split(": ")
        pos, letter = rule.split()
        pos1, pos2 = map(int, pos.split("-"))

        if (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter):
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        entries = f.read().strip().splitlines()

    print(f"Part1: result is {part1(entries)}")
    print(f"Part2: result is {part2(entries)}")
