import time
from math import floor, ceil
from typing import Tuple, List

begin = time.time()

###

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def binsearch(part: str, lower:int, upper:int, lower_sym:str, upper_sym:str) -> int:
    for (i, sym) in enumerate(part):
        if (i == len(part)-1):
            return lower if sym == lower_sym else upper
        dist = ceil((upper-lower) / 2)
        if sym == lower_sym:
            upper -= dist
        elif sym == upper_sym:
            lower += dist
        else:
            raise("never")

def seat_id(row:int, col:int) -> int:
    return (row * 8) + col

seats = [(binsearch(l[:7], 0, 127, "F", "B"), binsearch(l[7:], 0, 7, "L", "R")) for l in lines]
seat_ids = [seat_id(*s) for s in seats]

def solve2(seats: List[int]) -> int:
    prev = seats[0]
    for s in seats[1:]:
        if s - prev == 2:
            return s - 1
        prev = s

print(f"Highest seat id: {max(seat_ids)}")
print(f"Free seat id: {solve2(sorted(seat_ids))}")

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")

#   super smart idea using bits
#
#   ALLOCATION = {
#   	"F": "0",
#   	"B": "1",
#   	"L": "0",
#   	"R": "1"
#   }
#   
#   
#   def parseSeatId(brdng_pass: str) -> int:
#   	binary = (ALLOCATION[char] for char in list(brdng_pass))
#   	return int("".join(binary), 2)
#   