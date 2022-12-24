#!/usr/bin/env python3
import sys
import pprint
import re


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


m, d = open(0).read().rstrip().split("\n\n")

ns = list(map(int, re.findall(r"\d+", d)))
ts = re.findall(r"\D+", d)
inst = [None]*(len(ns)+len(ts))
inst[::2] = ns
inst[1::2] = ts

f = set()
w = set()
s = None

for ri, r in enumerate(m.splitlines()):
    for ci, c in enumerate(r):
        v = ri+1+ci*1j+1j
        if not s and c != " ":
            s = v
        if c == "#":
            w.add(v)
        elif c == ".":
            f.add(v)

# up -1
# down 1
# right 1j
# left -1j
heading = 1j
p = s


def translate(h):
    match h:
        case 1j:
            return 0
        case -1:
            return 1
        case -1j:
            return 2
        case 1:
            return 3


def wrap(pos, h):
    n = pos - h
    while n in f or n in w:
        n -= h
    n += h
    if n in f:
        return n
    else:
        return pos


for i in inst:
    if type(i) == int:
        for i in range(i):
            n = p + heading
            if n in w:
                break
            elif n in f:
                p = n
            else:
                n = wrap(p, heading)
                p = n
    elif i == "R":
        heading /= 1j
    elif i == "L":
        heading *= 1j

print(int(1000 * p.real + 4 * p.imag + translate(heading)))

# up -1
# down 1
# right 1j
# left -1j
heading = 1j
p = s

for i in inst:
    if type(i) == int:
        for i in range(i):
            n = p + heading
            if n in w:
                break
            elif n in f:
                p = n
            else:
                nc = n
                if n.real < 1 and 51 <= n.imag <= 100 and heading == -1:
                    nh = 1j
                    n = complex(n.imag + 100, 1)
                elif n.imag < 1 and 151 <= n.real <= 200 and heading == -1j:
                    nh = 1
                    n = complex(1, n.real - 100)
                elif n.real < 1 and 101 <= n.imag <= 150 and heading == -1:
                    n = complex(200, n.imag - 100)
                elif n.real > 200 and 1 <= n.imag <= 50 and heading == 1:
                    n = complex(1, n.imag + 100)
                elif n.imag > 150 and 1 <= n.real <= 50 and heading == 1j:
                    nh = -1j
                    n = complex(150 - n.real, 100)
                elif n.imag > 100 and 101 <= n.real <= 150 and heading == 1j:
                    nh = -1j
                    n = complex(150 - n.real, 150)
                elif n.real > 50 and 101 <= n.imag <= 150 and heading == 1:
                    nh = -1j
                    n = complex(n.imag - 50, 100)
                elif n.imag > 100 and 51 <= n.real <= 100 and heading == 1j:
                    nh = -1
                    n = complex(50, n.real + 50)
                elif n.real > 150 and 51 <= n.imag <= 100 and heading == 1:
                    nh = -1j
                    n = complex(n.imag + 100, 50)
                elif n.imag > 50 and 151 <= n.real <= 200 and heading == 1j:
                    nh = -1
                    n = complex(150, n.real - 100)
                elif n.real < 101 and 1 <= n.imag <= 50 and heading == -1:
                    nh = 1j
                    n = complex(n.imag + 50, 51)
                elif n.imag < 51 and 51 <= n.real <= 100 and heading == -1j:
                    nh = 1
                    n = complex(101, n.real - 50)
                elif n.imag < 51 and 1 <= n.real <= 50 and heading == -1j:
                    nh = 1j
                    n = complex(150 - n.real, 1)
                elif n.imag < 1 and 101 <= n.real <= 150 and heading == -1j:
                    nh = 1j
                    n = complex(150 - n.real, 51)

                if n not in f and n not in w:
                    debug(f"p {p} h {heading} nc {nc} n {n}")
                assert n in f or n in w, "valid coordinate"

                if n != nc:
                    debug(f"warped from {nc} to {n}")
                    assert 129+100j in w

                if n not in w:
                    p = n
                    heading = nh
        pass
    elif i == "R":
        heading /= 1j
    elif i == "L":
        heading *= 1j

print(int(1000 * p.real + 4 * p.imag + translate(heading)))
