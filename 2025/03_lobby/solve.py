#!/user/bine/env python3
from icecream import ic

p1 = 0
for line in open(0):
    bank = line.strip()
    highest_val = 0
    for index, battery in enumerate(bank):
        rest = [int(x) for x in bank[index + 1 :]]
        if len(rest):
            highest_digit = max(rest)
            highest_val = max(int(str(battery + str(highest_digit))), highest_val)

    p1 += highest_val

print(f"part1: {p1}")
