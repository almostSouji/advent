from functools import reduce
from operator import mul

grid = []
p2_grid = []
with open(0) as f:
    for line in f.readlines():
        line = line.strip("\n")
        p2_grid.append(line)
        grid.append(line.split())

problems = []
for i in range(len(grid[0])):
    problem = []
    for line in grid:
        problem.append(line[i])

    problems.append(problem)


p1 = 0
for problem in problems:
    op = problem[-1]
    numbers = [int(x) for x in problem[:-1]]

    if op == "+":
        p1 += sum(numbers)
    if op == "*":
        p1 += reduce(mul, numbers)


max_p2_len = max([len(line) for line in p2_grid])
p2_grid = [line.ljust(max_p2_len, " ") for line in p2_grid]


p2_transposed = reversed(list(zip(*p2_grid)))

p2 = 0
numbers = []
for line in p2_transposed:
    joined = "".join(line[:-1]).strip()
    if len(joined) <= 0:
        numbers = []
        continue

    val = int(joined)
    numbers.append(val)

    op = line[-1]
    if op == "+":
        p2 += sum(numbers)
        continue

    if op == "*":
        p2 += reduce(mul, numbers)


print(f"part1: {p1}")
print(f"part2: {p2}")
