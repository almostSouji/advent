import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = list(map(lambda x: int(x), file.readlines()))


def solve1(ns):
    prev = float('inf')
    c = 0
    for n in ns:
        if n > prev:
            c += 1
        prev = n
    return c


def solve2(ns):
    i = 0
    prev = float('inf')
    c = 0
    for i in range(len(ns) - 3 + 1):
        s = ns[i] + ns[i+1] + ns[i+2]
        if (s > prev):
            c += 1
        prev = s
    return c


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
