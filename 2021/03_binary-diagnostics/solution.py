import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = [line.strip() for line in file.readlines()]


def countBits(ns):
    bc = [(0, 0)] * (len(ns[0]))

    for n in ns:
        for i, c in enumerate(n):
            if c == "0":
                bc[i] = (bc[i][0] + 1, bc[i][1])
            else:
                bc[i] = (bc[i][0], bc[i][1] + 1)

    return bc


def solve1(ns):
    bc = countBits(ns)
    g = ""
    e = ""

    for b in bc:
        (z, o) = b
        if z > o:
            g += "0"
            e += "1"
        else:
            g += "1"
            e += "0"

    gr = int(g, 2)
    er = int(e, 2)

    return gr * er


def getReading(ns, pred):
    indices = list(range(0, len(ns)))
    i = 0

    while len(indices) > 1:
        counts = countBits([ns[a] for a in indices])

        b = pred(*counts[i])
        indices = [a for a in indices if ns[a][i] == b]
        i += 1

    return int(ns[indices[0]], 2)


def solve2(ns):
    oxy = getReading(ns, lambda z, o: "0" if z > o else "1")
    co2 = getReading(ns, lambda z, o: "0" if z <= o else "1")
    return oxy * co2


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
