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

count = dict()

s = 0
for i, line in enumerate(open(0)):
    _wnstr, nstr = line.strip().split(" | ")
    wns = [int(x) for x in _wnstr.split()[2::]]
    ns = [int(x) for x in nstr.split()]
    matches = [x for x in ns if x in wns]

    nm = len(matches)
    s += 2 ** (nm - 1) if nm > 0 else 0

    count[i] = count.get(i, 1)

    for j in range(i + 1, i + nm + 1):
        count[j] = count.get(j, 1) + count[i]

print(s)

s2 = sum(count.values())
print(s2)

assert s == 19855, s
assert s2 == 10378710, s2
