"""
concept: DSU
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
"""

boxes = []
for line in open(0).readlines():
    line = line.strip()
    boxes.append(tuple([int(x) for x in line.split(",")]))

distances = []
for i, (x1, y1, z1) in enumerate(boxes):
    for j, (x2, y2, z2) in enumerate(boxes[i + 1 :]):
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        distances.append((dist, (x1, y1, z1), (x2, y2, z2)))


roots = {x: x for x in boxes}


def find(member):
    parent = roots[member]
    if member == parent:
        return member

    roots[member] = find(parent)
    return roots[member]


def merge(one, other):
    roots[find(one)] = find(other)


distances.sort()

made_connections = 0
for i, (_dist, one, other) in enumerate(distances):
    if i == 1000:
        counts = dict()
        for box in boxes:
            box_root = find(box)
            root_size = counts.get(box_root, 0)
            counts[box_root] = root_size + 1

        sol1, sol2, sol3, *_rest = sorted(counts.values(), reverse=True)
        print(f"part1: {sol1 * sol2 * sol3}")

    root_one = find(one)
    root_other = find(other)

    if root_one != root_other:
        merge(one, other)
        made_connections += 1
        if made_connections >= len(boxes) - 1:
            print(f"part2: {one[0] * other[0]}")
            break
