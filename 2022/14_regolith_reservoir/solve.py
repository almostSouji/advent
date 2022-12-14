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


def betw(x1, y1, x2, y2):
    res = []
    xmin, xmax = sorted([x1, x2])
    ymin, ymax = sorted([y1, y2])
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            res.append(complex(x, y))
    return res


def check(a, s, floor=None):
    if floor and a.imag+1 == floor:
        return a

    if a+1j not in s:
        return a+1j
    if a+1j-1 not in s:
        return a+1j-1
    if a+1j+1 not in s:
        return a+1j+1
    return a


def move(s, floor=None):
    b = None
    a = 500
    while b != a:
        b = a
        a = check(a, s, floor)

        if floor:
            if a == 500:
                return None
        elif (a.imag > abyss):
            return None
    return a


s = set()
abyss = 0

for line in open(0). readlines():
    pairs = list(
        map(lambda x: tuple(map(int, x.split(","))), line.strip().split(" -> ")))
    for i in range(len(pairs)-1):
        (x1, y1), (x2, y2) = pairs[i], pairs[i+1]
        s.update(betw(x1, y1, x2, y2))
        abyss = max(abyss, max(y1, y2))


c = 0
while True:
    r = move(s)
    if r:
        s.add(r)
        c += 1
    else:
        break

print(f"part 1: {c}")

floor = abyss + 2

while True:
    r = move(s, floor)
    if r:
        s.add(r)
        c += 1
    else:
        break

print(f"part 2: {c+1}")
