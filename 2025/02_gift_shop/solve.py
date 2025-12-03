#!/user/bine/env python3

from math import ceil

with open(0) as f:
    ranges = [tuple(int(y) for y in x.split("-")) for x in f.read().strip().split(",")]
    f.close()

invalid_1 = []
invalid_2 = []
for lower, upper in ranges:
    for i in range(lower, upper + 1):
        id = str(i)
        if (len(id) % 2) == 0:
            mid = len(id) // 2

            fst, snd = id[:mid], id[mid:]
            if fst == snd:
                invalid_1.append(i)

        for j in range(1, (len(id) // 2) + 1):
            chunk = id[0:j]
            times = len(id) / j
            if chunk * ceil(times) == id:
                invalid_2.append(i)
                break

print(f"part1: {sum(invalid_1)}")
print(f"part1: {sum(invalid_2)}")
