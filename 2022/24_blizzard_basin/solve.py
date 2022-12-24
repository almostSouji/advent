#!/usr/bin/env python3
import sys
import pprint
from collections import deque
from math import lcm, gcd


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


blizzards = [set() for _ in range(4)]
for ri, row in enumerate(open(0).readlines()[1:]):
    for ci, col in enumerate(row.strip()[1:]):
        i = "><v^".find(col)
        if i >= 0:
            blizzards[i].add((ri, ci))

# consistent with ><v^
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

mins = 0
# r c time
s = (-1, 0, 0)
g = (ri, ci-1)

visited = set()
q = deque([s])
rep = lcm(ri, ci)

while q:
    r, c, t = q.popleft()
    t += 1

    for rd, cd in deltas + [(0, 0)]:
        nr = r+rd
        nc = c+cd

        if (nr, nc) == g:
            print(t)
            exit(0)

        if (nr, nc) != (-1, 0):
            if nr < 0 or nr >= ri:
                continue
            if nc < 0 or nc >= ci:
                continue
        for bi, (dbr, dbc) in enumerate(deltas):
            bliz = blizzards[bi]

            p = pr, pc = ((nr - (dbr * t)), (nc - (dbc * t)))
            pn = (pr % ri, pc) if bi == 2 or bi == 3 else (pr, pc % ci)

            if pn in bliz:
                break
        else:
            # no blizzard in the way
            k = (nr, nc, t % rep)
            if k in visited:
                # exact state already seen
                continue

            visited.add(k)
            q.append((nr, nc, t))
