with open(0) as f:
    grid = f.readlines()

occupied = set()
for line_index, line in enumerate(grid):
    for col_index, val in enumerate(line):
        if val == "@":
            occupied.add((line_index, col_index))


def getOrNone(
    coords: tuple[int, int], occupied: set[tuple[int, int]], max_line: int, max_col: int
):
    if line_index < 0 or line_index > max_line:
        return None
    if col_index < 0 or col_index > max_col:
        return None

    return coords in occupied


p1 = 0
p2 = 0
coords = []
found_removables = [(-1, -1)]

while len(found_removables) > 0:
    found_removables = []
    for line_index, col_index in occupied:
        surrounding = [
            (line_index, col_index + 1),
            (line_index, col_index - 1),
            (line_index + 1, col_index),
            (line_index - 1, col_index),
            (line_index + 1, col_index + 1),
            (line_index + 1, col_index - 1),
            (line_index - 1, col_index + 1),
            (line_index - 1, col_index - 1),
        ]

        surrounding_is_occupied = [
            getOrNone(x, occupied, len(grid) - 1, len(grid[0]) - 1) for x in surrounding
        ]
        surrounding_occupied = [x for x in surrounding_is_occupied if x]

        if len(surrounding_occupied) < 4:
            found_removables.append((line_index, col_index))

    if len(found_removables):
        p2 += len(found_removables)
        for removable in found_removables:
            occupied.remove(removable)

    if p1 == 0:
        p1 = len(found_removables)


print(f"part1: {p1}")
print(f"part2: {p2}")
