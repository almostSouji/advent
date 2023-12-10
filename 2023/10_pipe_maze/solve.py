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
s = None
for x, line in enumerate(open(0)):
    for y, c in enumerate(line.strip()):
        m[x + 1j * y] = c
        if c == "S":
            s = x + 1j * y

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
curr = [(s + d, d, [s]) for d in deltas if (d, m.get(s + d, None)) in n]

tick = 0
while True:
    for i, (c, d, path) in enumerate(curr):
        delta = n.get((d, m[c]), None)
        next = c + delta
        for j, (_, _, p) in enumerate(curr):
            if next in p and i != j:
                break
        else:
            curr[i] = (next, delta, path + [next])
            continue
        break
    else:
        continue
    break

s = len(curr[j][2])
print(s)

assert s == 7066, s
