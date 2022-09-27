#!/usr/bin/env python3
import sys


def debug(*args, **kwargs):
    "print() to stderr for debuggin purposes"
    print(
        *args,
        **kwargs,
        file=sys.stderr,
    )


for line in sys.stdin:
    if len(line.rstrip()) == 0:
        exit(0)
    print(line.strip())
