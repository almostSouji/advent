import time
from typing import Tuple, List
import re
import copy

begin = time.time()

###

with open("input.txt", "r") as file:
    lines = file.readlines()

OPS = {
    "nop" : 0,
    "jmp" : 1,
    "acc" : 2,
}

def parse(s: str) -> Tuple[int, int, bool]:
    m = re.match(r"(\w{3}) ([+-]\d+)", s)
    (op, val) = m.groups()
    return (OPS[op], int(val), False)

instructions = [parse(line) for line in lines]

def run(program: List[Tuple[int, int, bool]], silent=False):
    p = 0
    acc = 0
    terminated = False
    while not terminated:
        (op, val, visited) = program[p]
        if p == len(program) - 1:
            terminated = True
        if (visited):
            if (not silent):
                print(f"Loop detected, accumulator value: {acc}")
            return 0

        program[p] = (op, val, True)

        if (op == 0):
            p += 1
        elif (op == 1):
            p += val
        elif (op == 2):
            acc += val
            p += 1
        else:
            raise Exception(f"unknown operator {op}")

        if terminated:
            if (not silent):
                print(f"Terminated with accumulator value: {acc}")
            return 1

def gen_sols(program: List[Tuple[int, int, bool]]) -> List[List[Tuple[int, int, bool]]]:
    res = []
    for (i, ins) in enumerate(program):
        (op, val, _) = ins
        if op == 0 or op == 1:
            c = copy.deepcopy(program)
            c[i] = (int(not op), val, False)
            res.append(c)
    return res
    

run(copy.deepcopy(instructions))

sols = gen_sols(instructions)
p = 0
for (i, sol) in enumerate(sols):
    res = run(copy.deepcopy(sol), True)
    if (res == 1):
        p = i

run(copy.deepcopy(sols[p]))

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")