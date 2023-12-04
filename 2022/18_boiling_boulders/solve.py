#!/usr/bin/env python3
import sys
import pprint
from collections import deque
from itertools import combinations


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


deltas = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
cubes = {tuple(map(int, (l.strip().split(",")))) for l in open(0).readlines()}

t = 0
mins = [999] * 3
maxs = [-1] * 3

for c in cubes:
    (x, y, z) = c
    ns = set()

    for xd, yd, zd in deltas:
        pn = (x + xd, y + yd, z + zd)
        if pn in cubes:
            ns.add(pn)
        else:
            t += 1

    mins = tuple(map(min, zip(mins, c)))
    maxs = tuple(map(max, zip(maxs, c)))

print(f"part1: {t}")

visited = set()
q = deque([(mins[0] - 1, mins[1] - 1, mins[2] - 1)])
q.append(tuple(mins))

t = 0

while q:
    x, y, z = c = q.popleft()
    ns = set()
    if c not in visited:
        for xd, yd, zd in deltas:
            pn = (x + xd, y + yd, z + zd)

            if not mins[0] - 1 <= pn[0] <= maxs[0] + 1:
                continue

            if not mins[1] - 1 <= pn[1] <= maxs[1] + 1:
                continue

            if not mins[2] - 1 <= pn[2] <= maxs[2] + 1:
                continue

            if pn in cubes:
                t += 1
            else:
                ns.add(pn)
        q.extend(ns)
    visited.add(c)

print(f"part2: {t}")
