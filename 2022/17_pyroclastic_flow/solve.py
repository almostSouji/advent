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
    a = ["".join(["#" if c+r*1j in s else "." for c in range(7)])
         for r in range(int(get_h()+5))]
    a.reverse()
    for row in a:
        debug(row)


####

def s1(h):
    return [2+h*1j, 3+h*1j, 4+h*1j, 5+h*1j]


def s2(h):
    return [3+2j+h*1j, 2+1j+h*1j, 3+1j+h*1j, 4+1j+h*1j, 3+h*1j]


def s3(h):
    return [4+2j+h*1j, 4+1j+h*1j, 2+h*1j, 3+h*1j, 4+h*1j]


def s4(h):
    return [2+3j+h*1j, 2+2j+h*1j, 2+1j+h*1j, 2+h*1j]


def s5(h):
    return [2+1j+h*1j, 3+1j+h*1j, 2+h*1j, 3+h*1j]


rocks = set()


def is_collision(a):
    return bool(set(a) & rocks)


def r(rock):
    n = [x+1 for x in rock]
    if is_collision(n):
        return rock
    if sorted(map(lambda x: x.real, n))[-1] > 6:
        return rock
    return n


def l(rock):
    n = [x-1 for x in rock]
    if is_collision(n):
        return rock
    if sorted(map(lambda x: x.real, n))[0] < 0:
        return rock
    return n


def d(rock):
    n = [x-1j for x in rock]
    if is_collision(n):
        return False
    if sorted(map(lambda x: x.imag, n))[0] < 0:
        return False
    return n


def get_h():
    if not rocks:
        return -1
    return max(map(lambda x: x.imag, rocks))


c = open(0).read().strip()
types = [s1, s2, s3, s4, s5]

p = 0

for i in range(0, 2023):

    rock = types[i % 5](get_h()+4)
    while True:
        match(c[p % len(c)]):
            case ">":
                rock = r(rock)
            case "<":
                rock = l(rock)
        p += 1

        rock_before = [x for x in rock]
        rock = d(rock)
        if not rock:
            rock = rock_before
            break

    rocks.update(rock)


print(get_h()-1)
