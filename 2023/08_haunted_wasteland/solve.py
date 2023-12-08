#!/usr/bin/env python3
import sys
import pprint
from math import lcm


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

m = {}

inst = None
for line in open(0):
    line = line.strip()
    if not inst:
        inst = line
        continue
    if not len(line):
        continue

    nodename, node = line.split(" = ")
    a, b = [x.strip("()") for x in node.split(", ")]

    m[nodename] = (nodename, a, b)

s = 0
node = m["AAA"]
while True:
    i = s % len(inst)
    name, l, r = node

    if name == "ZZZ":
        break

    if inst[i] == "L":
        node = m[l]
    else:
        node = m[r]

    s += 1

nodes = [x for x in m.values() if x[0].endswith("A")]
seen = [0 for _ in range(len(nodes))]

c = 0
while nodes:
    i = c % len(inst)

    if 0 not in seen:
        break

    for ni, node in enumerate(nodes):
        name, l, r = node
        if name.endswith("Z"):
            seen[ni] = c
        if inst[i] == "L":
            nodes[ni] = m[l]
        else:
            nodes[ni] = m[r]
    c += 1

s2 = lcm(*seen)


print(s)
print(s2)
assert s == 14257, s
assert s2 == 16187743689077, s2
