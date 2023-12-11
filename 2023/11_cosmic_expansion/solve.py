#!/usr/bin/env python3
import sys
import pprint
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

galaxies = []
offset = 0
for x, line in enumerate(open(0)):
    seen = False
    for y, c in enumerate(line.strip()):
        if c == "#":
            galaxies.append(x + offset + 1j * y)
            seen = True
    if not seen:
        offset += 1

galaxies.sort(key=lambda x: x.imag)

c = galaxies.copy()
offset = 0
for i, (a, b) in enumerate(zip(galaxies, galaxies[1:])):
    delta = int(b.imag - a.imag)
    if delta > 1:
        offset += 1j * (delta - 1)
    c[i + 1] += offset

s = 0
for a, b in combinations(c, 2):
    dist = abs(a.real - b.real) + abs(a.imag - b.imag)
    s += int(dist)

print(s)

assert s == 9627977, s
