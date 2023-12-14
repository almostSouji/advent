#!/usr/bin/env python3

grid = open(0).read().split("\n")
transposed = list(list(line) for line in zip(*grid))


def sort(l):
    changed = True
    while changed:
        changed = False
        for i in range(len(l)):
            if l[i] == "." and i + 1 in range(len(l)) and l[i + 1] == "O":
                l[i] = "O"
                l[i + 1] = "."
                changed = True


s = 0
for line in transposed:
    sort(line)
    s += sum([len(line) - i for i, c in enumerate(line) if c == "O"])

print(s)

assert s == 106990, s
