fresh_ids = set()
fresh_ranges = []
with open(0) as f:
    [ranges, ids] = f.read().split("\n\n")

    for line in ranges.splitlines():
        upper, lower = [int(x) for x in line.split("-")]
        fresh_range = range(upper, lower + 1)
        fresh_ranges.append(fresh_range)

    for id in ids.splitlines():
        for f in fresh_ranges:
            if int(id) in f:
                fresh_ids.add(id)

fresh_ranges.sort(key=lambda x: x.start)

combined_ranges = [fresh_ranges[0]]
for r in fresh_ranges[1:]:
    last = combined_ranges[-1]

    if r.start <= last.stop:
        combined_ranges[-1] = range(last.start, max(last.stop, r.stop))
    else:
        combined_ranges.append(r)

p2 = 0
for x in combined_ranges:
    p2 += len(x)

print(f"part1: {len(fresh_ids)}")
print(f"part2: {p2}")
