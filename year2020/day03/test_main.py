import pytest

map_lines = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().splitlines()


def test_part1():
    assert part1(map_lines) == 7


def test_part2():
    assert part2(map_lines) == 336


if __name__ == "__main__":
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
