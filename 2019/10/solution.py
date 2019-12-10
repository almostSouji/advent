from typing import Tuple, List
import numpy
import math

ASTEROID = "#"

with open("input.txt", "r") as file:
	field = numpy.array(list(map(list, file.read().split("\n"))))

dimensions = (len(field[0]),len(field))
asteroids: List[Tuple[int, int]] = []
data: List[Tuple[Tuple[int, int], int]] = []

for x in range(0, dimensions[0]):
	for y in range(0, dimensions[1]):
		if field[y][x] == "#":
			asteroids.append((x,y))
data = []

# each asteroid is a potential station
for stat in asteroids:
	# copy of asteroid map and list
	fld = numpy.copy(field)
	ats = asteroids[:]
	# mark current station on map
	fld[stat[1]][stat[0]] = "x"
	# while there are still uninspected astroids
	while len(ats) != 0:
		# remove one from the list
		cur = ats.pop()
		# if it's already marked, continue
		sign = fld[cur[1]][cur[0]]
		if sign == "v" or sign == "h" or sign == "x":
			continue
		# calculate x and y for direction vecor
		v_x = cur[0] - stat[0]
		v_y = cur[1] - stat[1]
		# get gcd of x and y
		g = math.gcd(v_x, v_y)
		# calculate offset
		x_offset = v_x // g
		y_offset = v_y // g
		# start coordinate at potential station
		coord = stat
		# start visible at false
		visible_found = False

		while (True):
			# increment coordinates by offset
			coord = (coord[0] + x_offset, coord[1] + y_offset)
			# if coordinates are out of bound break
			if 0 <= coord[0] < dimensions[0] and 0 <= coord[1] < dimensions[1]:
				# if the coordinate is an asteroid, mark it visible or hidden
				if fld[coord[1]][coord[0]] == "#":
					fld[coord[1]][coord[0]] = "h" if visible_found else "v"
					# if visible was found, set all continuous matches for this inspection to hidden
					visible_found = True
			else:
				break
	# calculate visible asteroids for this station
	vs = len([item for sublist in fld for item in sublist if item == "v"])
	# put new data into list
	data.append((stat, vs))
	
# find max data point for visible asteroids
m = max(data, key=lambda x: x[1])
print("Part 1: Max. visibility {} on asteroid {}".format(m[1], m[0]))