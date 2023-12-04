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

cards = dict()

s = 0
for i, line in enumerate(open(0)):
    i = i + 1
    _wnstr, nstr = line.strip().split(" | ")
    wns = [int(x) for x in _wnstr.split()[2::]]
    ns = [int(x) for x in nstr.split()]
    matches = [x for x in ns if x in wns]
    s += 2 ** (len(matches) - 1) if len(matches) else 0

print(s)

assert s == 19855, s
