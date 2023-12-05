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

sds = None
conv = []

for block in open(0).read().split("\n\n"):
    if not sds:
        sds = [int(x) for x in block.split()[1::]]
        continue

    ranges = []
    for line in block.split("\n")[1::]:
        drs, srs, rl = [int(x) for x in line.split()]

        ranges.append((drs, srs, rl))
    conv.append(ranges)


locs = []
for s in sds:
    v = s
    for c in conv:
        for range in c:
            drs, srs, rl = range
            if srs <= v < srs + rl:
                v = drs + (v - srs)
                break
        else:
            v = v
    locs.append(v)

s = min(locs)
print(s)
