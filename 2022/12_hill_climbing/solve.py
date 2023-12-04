#!/usr/bin/env python3
import sys
import pprint
from collections import deque, defaultdict


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


l = list(map(lambda x: x.strip(), open(0).readlines()))


def can_visit(a, b):
    a = l[int(a.real)][int(a.imag)]
    b = (
        l[int(b.real)][int(b.imag)]
        if b.real in range(len(l)) and b.imag in range(len(l[0]))
        else None
    )

    if b == None:
        return False

    a = "a" if a == "S" else "z" if a == "E" else a
    b = "a" if b == "S" else "z" if b == "E" else b
    return ord(a) - ord(b) >= -1


g = defaultdict(lambda: [])
start, end, starts = None, None, []

for ri, r in enumerate(l):
    for ci, c in enumerate(r):
        curr = complex(ri, ci)
        if can_visit(curr, curr + 1):
            g.setdefault(curr, []).append(curr + 1)

        if can_visit(curr, curr - 1):
            g.setdefault(curr, []).append(curr - 1)

        if can_visit(curr, curr + 1j):
            g.setdefault(curr, []).append(curr + 1j)

        if can_visit(curr, curr - 1j):
            g.setdefault(curr, []).append(curr - 1j)

        if c == "S":
            start = curr
            starts.append(curr)

        if c == "E":
            end = curr

        if c == "a":
            starts.append(curr)


def dfs(start):
    q = deque()
    q.extend([x] for x in g[start])
    s = set()

    while q:
        path = q.popleft()
        c = path[-1]
        if c == end:
            return len(path)
        if c not in s:
            ns = g[c]
            for n in ns:
                q.append([*path, n])

        s.add(c)


print(f"p1: {dfs(start)}")
print(f"p2: {min(filter(lambda x: x, [dfs(s) for s in starts]))}")
