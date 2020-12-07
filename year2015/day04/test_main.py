def test_part1():
    assert part1("abcdef") == 609043
    assert part1("pqrstuv") == 1048970


if __name__ == "__main__":
    import pytest
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
