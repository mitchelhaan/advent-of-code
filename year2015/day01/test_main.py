def test_part1():
    assert part1("(())") == 0
    assert part1("()()") == 0
    assert part1("(((") == 3
    assert part1("(()(()(") == 3
    assert part1("))(((((") == 3
    assert part1("())") == -1
    assert part1("))(") == -1
    assert part1(")))") == -3
    assert part1(")())())") == -3


def test_part2():
    assert part2(")") == 1
    assert part2("()())") == 5


if __name__ == "__main__":
    import pytest
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
