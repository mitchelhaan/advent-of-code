from typing import List


def seat_ids(seats: List[str]) -> List[int]:
    # Each seat ID is a string of row directions (F/B) and col directions (L/R)

    # There's a sneaky optimization here. Since I recognize the binary tree and encoding
    # as a disguised binary string (F/L = 0, B/R = 1), I'm skipping the tree part.
    # For example, "FBFBBFFRLR" is 0b0101100101 (357)
    seat_trans = str.maketrans("FBLR", "0101")

    return [int(seat.translate(seat_trans), 2) for seat in seats]


def part1(seats: List[str]) -> int:
    return max(seat_ids(seats))


def part2(seats: List[str]) -> int:
    taken = sorted(seat_ids(seats))

    # Find the first missing number in the list
    # There should only be one, and not the first or last number
    for i, x in enumerate(taken):
        if taken[i + 1] != x + 1:
            return x + 1


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        seats = f.read().strip().splitlines()

    print(f"Part1: result is {part1(seats)}")
    print(f"Part2: result is {part2(seats)}")
