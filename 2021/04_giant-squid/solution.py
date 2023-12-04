import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = [int(l) for l in file.readline().split(",")]
    r = file.read()
    boards = [
        [[(int(c), 0) for c in l.split()] for l in c.strip().split("\n")]
        for c in r.split("\n\n")
    ]


def check_board(b):
    sols = [*b, *[[b[j][i] for j in range(0, len(b))] for i in range(0, len(b))]]

    for sol in sols:
        if len([c for c in sol if c[1] == 0]) == 0:
            return True
    return False


def apply(b, n):
    for ri, r in enumerate(b):
        for fi, f in enumerate(r):
            if f[0] == n:
                b[ri][fi] = (n, 1)


def score(b):
    flat = [c[0] for r in b for c in r if c[1] == 0]
    return sum(flat)


def solve1():
    for n in ns:
        for b in boards:
            apply(b, n)
            w = check_board(b)
            if w:
                return score(b) * n


def solve2():
    tracker = [0] * len(boards)
    wins = []
    for n in ns:
        for i, b in enumerate(boards):
            apply(b, n)
            w = check_board(b)
            if w and tracker[i] == 0:
                tracker[i] = 1
                wins.append(score(b) * n)
    return wins[-1]


print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
