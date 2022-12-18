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


def debug_plot_set(s):
    h = max(map(lambda x: x.imag, s))
    a = ["".join(["#" if c+r*1j in s else "." for c in range(7)])
         for r in range(int(h+3))]
    a.reverse()
    for row in a:
        print(row)

####


SHAPES = [
    [0, 1, 2, 3],
    [0+1j, 1+1j, 2+1j, 1, 1+2j],
    [0, 1, 2, 2+1j, 2+2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1+1j]
]


def is_collision(a, rocks):
    for c in a:
        if c.real not in range(0, 7):
            return True
        if c.imag < 0:
            return True

    return bool(set(a) & rocks)


def skyline(s):
    res = [-1] * 7

    for x in s:
        r = int(x.real)
        i = int(x.imag)

        res[r] = max(res[r], i)

    f = max(res)
    return tuple(x - f for x in res)


jets = [1 if x == ">" else -1 for x in input()]

T = 1000000000000


def solve(n):
    rocks = set()
    states = {}

    ji = 0
    si = 0
    i = 0
    h = -1

    while i <= n:
        rock = [x+2+(h+4)*1j for x in SHAPES[si]]
        while True:
            jo = jets[ji]
            nex = [x+jo for x in rock]
            if not is_collision(nex, rocks):
                rock = nex

            ji = (ji + 1) % len(jets)

            nex = [x-1j for x in rock]
            if not is_collision(nex, rocks):
                rock = nex
            else:
                break

        i += 1
        rocks.update(rock)
        h = max(x.imag for x in rocks)
        si = (si+1) % len(SHAPES)

        sky = skyline(rocks)
        key = (si, ji, sky)

        if key in states:
            h_prev, i_prev = states[key]
            h_delta = h - h_prev
            i_delta = i+1 - i_prev

            todo = n - i+1
            repetitions = todo // i_delta

            h_skipped = h_delta * repetitions + 1
            i += i_delta * repetitions

            states = {}
        else:
            states[key] = (h, i+1)

    return(int(h-1 + h_skipped))


print(f"p1: {solve(2022)} -1, off by one :(")
print(f"p2: {solve(T)}")
