import re
from math import ceil, prod

# Test solutions:
# 0: 31
# 1: 165
# 2: 13312
# 3: 180697
# 4: 2210736

PATTERN = re.compile("(.*) => (.*)")
STRING_PATTERN = re.compile("[a-zA-Z]*")

def parse(s: str):
	matches = PATTERN.findall(s)
	d = {}
	f = ""
	for i, o in matches:
		(o_q_string, o_name) = o.split(" ")
		d[o_name] = (int(o_q_string), i)
	return (d, f)

with open("test3.txt", "r") as file:
	(d, formula) = parse(file.read())

base = [x for x in d if "ORE" in d[x][1]]
formula = d["FUEL"][1]
formula_l = formula.split(", ")
storage = {x:0 for x in d}
cost = 0

def make(quantity: int, name: str):
	print("Storage: {}".format(storage))
	print("Cost: {}".format(cost))
	print("Make: {} {}".format(quantity, name))
	recipe = d[name]
	if (name in base):
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

for elem in formula_l:
	(q, n) = elem.split(" ")
	cost += make(int(q), n)

def redeemLeftovers():
	redeemable = True
	while redeemable:
		for key in storage:
			amount = storage[key]
			

print("Cost: {}".format(cost))
print("Leftovers: {}".format(storage))
