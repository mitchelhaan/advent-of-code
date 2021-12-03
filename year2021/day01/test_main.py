import pytest


depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1():
    assert part1(depths) == 7


def test_part2():
    assert part2(depths) == 5


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
