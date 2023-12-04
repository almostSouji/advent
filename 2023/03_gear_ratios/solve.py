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

symbols = dict()
numbers = []
deltas = [1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]

for x, line in enumerate(open(0)):
    current_num = ""
    current_coords = []
    for y, s in enumerate(line.strip()):
        if s.isdigit():
            current_num += s
            current_coords.append(x + y * 1j)
        else:
            if len(current_num) > 0:
                numbers.append((int(current_num), current_coords))
                current_num = ""
                current_coords = []
            if s != ".":
                symbols[x + y * 1j] = s
    if len(current_num) > 0:
        numbers.append((int(current_num), current_coords))
        current_num = ""
        current_coords = []

to_del = []
for i, (num, coords) in enumerate(numbers):
    for coord in coords:
        for delta in deltas:
            if coord + delta in symbols:
                break
        else:
            continue
        break
    else:
        to_del.append(i)

for i, index in enumerate(to_del):
    del numbers[index - i]

sol1 = sum([x[0] for x in numbers])
print(sol1)

s = 0
for coord, symbol in symbols.items():
    if symbol == "*":
        nums = []
        for num, num_coord in numbers:
            for delta in deltas:
                if coord + delta in num_coord:
                    nums.append(num)
                    break
        if len(nums) == 2:
            s += nums[0] * nums[1]

print(s)

assert sol1 == 535351, sol1
assert s == 87287096, s
