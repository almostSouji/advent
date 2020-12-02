import time

begin = time.time()

###

with open("input.txt", "r") as file:
    ns = list(map(lambda x: int(x), file.readlines()))

def solve1(ns):
    for n in ns:
        for m in ns:
            if m + n == 2020:
                return m * n


def solve2(ns):
    for n in ns:
        for m in ns:
            for o in ns:
                if m + n + o == 2020:
                    return m * n * o

print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")
