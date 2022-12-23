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
    if name == "root":
        ns["root"] = (a, "=", b)
    r = f(a, s, b)
    if type(r) == int or type(r) == float:
        ns[n] = r
        return True
    else:
        td.append((n, r))
        return False


for line in open(0):
    n, s = line.strip().split(': ')
    if s.isdigit():
        ns[n] = int(s)
    else:
        v = s.split(" ")
        update(n, v)

step = True
while td and step:
    n, v = td.popleft()
    step = update(n, v)

debug(ns)


def equation(a):
    debug(a)
    if a == "humn":
        return "X"
    if type(a) == float or type(a) == int:
        return str(a)
    if a in ns:
        return ns[a]
    else:
        return a


a, _, b = ns["root"]
print(equation(a), "=", equation(b))
