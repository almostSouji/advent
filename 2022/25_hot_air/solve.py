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


def s_to_d(s):
    t = 0
    for i, sd in enumerate(reversed(s.strip())):
        t += ("=-012".index(sd) - 2) * 5**i
    return t


def d_to_s(d):
    o = ""

    while d:  # while there are partials to convert
        rem = d % 5
        d //= 5

        if rem <= 2:
            o = str(rem) + o
        elif rem == 3:
            d += 1  # add 5 to then compensate:
            o = "=" + o  # 3 - 5 = -2 -> =
        elif rem == 4:
            d += 1  # add 5 to then compensate:
            o = "-" + o  # 4 - 5 = -1 -> -
    return o


print(d_to_s(sum(map(s_to_d, (l.strip() for l in open(0).readlines())))))
