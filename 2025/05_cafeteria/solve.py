from icecream import ic

fresh_ids = set()
with open(0) as f:
    [ranges, ids] = f.read().split("\n\n")

    fresh_ranges = []
    for line in ranges.splitlines():
        upper, lower = [int(x) for x in line.split("-")]
        fresh_ranges.append(range(upper, lower + 1))

    for id in ids.splitlines():
        for f in fresh_ranges:
            if int(id) in f:
                fresh_ids.add(id)

print(f"part1: {len(fresh_ids)}")
