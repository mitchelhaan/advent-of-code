from typing import List


def str_is_nice(string: str) -> bool:
    # It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    if sum((string.count(v) for v in "aeiou")) < 3:
        return False

    # It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    try:
        for i, x in enumerate(string):
            if x == string[i + 1]:
                break
    except IndexError:
        return False

    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    if any(x in string for x in ["ab", "cd", "pq", "xy"]):
        return False

    return True


def part1(strings: List[str]) -> int:
    return [str_is_nice(s) for s in strings].count(True)


def str_is_nicer(string: str) -> bool:
    # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    for x in range(len(string)):
        check = string[x : x + 2]
        # When we get to the end, we'll get an empty slice rather than IndexError
        if len(check) != 2:
            return False
        if check in string[:x] or check in string[x + 2 :]:
            break

    # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    try:
        for i, x in enumerate(string):
            if x == string[i + 2]:
                break
    except IndexError:
        return False

    return True


def part2(strings: List[str]) -> int:
    return [str_is_nicer(s) for s in strings].count(True)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        strings = f.read().strip().splitlines()

    print(f"Part1: result is {part1(strings)}")
    print(f"Part2: result is {part2(strings)}")
