#!/usr/bin/env python3
import sys
import pprint
from collections import deque


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


ns = {}
td = deque()


def res(v):
    if v in ns:
        return ns[v]
    else:
        return v


def f(a, s, b):
    ar = res(a)
    br = res(b)
    tar = type(ar)
    tbr = type(br)

    if (tar == int or tar == float) and (tbr == int or tbr == float):
        match s:
            case "-":
                return ar - br
            case "+":
                return ar + br
            case "*":
                return ar * br
            case "/":
                return ar / br
    return (ar, s, br)


def update(name, v):
    a, s, b = v
    r = f(a, s, b)
    if type(r) == int or type(r) == float:
        if name == "root":
            print(r)
            exit(0)
        ns[n] = r
    else:
        td.append((n, r))


for line in open(0):
    n, s = line.strip().split(': ')
    if s.isdigit():
        ns[n] = int(s)
    else:
        v = s.split(" ")
        update(n, v)

while td:
    n, v = td.popleft()
    update(n, v)
