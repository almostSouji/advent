#!/usr/bin/env python3
def seek(lines, p2=False):
    sol = None
    for pivot in range(0, len(lines) - 1):
        totaldiff = 0
        for r in range(pivot + 1, len(lines)):
            l = pivot - (r - pivot - 1)

            left = lines[l] if l in range(0, len(lines)) else None
            right = lines[r] if r in range(0, len(lines)) else None

            if right is None or left is None:
                assert right is not None or left is not None
                continue

            if p2:
                diff = [i for i, c in enumerate(left) if c != right[i]]
                totaldiff += len(diff)
            else:
                if right != left:
                    break
        else:
            if p2 and totaldiff == 1:
                assert sol is None
                sol = pivot
            elif not p2:
                sol = pivot
    return sol


s = 0
s2 = 0
for pattern in open(0).read().split("\n\n"):
    grid = []
    for line in pattern.split("\n"):
        grid.append(line)
    cols = list("".join(x) for x in zip(*grid))

    for flag in [False, True]:
        horizontal = seek(grid, p2=flag)
        vertical = seek(cols, p2=flag)

        assert (horizontal is None and vertical is not None) or (
            vertical is None and horizontal is not None
        )

        if horizontal is not None:
            assert horizontal >= 0
            if flag:
                s2 += 100 * (horizontal + 1)
            else:
                s += 100 * (horizontal + 1)
        if vertical is not None:
            assert vertical >= 0
            if flag:
                s2 += vertical + 1
            else:
                s += vertical + 1

print(s)
print(s2)

assert s == 37025, s
assert s2 == 32854, s2
