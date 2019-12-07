from computer import compute
import itertools as itert

with open("input.txt", "r") as file:
	program = file.read().split(",")

permutations = list(map(list, itert.permutations([0,1,2,3,4])))

def calcOut (config):
	val = 0
	for i in range(0, len(config)):
		res = compute(program, [val, config[i]], 0)
		val = res[1]
	return val

values = list(map(lambda config : calcOut(config),permutations))
print("Part 1: Max thruster output: {} with thruster signal {}".format(max(values), permutations[values.index(max(values))]))
