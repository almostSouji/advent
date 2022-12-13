#!/usr/bin/env python3
import sys
import pprint
from functools import cmp_to_key


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


def validate(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == list and type(b) == list:
        for x, y in zip(a, b):
            r = validate(x, y)
            if r:
                return r
        return len(a) - len(b)

    a, b = a if isinstance(a, list) else [a], b if isinstance(b, list) else[b]
    return validate(a, b)


l = []
t = 0
for i, chunk in enumerate(open(0).read().strip().split("\n\n")):
    a, b = map(eval, chunk.split("\n"))
    l += [a, b]
    res = validate(a, b)

    if res < 0:
        t += i + 1

print(f"part 1: {t}")

l += [[[2]], [[6]]]
s = list(map(str, sorted(l, key=cmp_to_key(validate))))
pi1, pi2 = (s.index("[[2]]")+1), (s.index("[[6]]")+1)

print(f"par 2: {pi1*pi2}")
