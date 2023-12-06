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

lines = []
race = []
for line in open(0).readlines():
    lines.append([int(x) for x in line.split()[1::]])
    race.append(int("".join(line.split()[1::])))

races = list(zip(*lines))


s = 1
for t, d in races:
    wins = 0
    for h in range(1, t):
        sp = t - h
        dist = sp * h
        if dist > d:
            wins += 1

    s *= wins

print(s)

s2 = 0
t, d = race
for h in range(1, t):
    sp = t - h
    dist = sp * h
    if dist > d:
        # iterating to the minimum
        # h is the minimum time that wins
        # everything up to race time - the minimum time we need to win also wins
        # time - min + 1 (inclusive)
        # max - min
        s2 = t - h + 1 - h
        break

print(s2)

assert s == 608902, s
assert s2 == 46173809, s2
