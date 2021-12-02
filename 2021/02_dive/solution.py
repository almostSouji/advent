import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = file.readlines()


def solve1(ns):
    h = 0
    d = 0
    for n in ns:
        (op, val_s) = n.split()
        val = int(val_s)
        match op:
            case "forward":
                h += val
            case "down":
                d += val
            case "up":
                d -= val
    return h * d


def solve2(ns):
    h = 0
    d = 0
    a = 0
    for n in ns:
        (op, val_s) = n.split()
        val = int(val_s)
        match op:
            case "forward":
                h += val
                d += (val * a)
            case "down":
                a += val
            case "up":
                a -= val
    return h * d


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
