import time
from typing import List, Tuple
from functools import reduce
import operator

begin = time.time()

###

TREESYMBOL = "#"
SLOPE1 = (1, 3)
SLOPES = [(1, 1), (1, 5), (1, 7), (2, 1)]

with open("input.txt", "r") as file:
    lines = file.readlines()


def checkRoute(lines: List[str], move: Tuple[int, int]) -> int:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    width = len(lines[0]) - 1
    length = len(lines)
    cur = (0, 0)
    count = 0

    while cur[0] < length:
        if lines[cur[0]][cur[1]] == TREESYMBOL:
            count += 1
        cur = (cur[0] + move[0], (cur[1] + move[1]) % width)
    return count


###

end = time.time()

part1 = checkRoute(lines, SLOPE1)
part2 = reduce(operator.mul, [part1, *[checkRoute(lines, slope) for slope in SLOPES]])

print(f"Part 1: Trees hit: {part1}")
print(f"Part 2: Tree product over all routes: {part2}")
print(f"Runtime: {(end - begin) * 1000}ms")
