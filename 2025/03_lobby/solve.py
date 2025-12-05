#!/user/bine/env python3

p1 = 0
p2 = 0
for line in open(0):
    bank = line.strip()
    highest_val = 0

    for index, battery in enumerate(bank):
        rest = [int(x) for x in bank[index + 1 :]]
        if len(rest):
            highest_digit = max(rest)
            highest_val = max(int(str(battery + str(highest_digit))), highest_val)

    p1 += highest_val

    res = []
    i = 11
    start = 0
    while i >= 0:
        prefix = bank[start : len(bank) - i]

        max_element = (-1, -1)
        for j, battery in enumerate([int(x) for x in prefix]):
            max_val, max_pos = max_element
            if battery > max_val:
                max_element = (battery, j + start)

        res.append(max_element[0])
        start = max_element[1] + 1
        i -= 1
    p2 += int("".join([str(x) for x in res]))


print(f"part1: {p1}")
print(f"part2: {p2}")
