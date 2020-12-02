import pytest

entries = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_part1():
    assert part1(entries) == 2


def test_part2():
    assert part2(entries) == 1


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
