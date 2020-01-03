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
print("Part 1: Max thruster output: {} with thruster signals: {}".format(max(values), permutations[values.index(max(values))]))

p2permutations = list(map(list, itert.permutations([5, 6, 7, 8, 9])))

def p2calcOut (config):
	# (state, pointer, finished, last_value)
	thrusterstates = []
	val = 0
	
	for i in range(0, len(config)):
		thrusterstates.append(compute(program, [val, config[i]]))
		val = thrusterstates[-1][-1]
	while any(list(map(lambda state: not state[2] ,thrusterstates))):
		for i in range (0, len(config)):
			c_state, c_pointer, c_finished, c_last_value = thrusterstates[i]
			state, pointer, is_finished, value = compute(c_state, [val], c_pointer)
			if (not is_finished):
				thrusterstates[i] = (state, pointer, is_finished, value)
				val = value
			else:
				thrusterstates[i] = (state, pointer, is_finished, c_last_value)
	return (thrusterstates[-1][3], config)

values = list(map(lambda config : p2calcOut(config), p2permutations))

ceil = max(values, key=lambda x: x[0])
print("Part 2: Max thruster output: {} with thruster signals: {}".format(ceil[0], ceil[1]))
