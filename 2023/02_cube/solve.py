#!/usr/bin/env python3

available_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

s = 0
s2 = 0
for i, line in enumerate(open(0)):
    game, rounds = line.split(":")
    minimums = {"red": 0, "green": 0, "blue": 0}

    possible = True
    for run in line.split(": ")[1].split("; "):
        for cube in run.split(", "):
            num, color = cube.split()
            num = int(num)

            minimums[color] = max(minimums[color], num)

            if available_cubes.get(color, 0) < num:
                possible = False
    if possible:
        s += i + 1

    power = 1
    for val in minimums.values():
        power *= val
    s2 += power

print(s)
print(s2)

assert s == 2716, s
assert s2 == 72227, s2
