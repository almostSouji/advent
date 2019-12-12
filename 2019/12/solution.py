import re
from itertools import combinations
import operator

EXPRESSION = "<x=(?P<x>-?\d+), y=(?P<y>-?\d+), z=(?P<z>-?\d+)>"
STEPS = 1000

with open("input.txt", "r") as file:
	input = file.read().splitlines()

positions = list(map(lambda line: re.match(EXPRESSION, line), input))
io_pos = positions[0]
europa_pos = positions[1]
ganymede_pos = positions[2]
callisto_pos = positions[3]

io = {
	"name": "io",
	"velocity": [0, 0, 0],
	"coordinates": list(map(int, [io_pos.group("x"), io_pos.group("y"), io_pos.group("z")]))
}

europa = {
	"name": "europa",
	"velocity": [0, 0, 0],
	"coordinates": list(map(int, [europa_pos.group("x"), europa_pos.group("y"), europa_pos.group("z")]))
}

ganymede = {
	"name": "ganymede",
	"velocity": [0, 0, 0],
	"coordinates": list(map(int, [ganymede_pos.group("x"), ganymede_pos.group("y"), ganymede_pos.group("z")]))
}

callisto = {
	"name": "callisto",
	"velocity": [0, 0, 0],
	"coordinates": list(map(int, [callisto_pos.group("x"), callisto_pos.group("y"), callisto_pos.group("z")]))
}

moons = [io, europa, ganymede, callisto]
combinations = list(combinations(moons, 2))

for i in combinations:
	print(i)

for i in range(STEPS):
	# apply gravity
	for c in combinations:
		c1 = c[0]["coordinates"]
		c2 = c[1]["coordinates"]
		v1 = c[0]["velocity"]
		v2 = c[1]["velocity"]
		for j in range(3):
			if c1[j] > c2[j]:
				v1[j] -= 1
				v2[j] += 1
			elif c1[j] < c2[j]:
				v1[j] += 1
				v2[j] -= 1
	# apply velocity
	for m in moons:
		m["coordinates"] = [a + b for a, b in zip(m["coordinates"], m["velocity"])]
		m["kin"] = sum(map(abs, m["coordinates"]))
		m["pot"] = sum(map(abs, m["velocity"]))

s = sum([m["kin"] * m["pot"] for m in moons])

print("Part 1: total energy in the system after {} time steps: {}".format(STEPS, s))

def printState(moonlist):
	for m in moonlist:
		print("{}: position: {}, velocity: {} kin: {} pot: {} total: {}".format(m["name"], m["coordinates"], m["velocity"], m["kin"], m["pot"], m["kin"] * m["pot"]))