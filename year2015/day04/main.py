from hashlib import md5

SEARCH_MAX = 1_000_000_000


def md5_prefix_search(secret: str, prefix: str) -> int:
    for number in range(1, SEARCH_MAX):
        if md5(f"{secret}{number}".encode()).hexdigest().startswith(prefix):
            return number


def part1(secret: str) -> int:
    return md5_prefix_search(secret, 5 * "0")


def part2(secret: str) -> int:
    return md5_prefix_search(secret, 6 * "0")


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        data = f.read().strip()

    print(f"Part1: result is {part1(data)}")
    print(f"Part2: result is {part2(data)}")
