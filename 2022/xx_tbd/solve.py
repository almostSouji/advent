#!/usr/bin/env python3
import sys
import pprint
import time

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

begin = time.time()

####

for raw_line in sys.stdin:
    line = raw_line.strip()
    if len(line) == 0:
        continue


###

end = time.time()
debug(f"Runtime: {(end - begin) * 1000}ms")