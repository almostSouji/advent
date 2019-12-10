from typing import Tuple, List
import numpy
import math

# test 1: (3, 4) with 8
# test 2: (5, 8) with 33
# test 3: (1, 2) with 35
# test 4: (6, 3) with 41
# test 5: (11, 13) with 210

with open("test1.txt", "r") as file:
	field = numpy.array(list(map(list, file.read().split("\n"))))

for line in field:
	print(line)
ASTEROID = "#"

dimensions = (len(field[0]),len(field))
asteroids: List[Tuple[int, int]] = []
data: List[Tuple[Tuple[int, int], int]] = []

for x in range(0, dimensions[0]):
	for y in range(0, dimensions[1]):
		if field[(x,y)] == "#":
			asteroids.append((x, y))

print(asteroids)

def vec_eq(v1:Tuple[int, int], v2:Tuple[int,int]):
	# equal direction if cross product is 0
	return numpy.cross(v1, v2) == 0
	
def vec_dist(v1:Tuple[int, int], v2: Tuple[int, int]):
	if v1 == v2:
		return math.inf
	return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
	
def max_index(lst: List[int]):
	max_val = 0
	max_i = 0
	for i in range(0, len(lst)):
		if lst[i] > max_val:
			max_val = lst[i]
			max_i = i
	return max_i
	
# each asteroid is a potential station
for stat in asteroids:
	print("------ {} ------".format(stat))
	f = numpy.copy(field)
	# check for each asteroid in the field
	for a in asteroids:
		# if self continue
		if a == stat:
			continue
		# if already marked as viewable/hidden continue
		sign = f[a]
		if sign == "v" or sign == "h":
			continue
		# vector of this asteroid and pot. station
		vec = (a[0] - stat[0], a[1] - stat[1])
		# all asts with the same station
		# print("For vector: {}".format(vec))
		eqs = [b for b in asteroids if vec_eq(vec, (b[0] - stat[0], b[1] - stat[1]))]
		# print("Equal vectors: {}".format(eqs))
		# mark closest as viewable, others as hidden
		m = min(eqs, key=lambda x: vec_dist(stat, x))
		# print("Min: {}".format(m))
		for t in eqs:
			f[t] = "v" if t == m else "h"	
	f[stat] = "X"
	for line in f:
		print(line)
	vs = len([item for sublist in f for item in sublist if item == "v"])
	data.append((stat, vs))
	
m = max(data, key=lambda x: x[1])
print("Part 1: Max. visibility {} on asteroid {}".format(m[1], m[0]))
		
print(data)