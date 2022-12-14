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


def betw(a, b):
    res = []
    min_x, max_x = sorted([int(a.real), int(b.real)])
    min_y, max_y = sorted([int(a.imag), int(b.imag)])
    if a.real == b.real:
        for x in range(min_y, max_y+1):
            res.append(complex(a.real, x))
    elif a.imag == b.imag:
        for x in range(min_x, max_x+1):
            res.append(complex(x, a.imag))
    return res


s = set()
e = 500+0j
abyss = 0


def check(a):
    if a+1j in s:
        if a-1+1j in s:
            if a+1+1j in s:
                return a
            else:
                return a+1+1j
        else:
            return a-1+1j
    else:
        return a+1j


def move():
    b = e
    a = e+1j
    while b != a:
        b = a
        a = check(a)

        if (a.imag > abyss):
            return None
    return a


for line in open(0).read().strip().splitlines():
    pairs = list(
        map(lambda x: x.split(","), line.split(" -> ")))
    for i in range(len(pairs)-1):
        a, b = pairs[i], pairs[i+1]
        a = complex(int(a[0]), int(a[1]))
        b = complex(int(b[0]), int(b[1]))
        s.update(betw(a, b))
        abyss = max(abyss, max(a.imag, b.imag))


c = 0
while True:
    r = move()
    if r:
        s.add(r)
        c += 1
    else:
        break

print(f"part 1: {c}")
