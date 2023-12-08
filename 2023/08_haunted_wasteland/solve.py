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

print(s)
assert s == 14257, s
