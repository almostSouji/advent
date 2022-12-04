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


c = 0
c2 = 0
total = set()
for raw_line in sys.stdin:
    line = raw_line.strip()
    if len(line) == 0:
        continue
    (fst, snd) = line.split(",")
    (fst_start, fst_end) = fst.split("-")
    (snd_start, snd_end) = snd.split("-")

    fst_s = set(range(int(fst_start), int(fst_end)+1))
    snd_s = set(range(int(snd_start), int(snd_end)+1))

    if fst_s.issubset(snd_s) or fst_s.issuperset(snd_s):
        c += 1

    if not fst_s.isdisjoint(snd_s):
        c2 += 1

print(c)
print(c2)
