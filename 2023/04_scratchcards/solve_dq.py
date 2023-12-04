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

cards = dict()
todo = deque()

s = 0
for i, line in enumerate(open(0)):
    i = i + 1
    _wnstr, nstr = line.strip().split(" | ")
    wns = [int(x) for x in _wnstr.split()[2::]]
    ns = [int(x) for x in nstr.split()]
    matches = [x for x in ns if x in wns]

    nm = len(matches)
    score = 2 ** (nm - 1) if nm > 0 else 0
    s += score

    c = (i, nm, score)
    cards[i] = c
    todo.append(c)

print(s)

s2 = 0

while todo:
    s2 += 1
    val = todo.popleft()
    i, nm, score = val

    for j in range(i + 1, i + nm + 1):
        todo.append(cards[j])

print(s2)

assert s == 19855, s
assert s2 == 10378710, s2
