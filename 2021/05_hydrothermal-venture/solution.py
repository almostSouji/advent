import time

begin = time.time()

###


def parse(x):
    (f, t) = x.strip().split(" -> ")
    (fx, fy) = f.split(",")
    (tx, ty) = t.split(",")

    return ((int(fx), int(fy)), (int(tx), int(ty)))


with open("./input.txt", "r") as file:
    ns = list(map(parse, file.readlines()))


def solve1(ns):
    d = {}

    for n in ns:
        (f, t) = n
        (fx, fy) = f
        (tx, ty) = t

        if (fx == tx):
            mi = min(fy, ty)
            ma = max(fy, ty)
            for i in range(mi, ma+1):
                c = (fx, i)
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

        elif (fy == ty):
            mi = min(fx, tx)
            ma = max(fx, tx)
            for i in range(mi, ma+1):
                c = (i, fy)
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

    return len([k for k, v in d.items() if v >= 2])


def solve2(ns):
    d = {}

    for n in ns:
        (f, t) = n
        (fx, fy) = f
        (tx, ty) = t

        if (fx == tx):
            mi = min(fy, ty)
            ma = max(fy, ty)
            for i in range(mi, ma+1):
                c = (fx, i)
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

        elif (fy == ty):
            mi = min(fx, tx)
            ma = max(fx, tx)
            for i in range(mi, ma+1):
                c = (i, fy)
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
        else:
            xi = 1 if fx < tx else -1
            yi = 1 if fy < ty else -1

            y = fy
            for x in range(fx, tx + xi, xi):
                c = (x, y)
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
                y += yi

    return len([k for k, v in d.items() if v >= 2])


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
