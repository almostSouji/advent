#!/usr/bin/env python3
import sys
import pprint
import re
import numpy


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


p = re.compile("[\[ ]([A-Z\d ])[ \]] ?")
p_moves = re.compile("move (\d+) from (\d+) to (\d+)")
lines = []
parsed = False
stacks = []
stacks2 = []

for raw_line in sys.stdin:
    if len(raw_line.strip()) == 0:
        parsed = True
    elif parsed == False:
        m = p.findall(raw_line)
        lines.append(m)
    else:
        if len(stacks) == 0:
            t = numpy.transpose(lines)
            stacks = [[x for x in reversed(
                line) if x != ' ' and not x.isdigit()] for line in t]
            stacks2 = [x[:] for x in stacks]

        n, fro, to = [int(x) for x in p_moves.findall(raw_line)[0]]

        for i in range(n):
            stacks[to-1].append(stacks[fro-1].pop())
        stacks2[to-1].extend(stacks2[fro-1][-n:])
        stacks2[fro-1] = stacks2[fro-1][:-n]

print("".join([x[-1] for x in stacks]))
print("".join([x[-1] if len(x) > 0 else "" for x in stacks2]))
