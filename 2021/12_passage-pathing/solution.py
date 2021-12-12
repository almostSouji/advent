import time

begin = time.time()

###


def mapper(l):
    (t, f) = l.strip().split("-")
    return (t, f)


with open("./input.txt", "r") as file:
    paths = list(map(mapper, file.readlines()))
    nodes = set()
    for path in paths:
        (t, f) = path
        if t not in nodes:
            nodes.add(t)
        if f not in nodes:
            nodes.add(f)


def has_lowercase_dupe(path):
    d = {}
    for p in path:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1

    for k, v in d.items():
        if v > 1 and k.lower() == k:
            return True
    return False


def should_discard_2(path):
    d = {}
    check = False
    for p in path:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1

    for k, v in d.items():
        if v > 1 and k.lower() == k:
            if v == 2 and k != "start" and k != "end" and not check:
                check = True
                continue
            return True
    return False


def rec(ps, fin, should_discard):
    np = []

    for p in ps:
        last = p[-1]
        if should_discard(p):
            continue
        for candidate in paths:
            if last in candidate:
                other = candidate[1] if candidate[0] == last else candidate[0]

                if last == "end":
                    continue
                if other == "end":
                    fin.append([*p, other])
                else:
                    np.append([*p, other])

    if len(np) != 0:
        fin = [*fin, *rec(np, fin, should_discard)]
    return fin


def solve1(paths):
    p = []
    for path in paths:
        if "start" in path:
            other = path[1] if path[0] == "start" else path[0]
            p.append(["start", other])

    fins = rec(p, [], has_lowercase_dupe)
    deduped = set([",".join(fin) for fin in fins])

    return len(deduped)


def solve2(paths):
    p = []
    for path in paths:
        if "start" in path:
            other = path[1] if path[0] == "start" else path[0]
            p.append(["start", other])

    fins = rec(p, [], should_discard_2)
    deduped = set([",".join(fin) for fin in fins])

    return len(deduped)


print(f"Part 1: {solve1(paths)}")
print(f"Part 2: {solve2(paths)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
