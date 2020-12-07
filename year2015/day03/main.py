def part1(directions: str) -> int:
    pos = (0, 0)
    visited = set([pos])

    for d in directions:
        if d == "<":
            pos = (pos[0] - 1, pos[1])
        elif d == ">":
            pos = (pos[0] + 1, pos[1])
        elif d == "v":
            pos = (pos[0], pos[1] - 1)
        elif d == "^":
            pos = (pos[0], pos[1] + 1)
        visited.add(pos)

    return len(visited)


def part2(directions: str) -> int:
    santa_pos = (0, 0)
    robot_pos = (0, 0)

    visited = set([santa_pos])

    for i, d in enumerate(directions):
        if i % 2:
            pos = santa_pos
        else:
            pos = robot_pos

        if d == "<":
            pos = (pos[0] - 1, pos[1])
        elif d == ">":
            pos = (pos[0] + 1, pos[1])
        elif d == "v":
            pos = (pos[0], pos[1] - 1)
        elif d == "^":
            pos = (pos[0], pos[1] + 1)

        if i % 2:
            santa_pos = pos
        else:
            robot_pos = pos

        visited.add(pos)

    return len(visited)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        data = f.read().strip()

    print(f"Part1: result is {part1(data)}")
    print(f"Part2: result is {part2(data)}")
