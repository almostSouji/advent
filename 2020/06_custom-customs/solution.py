import time
from typing import List

begin = time.time()

###

with open("input.txt", "r") as file:
    blocks = file.read().split("\n\n")


def solve1(blocks: List[str]) -> int:
    return sum([len(set(block.replace("\n", ""))) for block in blocks])


def solve2(block: List[str]) -> int:
    ses = []
    for block in blocks:
        parts = block.split()
        s = set(parts[0])
        for part in parts:
            s.intersection_update(part)
        ses.append(s)
    return sum([len(s) for s in ses])


print(f"Sum of marked answers (anyone per group): {solve1(blocks)}")
print(f"Sum of marked answers (everyone per group): {solve2(blocks)}")

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")
