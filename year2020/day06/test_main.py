import pytest

group_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip().split(
    "\n\n"
)


def test_part1():
    assert part1(group_data) == 11


def test_part2():
    assert part2(group_data) == 6


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
