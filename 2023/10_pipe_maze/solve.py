#!/usr/bin/env python3
import sys
import pprint


def debug(*args, pretty=False, **kwargs):
    "print() to stderr for debuggin purposes"
    if pretty:
        pprint.pprint(*args, **kwargs, stream=sys.stderr)
    else:
        print(
            *args,
            **kwargs,
            file=sys.stderr,
        )


####

m = {}
start = None
for x, line in enumerate(open(0)):
    for y, c in enumerate(line.strip()):
        m[x + 1j * y] = c
        if c == "S":
            start = x + 1j * y

n = {
    (1, "|"): 1,
    (-1, "|"): -1,
    (1j, "-"): 1j,
    (-1j, "-"): -1j,
    (1, "L"): 1j,
    (-1j, "L"): -1,
    (1, "J"): -1j,
    (1j, "J"): -1,
    (1j, "7"): 1,
    (-1, "7"): -1j,
    (-1j, "F"): 1,
    (-1, "F"): 1j,
}

deltas = [1, -1, 1j, -1j]
curr = [
    (start + d, d, [start, start + d])
    for d in deltas
    if (d, m.get(start + d, None)) in n
]

lace = None
while True:
    for i, (c, d, path) in enumerate(curr):
        delta = n.get((d, m[c]), None)
        next = c + delta
        for j, (_, _, p) in enumerate(curr):
            if next in p and i != j:
                lace = [*curr[i][2], *reversed(curr[j][2][1:])]
                break
        else:
            curr[i] = (next, delta, path + [next])
            continue
        break
    else:
        continue
    break

s = int(len(lace) / 2)

# find the real symbol of S
assert lace[0] == start

candidates = set("|-LJ7F")
for elem in [lace[-1] - start, lace[1] - start]:
    possible = set()
    for k, v in n.items():
        if v == elem:
            possible.add(k[1])
    candidates &= possible

start_shape = candidates.pop()
m[start] = start_shape

# clean up the maze to not have to deal with weird pipes
for a in range(x + 1):
    for b in range(y + 1):
        coord = a + 1j * b
        if coord not in lace:
            m[coord] = "."

# find the tiles outside the maze
outcoords = set()
for a in range(x + 1):
    inside = False
    seenL = None
    for b in range(y + 1):
        assert a + 1j * b in m
        c = m[a + 1j * b]

        if c == "|":
            assert seenL is None
            inside = not inside
        elif c in "LF":
            assert seenL is None, (a, b, c, seenL)
            seenL = c == "L"
        elif c in "J7":
            assert seenL is not None
            if (seenL and c == "7") or (not seenL and c == "J"):
                inside = not inside
            seenL = None

        coord = a + 1j * b
        if not inside:
            outcoords.add(coord)

# remove the outside tiles and the lace tiles from all tiles to find the surrounded tiles
s2 = len(set(m.keys()) - outcoords - set(lace))

print(s)
print(s2)
assert s == 7066, s
assert s2 == 401, s2
