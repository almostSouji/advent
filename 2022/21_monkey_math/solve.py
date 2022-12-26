#!/usr/bin/env python3
import sys
import pprint
import sympy


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


lines = [x.strip() for x in open(0).readlines()]
l2 = [x for x in lines]
ms = {}


for x in lines:
    name, exp = x.split(": ")
    if exp.isdigit():
        ms[name] = int(exp)
    else:
        l, op, r = exp.split(" ")
        if l in ms and r in ms:
            ms[name] = eval(f"{ms[l]} {op} {ms[r]}")
        else:
            lines.append(x)

r = ms["root"]
print(f"p1: {int(r)}")

ms = {"humn": sympy.Symbol("x")}
ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for x in l2:
    name, exp = x.split(": ")

    if name in ms:
        continue
    if exp.isdigit():
        ms[name] = sympy.Integer(exp)
    else:
        l, op, r = exp.split(" ")
        if l in ms and r in ms:
            if name == "root":
                print(f"p2: {sympy.solve(ms[l] - ms[r])[0]}")
                break
            ms[name] = ops[op](ms[l], ms[r])
        else:
            l2.append(x)
