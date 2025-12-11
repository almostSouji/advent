from icecream import ic

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
for _dist, one, other in distances[:1000]:
    merge(one, other)

sizes = dict()

for box in boxes:
    box_root = find(box)
    root_size = sizes.get(box_root, 0)
    sizes[box_root] = root_size + 1

sol1, sol2, sol3, *_rest = sorted(sizes.values(), reverse=True)

p1 = sol1 * sol2 * sol3

print(f"part1: {p1}")
