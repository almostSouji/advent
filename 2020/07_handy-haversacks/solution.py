import time

begin = time.time()

###

with open("input.txt", "r") as file:
    lines = [[part.strip(r" |.") for part in line.strip().split("bags contain")] for line in [line.strip() for line in file.readlines()]]

table = {}

for line in lines:
    (key, rest) = line
    table[key] = [((int(part.split(" ")[0]) if part.split(" ")[0].isnumeric() else 0), " ".join(part.split(" ")[1:-1])) for part in rest.split(", ")]

def bag_count(table, clr: str):
    s = 0
    for (amount, color) in table[clr]:
            s += amount + amount * bag_count(table, color) if amount > 0 else amount
    return s;

def search_bags(table, clr: str):
    res = set()
    for (key, val) in table.items():
        for (_, color) in val:
            if color == clr:
                res.add(key) 
    return res

candidates = search_bags(table, "shiny gold")
res = set(candidates)

while len(candidates) > 0:
    n = search_bags(table, candidates.pop())
    res.update(n)
    candidates.update(n)

print(f"Eventually containing shiny gold: {len(res)}")
print(f"Needed bags: {bag_count(table, 'shiny gold')}")

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")
