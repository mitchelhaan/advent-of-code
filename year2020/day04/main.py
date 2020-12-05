import re
import traceback
from typing import List

required_fields = ["ecl", "pid", "hcl", "byr", "iyr", "hgt", "eyr"]


def part1(passports: List[str]) -> int:
    valid_count = 0

    for p in passports:
        fields = dict(f.split(":") for f in p.split())

        if all(f in fields for f in required_fields):
            valid_count += 1

    return valid_count


def part2(passports: List[str]) -> int:
    valid_count = 0

    for p in passports:
        fields = dict(f.split(":") for f in p.split())

        try:
            assert 1920 <= int(fields["byr"]) <= 2002
            assert 2010 <= int(fields["iyr"]) <= 2020
            assert 2020 <= int(fields["eyr"]) <= 2030
            hgt = fields["hgt"]
            assert hgt.endswith("cm") or hgt.endswith("in")
            if hgt.endswith("cm"):
                assert 150 <= int(hgt.rsplit("cm")[0]) <= 193
            if hgt.endswith("in"):
                assert 59 <= int(hgt.rsplit("in")[0]) <= 76
            assert re.search(r"^#[0-9a-fA-F]{6}$", fields["hcl"])
            assert fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            assert re.search(r"^\d{9}$", fields["pid"])
        except Exception as e:
            # traceback.print_exc()
            # print(f"Invalid passport: {fields}\n")
            continue

        valid_count += 1

    return valid_count


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as f:
        passports = f.read().strip().split("\n\n")

    print(f"Part1: result is {part1(passports)}")
    print(f"Part2: result is {part2(passports)}")
