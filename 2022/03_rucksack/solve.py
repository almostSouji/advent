#!/usr/bin/env python3
import sys
import pprint
from functools import reduce

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

def score(c: chr):
    offset = ord("A") - 27 if c.isupper() else ord("a") - 1
    return ord(c) - offset

scores = []
group_scores = []
curr_group = []
for raw_line in sys.stdin:
    line = raw_line.strip()
    if len(line) == 0:
        continue

    curr_group.append(set(line))
    if len(curr_group) == 3:
        common_item = reduce(lambda a, b: a & b, curr_group).pop()
        group_scores.append(score(common_item))
        curr_group = []

    breakpoint = int(len(line) / 2)
    [fst, snd] = [set(line[:breakpoint]), set(line[breakpoint:])]
    dupe = (fst & snd).pop()
    scores.append(score(dupe))

print(sum(scores))
print(sum(group_scores))