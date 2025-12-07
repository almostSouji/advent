start = -1
splitters = set()

visited_lines = 0
visited_cols = 0
for line_index, line in enumerate(open(0)):
    visited_lines += 1
    visited_cols = len(line)
    for col_index, val in enumerate(line):
        if val == "S":
            start = col_index

        if val == "^":
            splitters.add((line_index, col_index))


beams: set[int] = set([start])


p1 = 0
for i in range(1, visited_lines):
    rem = set()
    add = set()
    for beam in beams:
        check = (i, beam)
        if check in splitters:
            p1 += 1
            rem.add(beam)
            add.add(beam - 1)
            add.add(beam + 1)
    beams.update(add)
    beams.difference_update(rem)

print(f"part1: {p1}")
