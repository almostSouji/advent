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


def find_marker(buff, window_size):
    for i in range(window_size+1, len(buff)):
        chunk = buff[i-window_size-1:i-1]
        if (len(chunk) == len(set(chunk))):
            return i-1


for raw_line in sys.stdin:
    input = raw_line.strip()

    print(find_marker(input, 4))
    print(find_marker(input, 14))
