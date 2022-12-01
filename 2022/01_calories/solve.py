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

elves = []
current_elve = []
for raw_line in sys.stdin:
    line = raw_line.strip()
    if len(line) == 0:
        elves.append(sum(current_elve))
        current_elve = []
        continue
    current_elve.append(int(line))

elves.append(sum(current_elve))

print(max(elves))
print(sum(sorted(elves)[-3:]))

###

end = time.time()
debug(f"Runtime: {(end - begin) * 1000}ms")