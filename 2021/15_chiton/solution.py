import time
from collections import deque

begin = time.time()

###

with open("./test.txt", "r") as file:
    ns = list(map(lambda x: [int(y)
              for y in list(x.strip())], file.readlines()))
    res = []
    for i in range(len(ns)):
        row = []
        for j in range(len(ns[0])):
            row.append((i, j, ns[i][j]))
        res.append(row)
    print(res)


def get_adjacent(nodes, point):


def bfs(nodes, root):
    q = deque()
    e = set()
    q.append([root])
    while len(q) > 0:
        p = q.popleft()
        n = v[-1]
        if n == nodes[len(nodes)-1][len(nodes[0])-1]:
            # end found
            return p
        for a in get_adjacent(nodes, point):
            np = list(path)
            np.append(a)
            q.append(np)


def solve1(res):
    bfs(res, res[0][0])


def solve2(ns):
    0


print(f"Part 1: {solve1(res)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
