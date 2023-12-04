import time
from typing import List

begin = time.time()

###

INPUTFILE = "input.txt"
PREAMBLE_LENGTH = 5 if INPUTFILE == "test.txt" else 25

with open(INPUTFILE, "r") as file:
    numbers = [int(line) for line in file.readlines()]


def checksum(preamble: List[int], n: int):
    for e in preamble:
        for f in preamble:
            if e + f == n:
                return True
    return False


def findVuln(nums: [int]) -> int:
    for i, e in enumerate(nums):
        if i < PREAMBLE_LENGTH:
            continue
        if not checksum(nums[i - PREAMBLE_LENGTH : i], e):
            return e


v = findVuln(numbers)

print(f"First not passing checksum: {v}")

for i in range(0, len(numbers)):
    sm = 0
    if i == len(numbers) - 1:
        break
    for j in range(i, len(numbers)):
        sm += numbers[j]
        if sm > v:
            break
        if sm == v:
            if i == j:
                break
            found = numbers[i : j + 1]
            (s, l) = (min(found), max(found))
            print(f"Weakness: {s+l} | smallest: {s}, largest: {l}")
            break

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")
