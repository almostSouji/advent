import time
import copy

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = list(map(lambda x: [int(n)
              for n in list(x.strip())], file.readlines()))


def check_point(p, ns):
    (x, y) = p
    if y in range(0, len(ns)) and x in range(0, len(ns)):
        return True
    return False


def flash(p, ns):
    (x, y) = p
    n = [
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x, y+1),
        (x+1, y+1),
        (x+1, y),
        (x+1, y-1),
        (x, y-1),
    ]

    for q in n:
        (xq, yq) = q
        if check_point(q, ns):
            ns[xq][yq] += 1


def step(ns):
    for i, line in enumerate(ns):
        for j, cell in enumerate(line):
            ns[i][j] += 1

    has_flashed = []
    flashed = True
    while flashed:
        flashed = False
        for i, line in enumerate(ns):
            for j, cell in enumerate(line):
                if cell > 9:
                    if (i, j) in has_flashed:
                        continue
                    flash((i, j), ns)
                    has_flashed.append((i, j))
                    flashed = True

    for p in has_flashed:
        (x, y) = p
        ns[x][y] = 0

    return len(has_flashed)


def solve1(ns):
    ctr = 0
    for i in range(1, 100+1):
        ctr += step(ns)
    return ctr


def solve2(ns):
    i = 1
    while True:
        step(ns)
        flat = [c for r in ns for c in r]
        if (sum(flat) == 0):
            return i
        i += 1


print(f"Part 1: {solve1(copy.deepcopy(ns))}")
print(f"Part 2: {solve2(copy.deepcopy(ns))}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
