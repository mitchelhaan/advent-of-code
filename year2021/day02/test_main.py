import pytest

commands = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_part1():
    assert part1(commands) == 150


def test_part2():
    assert part2(commands) == 900


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
