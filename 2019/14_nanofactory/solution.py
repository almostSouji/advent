import re
from math import ceil, prod, floor

# Test solutions:
# 0: 31
# 1: 165
# 2: 13312
# 3: 180697
# 4: 2210736

FILEPATH = "./input.txt"
PATTERN = re.compile("(.*) => (.*)")
STRING_PATTERN = re.compile("[a-zA-Z]*")


def computeOreCost(content, fuel):
    def parse(s: str):
        matches = PATTERN.findall(s)
        d = {}
        for i, o in matches:
            (o_q_string, o_name) = o.split(" ")
            d[o_name] = (int(o_q_string), i)
        return d

    d = parse(content)

    base = [x for x in d if "ORE" in d[x][1]]
    fuel_recipe = d["FUEL"]
    formula = fuel_recipe[1]
    storage = {x: 0 for x in d}
    cost = 0
    base_counter = {x: 0 for x in base}

    def make(quantity: int, name: str):
        recipe = d[name]
        if name in base:
            ore_per_unit = int(recipe[1].split(" ")[0])
            # make from ore
            amount = ceil(quantity / recipe[0])
            made = amount * recipe[0]
            # add overflow to storage
            storage[name] += made - quantity
            return ore_per_unit * amount
        else:
            ore_counter = 0
            # determine needed elements
            amount = ceil(quantity / recipe[0])
            for elem in recipe[1].split(", "):
                (amount_mut, name_mut) = elem.split(" ")
                amount_mut = int(amount_mut)
                ore_counter += make(amount * amount_mut, name_mut)
            # parent is made
            # store parent elements if more made than needed
            made = amount * recipe[0]
            storage[name] += made - quantity
            return ore_counter

    for elem in formula.split(", "):
        (q, n) = elem.split(" ")
        q = int(q)
        cost += make(fuel * q, n)

    # redeem leftovers
    change = True
    while change:
        change = False
        for key in storage:
            amount = storage[key]
            if amount < 1:
                continue
            recipe = d[key]
            sales = floor(amount / recipe[0])
            if sales < 1:
                continue
            for elem in recipe[1].split(", "):
                (n, name) = elem.split(" ")
                n = int(n)
                if name == "ORE":
                    cost -= n * sales
                else:
                    storage[name] += n * sales
                    change = True
            storage[key] -= recipe[0] * sales
    return cost


with open(FILEPATH, "r") as file:
    costs = file.read()
    ore = computeOreCost(costs, 1)

print("Part 1: Cost: {}".format(ore))


def binSearch(one_fuel_cost, val):
    lower = val / one_fuel_cost
    upper = val
    v = 0
    while lower <= upper or v > val:
        mid = ceil((lower + upper - 1) / 2)
        v = computeOreCost(costs[:], mid)
        if v == val:
            return mid
        elif v < val:
            lower = mid + 1
        else:
            upper = mid - 1
    return mid


print("Part 2: Fuel for 1 Trillion ORE: {}".format(binSearch(ore, 1000000000000) // 1))
