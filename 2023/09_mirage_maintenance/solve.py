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

s = 0
s2 = 0
for line in open(0).readlines():
    line = [int(x) for x in line.split()]
    b = []
    while line.count(0) != len(line):
        b.append(line)
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    b.append(line)
    b.reverse()
    pred = 0
    past = 0
    for e in b:
        past = e[0] - past
        pred += e[-1]
    s += pred
    s2 += past

print(s)
print(s2)

assert s == 2005352194, s
assert s2 == 1077, s2
