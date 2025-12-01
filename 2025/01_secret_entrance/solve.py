#!/user/bine/env python3


dial = 50
count = 0
for line in open(0):
    line = line.strip()
    op = line[0]
    distance = int(line[1:])

    assert op in ["R", "L"]
    next = dial + distance if op == "R" else dial - distance
    dial = next % 100

    if dial == 0:
        count += 1

print(f"part1: {count}")
