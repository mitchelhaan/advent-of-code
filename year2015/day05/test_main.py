def test_part1():
    assert part1(["ugknbfddgicrmopn"]) == 1
    assert part1(["aaa"]) == 1
    assert part1(["jchzalrnumimnmhp"]) == 0
    assert part1(["haegwjzuvuyypxyu"]) == 0
    assert part1(["dvszwmarrgswjxmb"]) == 0


def test_part2():
    assert part2(["qjhvhtzxzqqjkmpb"]) == 1
    assert part2(["xxyxx"]) == 1
    assert part2(["uurcxstgmygtbstg"]) == 0
    assert part2(["ieodomkazucvgmuy"]) == 0


if __name__ == "__main__":
    import pytest
    from main import part1, part2

    pytest.main([__file__])
else:
    from .main import part1, part2
