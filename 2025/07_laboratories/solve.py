start = -1
splitters: set[tuple[int, int]] = set()

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


beams_d: dict[int, int] = dict()
beams_d[start] = 1


p1 = 0
for i in range(1, visited_lines):
    rem: list[int] = []
    add: list[tuple[int, int]] = []
    for beam, paths in beams_d.items():
        check = (i, beam)
        if check in splitters:
            p1 += 1
            rem.append(beam)
            add.append((beam - 1, paths))
            add.append((beam + 1, paths))

    for r in rem:
        del beams_d[r]

    for add_beam, paths in add:
        current = beams_d.get(add_beam, 0)
        beams_d[add_beam] = current + paths

p2 = sum(beams_d.values())

print(f"part1: {p1}")
print(f"part2: {p2}")
