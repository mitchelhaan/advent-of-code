def part1(data: str) -> int:
    level = 0
    for c in data:
        if c == "(":
            level += 1
        elif c == ")":
            level -= 1
    return level


def part2(data: str) -> int:
    level = 0
    for pos, c in enumerate(data, start=1):
        if c == "(":
            level += 1
        elif c == ")":
            level -= 1
        if level == -1:
            return pos


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        data = f.read().strip()

    print(f"Part1: result is {part1(data)}")
    print(f"Part2: result is {part2(data)}")
