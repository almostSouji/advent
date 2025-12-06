from functools import reduce
from operator import mul

from icecream import ic

grid = []
with open(0) as f:
    for line in f.readlines():
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

print(f"part1: {p1}")
