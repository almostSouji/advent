#!/usr/bin/env python3
import sys
import pprint
import re


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


beacons = set()
scanline = 2_000_000
scanline_t = 10
q = []


def dist(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


minx = 99999999999
maxx = 0

for line in open(0).readlines():
    sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
    d = dist(sx+sy*1j, bx+by*1j)
    q.append((sx+sy*1j, d))
    beacons.add(bx + by*1j)
    minx = min(minx, bx - int(d))
    maxx = max(maxx, bx + int(d))

t = 0

for i in range(minx, maxx+1):
    p = i+scanline*1j

    if p in beacons:
        continue

    if any([dist(s, p) <= d for s, d in q]):
        t += 1
        continue

print(t)
