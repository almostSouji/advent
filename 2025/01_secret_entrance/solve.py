#!/user/bine/env python3

dial = 50
count = 0
clicks = 0
for line in open(0):
    line = line.strip()
    op = line[0]
    distance = int(line[1:])

    assert op in ["R", "L"]
    next = dial + distance if op == "R" else dial - distance
    offset = 1 if op == "R" else -1

    zeros = [x for x in range(dial + offset, next + offset, offset) if x % 100 == 0]
    clicks += len(zeros)

    dial = next % 100

    if dial == 0:
        count += 1


print(f"part1: {count}")
print(f"part2: {clicks}")
