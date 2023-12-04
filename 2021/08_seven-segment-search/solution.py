import time

begin = time.time()

###


def splitter(x):
    (a, b) = x.split("|")
    return (a.strip().split(" "), b.strip().split(" "))


with open("./input.txt", "r") as file:
    ns = list(map(splitter, file.readlines()))


def solve1(ns):
    c = 0
    for n in ns:
        (sig, out) = n
        for d in out:
            if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
                c += 1
    return c


mapping = {
    frozenset(list("abcefg")): 0,
    frozenset(list("cf")): 1,
    frozenset(list("acdeg")): 2,
    frozenset(list("acdfg")): 3,
    frozenset(list("bcdf")): 4,
    frozenset(list("abdfg")): 5,
    frozenset(list("abdefg")): 6,
    frozenset(list("acf")): 7,
    frozenset(list("abcdefg")): 8,
    frozenset(list("abcdfg")): 9,
}


def solve2(ns):
    ctr = 0
    for n in ns:
        # d -> set<c>
        d = {}
        # c -> n
        cs = {}
        # c -> c
        m = {}
        (sig, out) = n
        for s in sig:
            ss = set(list(s))
            l = len(s)
            if l == 2:
                d[1] = ss
            elif l == 3:
                d[7] = ss
            elif l == 4:
                d[4] = ss
            elif l == 7:
                d[8] = ss

            for c in list(s):
                if c in cs:
                    cs[c] += 1
                else:
                    cs[c] = 1

        for k, v in cs.items():
            if v == 4:
                m[k] = "e"
            if v == 6:
                m[k] = "b"
            if v == 9:
                m[k] = "f"
            if v == 7:
                m[k] = "d" if k in d[4] else "g"
            if v == 8:
                m[k] = "c" if k in d[1] else "a"

        s = ""
        for w in out:
            k = frozenset([m[c] for c in list(w)])
            d = mapping[k]
            s += str(d)

        ctr += int(s)
    return ctr


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
