import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = [int(n) for n in file.readline().split(",")]
    s = [0]*9
    for n in ns:
        s[n] += 1


def step(s):
    ns = [0]*9
    for i, n in enumerate(s):
        if i == 0:
            ns[8] += n
            ns[6] += n
        else:
            ns[i-1] += n
    return ns


def solve1(s):
    ns = s
    for i in range(1, 80+1):
        ns = step(ns)
    return sum(ns)


def solve2(s):
    ns = s
    for i in range(1, 256+1):
        ns = step(ns)
    return sum(ns)


print(f"Part 1: {solve1(s)}")
print(f"Part 2: {solve2(s)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
