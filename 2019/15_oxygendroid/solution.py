from computer import compute
from typing import List

with open("input.txt", "r") as file:
    program = list(map(int, file.read().split(",")))

EXP_INVALID_RESPONSE = "Invalid response: {}"
EXP_INVALID_DIRECTION = "Invalid direction: {}"

# 0 wall, no position change
# 1 moved one step
# 2 moved one step + found

wall = []
good = []
leak = ()
s = (program, [], 0, 0, 0, 0)
p = (0, 0)


# north 1 | south 2 | west 3 | east 4
def run(instruction: int):
    prog, inp, pnt, bse, val, op = s
    state = compute(prog, [instruction], pnt, bse, val, op)
    return state[-2]


# north 1 | south 2 | west 3 | east 4
def move(direction: int):
    res = run(direction)
    new_pos = p
    if direction == 1:
        new_pos = (p[0] + 1, p[1])
    elif direction == 2:
        new_pos = (p[0] - 1, p[1])
    elif direction == 3:
        new_pos = (p[0], p[1] - 1)
    elif direction == 4:
        new_pos = (p[0], p[1] + 1)
    else:
        raise Exception(EXP_INVALID_DIRECTION.format(direction))

    if res == 2:
        leak = new_pos
        pos = new_pos
        return (new_pos, res)
    elif res == 1:
        good.append(new_pos)
        pos = new_pos
        return new_pos
    elif res == 0:
        wall.append(p)
        return p
    else:
        raise Exception(EXP_INVALID_RESPONSE.format(res))


print(move(3))
