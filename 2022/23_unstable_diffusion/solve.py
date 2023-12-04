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


def dp(s):
    mx = min(x.real for x in s)
    Mx = max(x.real for x in s)
    my = min(x.imag for x in s)
    My = max(x.imag for x in s)

    for r in range(int(mx), int(Mx + 1)):
        for c in range(int(my), int(My + 1)):
            if r + c * 1j in s:
                debug("#", end="")
            else:
                debug(".", end="")
        debug()
    debug()


####


es = set()

for ri, r in enumerate(open(0).readlines()):
    for ci, c in enumerate(r):
        if c == "#":
            es.add(ri + ci * 1j)

cons = [
    [-1 - 1j, -1, -1 + 1j],  # N
    [1 - 1j, 1, 1 + 1j],  # S
    [-1 - 1j, -1j, 1 - 1j],  # W
    [-1 + 1j, 1j, 1 + 1j],  # E
]

round = 0
while True:
    round += 1
    moved = 0

    pr = {}
    for e in es:
        p = None
        no = 0
        for c1, c2, c3 in cons:
            n1, n2, n3 = e + c1, e + c2, e + c3
            occ = any(x in es for x in [n1, n2, n3])
            if not occ:
                no += 1
                if p == None:
                    p = n2
        if no == 4:
            continue

        if p != None:
            if p not in pr:
                pr[p] = []

            pr[p].append(e)

    for c, p in pr.items():
        if len(p) == 1:
            moved += 1
            es.remove(p[0])
            es.add(c)

    cons = cons[1:] + [cons[0]]

    if round == 10:
        mx = my = float("inf")
        Mx = My = float("-inf")

        for e in es:
            mx = min(e.real, mx)
            Mx = max(e.real, Mx)
            my = min(e.imag, my)
            My = max(e.imag, My)

        t = 0
        for r in range(int(mx), int(Mx + 1)):
            for c in range(int(my), int(My + 1)):
                if r + c * 1j not in es:
                    t += 1

        print(f"p1: {t}")

    if not moved:
        break

print(f"p2: {round}")
