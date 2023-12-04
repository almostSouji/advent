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


def _strip(lines):
    for raw_line in lines:
        yield raw_line.strip()


def _move(lines):
    pos = (0, 0)
    yield pos
    for line in lines:
        dir, n = line.split(" ")
        for _ in range(int(n)):
            pos = step_h(pos, dir)
            yield pos


def step_h(h_pos, dir):
    h_x, h_y = h_pos
    match dir:
        case "R":
            return (h_x + 1, h_y)
        case "L":
            return (h_x - 1, h_y)
        case "U":
            return (h_x, h_y + 1)
        case "D":
            return (h_x, h_y - 1)


def sign(a):
    return a // abs(a)


def _catchup(positions):
    tail = (0, 0)
    yield tail
    for h_x, h_y in positions:
        t_x, t_y = tail
        d_x, d_y = h_x - t_x, h_y - t_y
        if abs(d_x) <= 1 and abs(d_y) <= 1:
            continue
        if abs(d_x) < abs(d_y):
            tail = (h_x, t_y + sign(d_y))
        elif abs(d_x) > abs(d_y):
            tail = (t_x + sign(d_x), h_y)
        else:
            tail = (t_x + sign(d_x), t_y + sign(d_y))

        yield tail


lines = list(_strip(sys.stdin))

print(len(set(_catchup(_move(lines)))))
print(
    len(
        set(
            _catchup(
                _catchup(
                    _catchup(
                        _catchup(
                            _catchup(
                                _catchup(_catchup(_catchup(_catchup(_move(lines)))))
                            )
                        )
                    )
                )
            )
        )
    )
)
