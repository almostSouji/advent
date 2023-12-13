#!/usr/bin/env python3
from icecream import ic


def seek(lines):
    found = None
    for pivot in range(0, len(lines) - 1):
        for r in range(pivot + 1, len(lines)):
            l = pivot - (r - pivot - 1)

            left = lines[l] if l in range(0, len(lines)) else None
            right = lines[r] if r in range(0, len(lines)) else None

            if right is None or left is None:
                assert right is not None or left is not None
                continue
            if right != left:
                break
        else:
            assert found is None
            found = pivot
    return found


s = 0
for pattern in open(0).read().split("\n\n"):
    grid = []
    for line in pattern.split("\n"):
        grid.append(line)
    cols = list("".join(x) for x in zip(*grid))

    horizontal = seek(grid)
    vertical = seek(cols)

    assert (horizontal is None and vertical is not None) or (
        vertical is None and horizontal is not None
    )

    if horizontal is not None:
        assert horizontal >= 0
        s += 100 * (horizontal + 1)
    if vertical is not None:
        assert vertical >= 0
        s += vertical + 1

print(s)

assert s == 37025, s
