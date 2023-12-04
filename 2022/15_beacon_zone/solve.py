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
    d = dist(sx + sy * 1j, bx + by * 1j)
    q.append((sx + sy * 1j, d))
    beacons.add(bx + by * 1j)
    minx = min(minx, bx - int(d))
    maxx = max(maxx, bx + int(d))

t = 0

for i in range(minx, maxx + 1):
    p = i + scanline * 1j

    if p in beacons:
        continue

    if any([dist(s, p) <= d for s, d in q]):
        t += 1
        continue

print(t)

N = 4000000
for y in range(0, N + 1):
    ranges = []
    for s, d in q:
        diff = abs(s.imag - y)
        if diff > d:
            continue
        ranges.append((max([s.real - (d - diff), 0]), min([s.real + (d - diff), N])))

    s = sorted(ranges)
    e = 0
    for le, he in s:
        if le > e + 1:
            debug(f"beacon at {(e+1, y)}")
            print(int((e + 1) * 4000000 + y))
            exit(0)
        e = max(e, le, he)
