from typing import List, Callable
import re
import time

begin = time.time()

###

with open("input.txt", "r") as file:
    lines = file.readlines()


def check1(phrase: str, min: str, max: str, letter: str) -> bool:
    return (
        int(min) <= len([symbol for symbol in phrase if symbol == letter]) <= int(max)
    )


def check2(phrase: str, min: str, max: str, letter: str) -> bool:
    return (phrase[int(min) - 1] == letter) ^ (phrase[int(max) - 1] == letter)


def checkEntry(entry: str, predicate: Callable[..., bool]) -> bool:
    m = re.match(
        r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<phrase>[a-z]*)", entry
    )
    return predicate(**m.groupdict())


def solve(inp: List[str], predicate: Callable[..., bool]) -> int:
    return len([entry for entry in inp if checkEntry(entry, predicate)])


print(f"Valid passwords (criterion 1): {solve(lines, check1)}")
print(f"Valid passwords (criterion 2): {solve(lines, check2)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
