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

outcome_grid = [
    [3, 0, 6],  # r vs [r, p, s]
    [6, 3, 0],  # p vs [r, p, s]
    [0, 6, 3],  # s vs [r, p, s]
]

choices_them = ["A", "B", "C"]
choices_me = ["X", "Y", "Z"]
needed_outcome_for_them = [6, 3, 0]  # [X =loose Y = draw Z = win]


def resolve_action(id: str):
    if id in choices_me:
        return choices_me.index(id)
    return choices_them.index(id)


sum = 0
sum2 = 0
for raw_line in sys.stdin:
    line = raw_line.strip()
    if len(line) <= 1:
        continue
    [them_string, me_string] = line.split()
    [them, me] = [resolve_action(them_string), resolve_action(me_string)]
    sum += outcome_grid[me][them] + me + 1

    action = needed_outcome_for_them[me]
    choose = outcome_grid[them].index(action)
    sum2 += outcome_grid[choose][them] + choose + 1

print(sum)
print(sum2)

###

end = time.time()
debug(f"Runtime: {(end - begin) * 1000}ms")
