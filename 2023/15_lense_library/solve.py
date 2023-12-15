#!/usr/bin/env python3


def HASH(text):
    cur = 0
    for c in text:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur


s = 0
for inst in open(0).read().split(","):
    s += HASH(inst)

print(s)
