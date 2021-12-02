import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = file.readlines()


def solve1(ns):
    h = 0
    d = 0
    for n in ns:
        match n.split():
            case "forward", val:
                h += int(val)
            case "down", val:
                d += int(val)
            case "up", val:
                d -= int(val)
    return h * d


def solve2(ns):
    h = 0
    d = 0
    a = 0
    for n in ns:
        match n.split():
            case "forward", val:
                h += int(val)
                d += (int(val) * a)
            case "down", val:
                a += int(val)
            case "up", val:
                a -= int(val)
    return h * d


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
