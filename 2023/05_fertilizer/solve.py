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
for block in open(0).read().split("\n\n"):
    if not seeds:
        seeds = [int(x) for x in block.split()[1::]]
        continue

    rs = []
    for line in block.split("\n")[1::]:
        dest_start, src_start, range_len = [int(x) for x in line.split()]
        rs.append((dest_start, src_start, range_len))

    converted = []
    for seed in seeds:
        for r in rs:
            dest_start, src_start, range_len = r

            if src_start <= seed < src_start + range_len:
                converted.append(dest_start + (seed - src_start))
                break
        else:
            converted.append(seed)
    seeds = converted

s = min(seeds)
print(s)

assert s == 510109797, s
