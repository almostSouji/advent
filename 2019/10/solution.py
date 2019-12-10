from typing import Tuple, List

# test 1: (3, 4) with 8
# test 2: (5, 8) with 33
# test 3: (1, 2) with 35
# test 4: (6, 3) with 41
# test 5: (11, 13) with 210

with open("input.txt", "r") as file:
	field = list(map(list, file.read().split("\n")))

for line in field:
	print(line)

ASTEROID = "#"

dimensions = (len(field[0]),len(field))
asteroids: List[Tuple[int, int]] = []

for x in range(0, dimensions[0] - 1):
	for y in range(0, dimensions[1] - 1):
		if field[x][y] == "#":
			asteroids.append((x, y))

print(asteroids)

station
# each asteroid is a potential station
for stat in asteroids:
	# check for each asteroid in the field
	for a in asteroids:
		x_dist = 
		y_dist =