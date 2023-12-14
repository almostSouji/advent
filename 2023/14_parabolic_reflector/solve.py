#!/usr/bin/env python3
from icecream import ic

grid = [list(x) for x in open(0).read().splitlines()]


def h(grid):
    return tuple([tuple(line) for line in grid])


def sort_grid(grid):
    [sort(line) for line in grid]


def sort(l):
    changed = True
    while changed:
        changed = False
        for i in range(len(l)):
            if l[i] == "." and i + 1 in range(len(l)) and l[i + 1] == "O":
                l[i] = "O"
                l[i + 1] = "."
                changed = True


def transpose(grid):
    return list(list(line) for line in zip(*grid))


def turn(grid):
    for i in range(4):
        grid = transpose(grid)
        sort_grid(grid)
        grid = [x[::-1] for x in grid]

    return grid


def score(grid):
    return sum(
        [sum([len(line) - i for i, c in enumerate(line) if c == "O"]) for line in grid]
    )


c = transpose([line.copy() for line in grid])
sort_grid(c)
s = score(c)

m = dict()

for i in range(10):
    grid = turn(grid)
    hash = h(grid)
    if hash in m:
        ic(i)
        break
    else:
        m[hash] = i
    ic(grid)

ic(h(grid))

assert s == 136, s
exit(0)
assert s == 106990, s
