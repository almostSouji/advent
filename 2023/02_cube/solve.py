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

total_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

s = 0
s2 = 0
for line in open(0):
    game, rounds = line.split(":")
    _, id = game.split(" ")
    id = int(id)
    minimums = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    possible = True
    for run in rounds.split(";"):
        for cube in run.split(","):
            num, color = cube.strip().split(" ")
            num = int(num)
            available = total_cubes.get(color, 0)

            if minimums.get(color, 0) < num:
                minimums[color] = num

            if available < num:
                possible = False
    if possible:
        s += id
    power = 1
    for val in minimums.values():
        power *= val
    s2 += power

print(s)
print(s2)