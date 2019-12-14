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

with open("test0.txt", "r") as file:
	(d, formula) = parse(file.read())

base = [x for x in d if "ORE" in d[x][1]]
formula = d["FUEL"][1]
print(base)

solved = False

def replace(s: str):
	(amount, name) = s.split(" ")
	rec = d[n]
	need = ceil(int(amount) / rec[0])
	m = list(map(lambda x: "{} {}".format(int(x.split(" ")[0]) * need, x.split(" ")[1]) , rec[1].split(", ")))
	return ", ".join(m)
	

while not solved:
	parsed = []
	to_parse = []
	# discern parts of the formula that have a base element
	for i in formula.split(", "):
		ingr = i.split(" ")[1]
		if ingr in base:
			parsed.append(i)
		else:
			to_parse.append(i)
	if len(to_parse) == 0:
		solved = True
		break
	for i in range(len(to_parse)):
		element = to_parse[i]
		(q, n) = element.split(" ")
		rec = d[n]
		amount = 3
		to_parse[i] = replace(element)
	formula = ""
	formula += ", ".join(parsed)
	formula += ", "
	formula += ", ".join(to_parse)
	
print(formula)

