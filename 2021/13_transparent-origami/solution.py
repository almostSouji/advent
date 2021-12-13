import time

begin = time.time()

###


def pp_paper(paper):
    for line in paper:
        print("".join(line))


with open("./input.txt", "r") as file:
    (dots, inst) = file.read().split("\n\n")
    points = []

    for line in dots.split("\n"):
        (a, b) = line.split(",")
        points.append((int(a), int(b)))

    instructions = []
    for line in inst.split("\n"):
        s = line.replace("fold along ", "")
        (c, n) = s.split("=")
        instructions.append((c, int(n)))

    max_x = 0
    max_y = 0
    for p in points:
        (y, x) = p
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x

    if max_x % 2 != 0:
        max_x += 1
    if max_y % 2 != 0:
        max_y += 1

    paper = [[" " for y in range(max_y+1)] for x in range(max_x+1)]

    for p in points:
        (x, y) = p
        paper[y][x] = "#"


def horizontalfold(paper, line):
    r1 = range(line)
    r2 = range(line+1, len(paper))

    new_paper = [[" " if paper[j][i] ==
                  " " else "#" for i in range(len(paper[0]))] for j in r1]
    c = 1
    for i in r2:
        for j in range(len(paper[0])):
            if paper[i][j] == "#":
                new_paper[line-c][j] = "#"
        c += 1
    return new_paper


def verticalfold(paper, line):
    r1 = range(line, -1, -1)
    r2 = range(line+1, len(paper[0]))

    new_paper = [[" " if paper[j][i] == " " else "#" for i in r2]
                 for j in range(len(paper))]

    c = 0
    for i in range(len(paper)):
        for j in r1:
            if paper[i][j] == "#":
                new_paper[i][c-1] = "#"
            c += 1
        c = 0
    return new_paper


def fold(paper, instruction):
    (d, n) = instruction
    match d:
        case "x":
            return verticalfold(paper, n)
        case "y":
            return horizontalfold(paper, n)


def solve1(paper, instruction):
    paper = fold(paper, instruction)
    flat = [c for line in paper for c in line if c == "#"]
    return len(flat)


def solve2(paper, instructions):
    for i in instructions:
        paper = fold(paper, i)
    pp_paper(paper)


print(f"Part 1: {solve1(paper, instructions[0])}")
print(f"Part 2: {solve2(paper, instructions)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
