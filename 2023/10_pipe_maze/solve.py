#!/usr/bin/env python3

m = {}
start = None
for x, line in enumerate(open(0)):
    for y, c in enumerate(line.strip()):
        m[x + 1j * y] = c
        if c == "S":
            start = x + 1j * y

n = {
    (1, "|"): 1,
    (-1, "|"): -1,
    (1j, "-"): 1j,
    (-1j, "-"): -1j,
    (1, "L"): 1j,
    (-1j, "L"): -1,
    (1, "J"): -1j,
    (1j, "J"): -1,
    (1j, "7"): 1,
    (-1, "7"): -1j,
    (-1j, "F"): 1,
    (-1, "F"): 1j,
}

deltas = [1, -1, 1j, -1j]
curr = [
    (start + d, d, [start, start + d])
    for d in deltas
    if (d, m.get(start + d, None)) in n
]

lace = None
while True:
    for i, (c, d, path) in enumerate(curr):
        delta = n.get((d, m[c]), None)
        next = c + delta
        for j, (_, _, p) in enumerate(curr):
            if next in p and i != j:
                lace = [*curr[i][2], *reversed(curr[j][2][1:])]
                break
        else:
            curr[i] = (next, delta, path + [next])
            continue
        break
    else:
        continue
    break

s = int(len(lace) / 2)

# find the real symbol of S
assert lace[0] == start

candidates = set("|-LJ7F")
for elem in [lace[-1] - start, lace[1] - start]:
    possible = set()
    for k, v in n.items():
        if v == elem:
            possible.add(k[1])
    candidates &= possible

start_shape = candidates.pop()
m[start] = start_shape

# shoelace algorithm https://www.101computing.net/the-shoelace-algorithm/

sum1 = 0
sum2 = 0
for a, b in zip(lace, lace[1:]):
    sum1 += a.real * b.imag
    sum2 += a.imag * b.real
sum1 += lace[-1].real * lace[0].imag
sum2 += lace[-1].imag * lace[0].real
area = abs(sum1 - sum2) / 2

# picks theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
# A = i + R/2 - 1
# A := total area
# i := number of internal points
# R := number of points on the boundary
# => i = A - R/2 + 1

s2 = int(area - len(lace) / 2 + 1)

print(s)
print(s2)
assert s == 7066, s
assert s2 == 401, s2
