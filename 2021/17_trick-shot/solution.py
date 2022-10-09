import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = list(map(lambda x: int(x), file.readlines()))


def solve1(ns):
    0


def solve2(ns):
    0


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
