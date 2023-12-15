#!/usr/bin/env python3
import re


def HASH(text):
    cur = 0
    for c in text:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur


s = 0

boxes = [{} for _ in range(256)]
for inst in open(0).read().split(","):
    s += HASH(inst)
    match = re.search(r"(\D{2,6})([=-])(\d)?", inst)
    assert match is not None
    (label, op, d) = match.groups()

    box_id = HASH(label)
    if op == "-":
        boxes[box_id].pop(label, None)
    else:
        assert op == "="
        assert d is not None
        d = int(d)
        boxes[box_id][label] = d

s2 = 0
for i, b in enumerate(boxes):
    for j, (label, foc) in enumerate(b.items()):
        s2 += (1 + i) * (j + 1) * foc

print(s)
print(s2)

assert s == 503487, s
assert s2 == 261505, s2
