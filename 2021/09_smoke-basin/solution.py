import time
import functools

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = list(map(lambda x: [int(i)
              for i in list(x.strip())], file.readlines()))


def is_local_min(c, ns):
    (x, y) = c
    m_x = len(ns) - 1
    m_y = len(ns[0]) - 1
    if x != 0:
        if ns[x-1][y] <= ns[x][y]:
            return False
    if x != m_x:
        if ns[x+1][y] <= ns[x][y]:
            return False
    if y != 0:
        if ns[x][y-1] <= ns[x][y]:
            return False
    if y != m_y:
        if ns[x][y+1] <= ns[x][y]:
            return False
    return True


def find_local_mins(ns):
    l = []
    for x in range(len(ns)):
        for y in range(len(ns[0])):
            if (is_local_min((x, y), ns)):
                l.append((x, y))
    return l


def risk(n):
    return n + 1


def cell_value(p, ns):
    (x, y) = p
    m_x = len(ns) - 1
    m_y = len(ns[0]) - 1

    if x not in range(0, m_x+1):
        return 0
    if y not in range(0, m_y+1):
        return 0
    if ns[x][y] == 9:
        return 0
    return 1


def explore_point(p, ns, v):
    (x, y) = p
    if p in v:
        return 0
    v.add(p)
    ctr = cell_value(p, ns)
    if ctr != 0:
        ctr += sum([explore_point((x+1, y), ns, v),
                    explore_point((x-1, y), ns, v),
                    explore_point((x, y-1), ns, v),
                    explore_point((x, y+1), ns, v)])
    return ctr


def solve1(ns):
    return sum([risk(ns[x][y]) for (x, y) in find_local_mins(ns)])


def solve2(ns):
    lm = find_local_mins(ns)
    s = [explore_point(m, ns, set()) for m in lm]
    s.sort()
    return functools.reduce(lambda a, b: a * b, s[-3:])


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
