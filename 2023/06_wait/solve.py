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

lines = []
for line in open(0).readlines():
    lines.append([int(x) for x in line.split()[1::]])

races = list(zip(*lines))


s = 1
for t, d in races:
    wins = 0
    for h in range(1, t):
        sp = t - h
        dist = sp * h
        if dist > d:
            wins += 1

    s *= wins

print(s)
