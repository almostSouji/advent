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
inst[::2] = ns  # type: ignore
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
pos = s


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
            n = pos + heading
            if n in w:
                break
            elif n in f:
                pos = n
            else:
                n = wrap(pos, heading)
                pos = n
    elif i == "R":
        heading /= 1j
    elif i == "L":
        heading *= 1j

print(int(1000 * pos.real + 4 * pos.imag + translate(heading)))
