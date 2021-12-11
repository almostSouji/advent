import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = [int(n) for n in file.readline().split(",")]


def cost(ns, x):
    c = 0
    for n in ns:
        c += abs(n - x)
    return c


def cost2(ns, x):
    c = 0
    for n in ns:
        i = abs(n-x)
        c += int((i * (i+1)) / 2)
    return c


def solve1(ns):
    mi = min(ns)
    ma = max(ns)
    c = [(i, cost(ns, i)) for i in range(mi, ma+1)]
    c.sort(key=lambda x: x[1])
    return c[0][1]


def solve2(ns):
    mi = min(ns)
    ma = max(ns)
    c = [(i, cost2(ns, i)) for i in range(mi, ma+1)]
    c.sort(key=lambda x: x[1])
    return c[0][1]


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
