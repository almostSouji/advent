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


def pp(l):
    for row in l:
        print("".join([str(elem) for elem in row]))


####


rx = 1
relevant_cycles = range(20, 221, 40)

inst_buffer = []
pause = False
res = []

display = [[" " for _ in list(range(0, 40))] for _ in range(0, 6)]

for cycle in range(1, 241):
    if not pause and len(inst_buffer) == 0:
        line = sys.stdin.readline().strip()
        match line.split(" "):
            case "addx", x:
                inst_buffer.append(int(x))
                pause = True

    index = cycle - 1
    display[index // 40][index % 40] = (
        "▓" if index % 40 in range(rx - 1, rx + 2) else "░"
    )

    if cycle in relevant_cycles:
        res.append(cycle * rx)

    if not pause and len(inst_buffer) > 0:
        rx += inst_buffer.pop()
    elif pause:
        pause = False

print(sum(res))
pp(display)
