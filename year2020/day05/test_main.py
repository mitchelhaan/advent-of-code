import pytest


def test_part1():
    assert part1(["FBFBBFFRLR"]) == 357
    assert part1(["BFFFBBFRRR"]) == 567
    assert part1(["FFFBBBFRRR"]) == 119
    assert part1(["BBFFBBFRLL"]) == 820
    assert part1(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]) == 820


missing_seat = [
    "FL",
    # seat 1
    "BL",
    "BR",
]


def test_part2():
    assert part2(missing_seat) == 1


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
