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

seeds = None
seeds2 = []
for block in open(0).read().split("\n\n"):
    if not seeds:
        seeds = [int(x) for x in block.split()[1::]]

        for i in range(0, len(seeds), 2):
            seeds2.append((seeds[i], seeds[i] + seeds[i + 1]))

        continue

    rs = []
    for line in block.split("\n")[1::]:
        dest_s, src_s, range_l = [int(x) for x in line.split()]
        rs.append((dest_s, src_s, range_l))

    conv = []
    for seed in seeds:
        for r in rs:
            dest_s, src_s, range_l = r

            if src_s <= seed < src_s + range_l:
                delta = dest_s - src_s
                conv.append(seed + delta)
                break
        else:
            conv.append(seed)
    seeds = conv

    conv = []
    for seed in seeds2:
        start, end = seed

        for r in rs:
            dest_s, src_s, range_l = r
            overlap_s = max(start, src_s)
            overlap_e = min(end, src_s + range_l)

            if overlap_s < overlap_e:
                delta = dest_s - src_s

                conv.append((overlap_s + delta, overlap_e + delta))

                if start < overlap_s:
                    seeds2.append((start, overlap_s))
                if end > overlap_e:
                    seeds2.append((end, overlap_e))

                break
        else:
            conv.append(seed)
    seeds2 = conv


start = min(seeds)
print(start)
s2 = min(seeds2)[0]
print(s2)

assert start == 510109797, start
assert s2 == 9622622, s2
