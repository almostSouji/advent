import time

begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = list(map(lambda x: x.strip(), file.readlines()))

error_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

complete_scores = {")": 1, "]": 2, "}": 3, ">": 4}


pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

opening = set(pairs.keys())
closing = set(pairs.values())


def error_score(s):
    chars = []
    for c in s:
        if c in opening:
            chars.append(c)
        if c in closing:
            last_pair = pairs[chars.pop(-1)]
            if c != last_pair:
                return error_scores[c]
    return 0


def complete(s):
    chars = []
    for c in s:
        if c in opening:
            chars.append(c)
        if c in closing:
            chars.pop(-1)
    sc = 0
    comp = [pairs[c] for c in chars]
    comp.reverse()
    for c in comp:
        sc *= 5
        sc += complete_scores[c]
    return sc


def solve1(ns):
    return sum([error_score(n) for n in ns])


def solve2(ns):
    incomplete = [n for n in ns if error_score(n) == 0]
    scores = [complete(n) for n in incomplete]
    scores.sort()
    return scores[int(len(scores) / 2)]


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
