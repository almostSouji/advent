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


def link(l):
    z = None
    for i in range(len(l)):
        l[i][0] = l[(i - 1) % len(l)]
        l[i][2] = l[(i + 1) % len(l)]
        if l[i][1] == 0:
            z = l[i]
    return z


def mix(l, times):
    for _ in range(times):
        for e in l:
            el, v, er = e
            p = e
            if v == 0:
                continue

            el[2] = er
            er[0] = el

            if v > 0:
                for _ in range(v % (len(l) - 1)):
                    p = p[2]
                pr = p[2]
                p[2] = e
                pr[0] = e
                e[0] = p
                e[2] = pr

            if v < 0:
                for _ in range(-v % (len(l) - 1)):
                    p = p[0]

                pl = p[0]
                p[0] = e
                pl[2] = e
                e[0] = pl
                e[2] = p


def getrelevant(start, n, interval):
    res = []
    p = start
    for _ in range(n):
        for _ in range(interval):
            p = p[2]
        res.append(p[1])
    return res


lines = open(0).readlines()

# L, V, R
l = [[None, int(x), None] for x in lines]
z = link(l)
mixed = mix(l, 1)


print(f"part1: {sum(getrelevant(z, 3, 1000))}")

PKEY = 811589153

l2 = [[None, int(x) * PKEY, None] for x in lines]
z2 = link(l2)
mixed = mix(l2, 10)

print(f"part2: {sum(getrelevant(z2, 3, 1000))}")
