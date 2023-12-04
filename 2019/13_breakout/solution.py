from computer import compute
from typing import List

with open("input.txt", "r") as file:
    program = list(map(int, file.read().split(",")))

SIZE = 10
TILES = {
    0: " ",  # empty
    1: "#",  # wall
    2: "x",  # block
    3: "--",  # paddle
    4: "o",  # ball
}


def setTile(field: List[List[int]], instr: List[int]):
    print(instr, "ins")
    field[instr[1]][instr[0]] = TILES[instr[2]]


field = [[0 for j in range(SIZE)] for i in range(SIZE)]

for line in field:
    print(line)


def setup(program: List[int]):
    state = (program,)
    while True:
        out = []
        state = compute(*state)
        out.append(state[-2])
        if len(out) == 3:
            setTile(field, out)
            print("check")
            for l in field:
                print(l)
            out = []
        if state[-1] == 99:
            return True


setup(program)
blocknum = len([item for sublist in field for item in sublist if item == "X"])

print("Part 1: number of blocks: {}".format(blocknum))

for line in field:
    print(line)
