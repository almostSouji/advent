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


t = 0
for i, chunk in enumerate(open(0).read().strip().split("\n\n")):
    a, b = map(eval, chunk.split("\n"))
    res = validate(a, b)

    if res < 0:
        t += i + 1

print(f"part 1: {t}")
