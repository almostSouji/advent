#!/usr/bin/env python3
import sys
import pprint
import re


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


m, d = open(0).read().rstrip().split("\n\n")

ns = list(map(int, re.findall(r"\d+", d)))
ts = re.findall(r"\D+", d)
inst = [None]*(len(ns)+len(ts))
inst[::2] = ns
inst[1::2] = ts

floor = set()
walls = set()
start = None

for ri, r in enumerate(m.splitlines()):
    for ci, c in enumerate(r):
        v = ri+1+ci*1j+1j
        if not start and c != " ":
            start = v
        if c == "#":
            walls.add(v)
        elif c == ".":
            floor.add(v)

"""
Portals are defined by their spawn point (left or topmost point) and the entrance direction
Connections are defined by two portals and if the connection inverts delta to the spawn point
"""
PORTAL_CONNECTIONS = [
    ((51j, -1), (151, -1j), False),  # 2U, 6L
    ((101j, -1), (201+1j, 1), False),  # 1U, 6D
    ((1+151j, 1j), (101+101j, 1j), True),  # 1R, 4R
    ((151+51j, 1), (151+51j, 1j), False),  # 4D, 6R
    ((1+50j, -1j), (101, -1j), True),  # 2L, 5L
    ((51+50j, -1j), (100+1j, -1), False),  # 3L, 5U
    ((51+101j, 1), (51+101j, 1j), False)  # 1D, 3R
]


def portal_delta(port, pos, heading):
    spawn, direction = port
    if heading != direction:
        return -1

    if direction == 1 or direction == -1 and pos.real == spawn.real:
        if pos.imag in range(int(spawn.imag), int(spawn.imag + 50)):
            return abs(pos.imag - spawn.imag)
    else:
        if pos.real in range(int(spawn.real), int(spawn.real+50)):
            return abs(pos.real - spawn.real)
    return -1


def wrap(pos, h):
    n = pos - h
    while n in floor or n in walls:
        n -= h
    n += h
    if n in floor:
        return n, h
    else:
        return None


def wrap_cube(pos, h):
    assert pos not in floor and pos not in walls, pos

    n = pos
    for a, b, flip in PORTAL_CONNECTIONS:
        # delta to portal spawns, -1 if portal n/a
        a_delta = portal_delta(a, n, h)
        b_delta = portal_delta(b, n, h)

        # determien out portal and applicable delta
        if a_delta >= 0:
            delta = a_delta
            out_spawn, out_direction = b
        elif b_delta >= 0:
            delta = b_delta
            out_spawn, out_direction = a
        else:
            # connection not relevant
            continue

        # invert delta, if connection requires it
        if flip:
            delta = 49 - delta

        # translate delta into imag, if required
        if out_direction == 1 or out_direction == -1:
            delta *= 1j

        # apply delta to the out portal spawn point
        n = out_spawn + delta

        # new heading is inverse of in-direction of out portal
        new_heading = -out_direction
        # walk the last step out of the portal
        n += new_heading
        assert n in floor or n in walls

        if n in walls:
            # if wall, discord
            return None
        else:
            # return new position and heading
            assert n in floor, n
            return n, new_heading

    assert False, (pos, h)


def solve(instructions, wrapper):
    heading = 1j
    p = start

    for i in instructions:
        if type(i) == int:
            for i in range(i):
                # test new position
                n = p + heading
                if n in walls:
                    # wall, stop
                    break
                elif n in floor:
                    # floor, commit change
                    p = n
                else:
                    # if not wall or floor, needs to wrap
                    wrap_res = wrapper(n, heading)
                    if wrap_res:
                        # wrap results in non-wall, commit change
                        p, heading = wrap_res
                    else:
                        break
        # turn
        elif i == "R":
            heading /= 1j
        elif i == "L":
            heading *= 1j

    return int(1000 * p.real + 4 * p.imag + [1j, 1, -1j, -1].index(heading))


res1 = solve(inst, wrap)
print(
    f"part 1: {res1}")
assert 164014 == res1, res1

res2 = solve(inst, wrap_cube)
print(f"part 2: {res2}")
assert 47525 == res2, res2
