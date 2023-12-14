#!/usr/bin/env python3
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
    return sum([line.count("O") * (len(grid) - i) for i, line in enumerate(grid)])


c = transpose([line.copy() for line in grid])
sort_grid(c)
c = transpose(c)
s = score(c)

m = dict()
states = []

N = 1000000000
cycle = (-1, -1)
for i in range(N):
    grid = turn(grid)
    hash = h(grid)
    if hash in m:
        cycle = (m[hash], i)
        print(cycle)
        break
    else:
        m[hash] = i
    states.append(hash)

first, repeated = cycle

final_i = (N - first) % (repeated - first) + first - 1
grid = states[final_i]

s2 = score(grid)

print(s)
print(s2)

assert s == 106990, s
assert s2 == 100531, s2
