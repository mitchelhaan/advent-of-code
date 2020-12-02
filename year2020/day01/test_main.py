import pytest


expenses = [1721, 979, 366, 299, 675, 1456]


def test_part1():
    assert part1(expenses) == 514579


def test_part2():
    assert part2(expenses) == 241861950


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
