#!/usr/bin/env python3
import sys
import pprint
import re
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


# 30 mins
# flowrate: pressure/min
# AA start
# minute move
# minute ope

ns = {}
flo = {}
nonempty = []

for line in open(0):
    [v, *n] = re.findall(r"[A-Z]{2}", line.strip())
    [f] = re.findall(r"\d+", line.strip())
    ns[v] = n
    flo[v] = int(f)

dst = {}

for v in flo:
    if v != "AA" and not flo[v]:
        continue

    if v != "AA":
        nonempty.append(v)

    dst[v] = {v: 0, "AA": 0}
    visited = {v}

    q = deque([(0, v)])

    while q:
        d, p = q.popleft()
        for n in ns[p]:
            if n in visited:
                continue
            visited.add(n)
            if flo[n]:
                dst[v][n] = d + 1
            q.append((d + 1, n))

    del dst[v][v]
    if v != "AA":
        del dst[v]["AA"]

ids = {}

for i, e in enumerate(nonempty):
    ids[e] = i

cache = {}


def dfs(time, v, bitmask):
    if (time, v, bitmask) in cache:
        return cache[(time, v, bitmask)]
    maxv = 0
    for n in dst[v]:
        bit = 1 << ids[n]
        if bitmask & bit:  # if already set
            continue
        rem = time - dst[v][n] - 1  # open valve
        if rem <= 0:
            continue
        maxv = max(maxv, dfs(rem, n, bitmask | bit) + flo[n] * rem)

    cache[(time, v, bitmask)] = maxv
    return maxv


print(dfs(30, "AA", 0))

b = (1 << len(nonempty)) - 1  # all valves open

m = 0
for i in range((b + 1) // 2):
    m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b ^ i))

print(m)
