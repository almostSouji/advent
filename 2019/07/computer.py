def compute(program, parameters, pointer = 0):
	prog = program[:]
	finished = False
	maxParamCount = 3
	while not finished:
		instruction = prog[pointer]
		op = int(instruction[-2:])
		modes = str(instruction)[:-2].zfill(maxParamCount)#
		# 3 parameter instructions
		if op in [1,2,7,8]:
			p1 = int(prog[int(prog[pointer + 1])]) if modes[2] == "0" else int(prog[pointer + 1])
			p2 = int(prog[int(prog[pointer + 2])]) if modes[1] == "0" else int(prog[pointer + 2])
			if op == 1:
				prog[int(prog[pointer + 3])] = str(p1 + p2)
			elif op == 2:
				prog[int(prog[pointer + 3])] = str(p1 * p2)
			elif op == 7:
				prog[int(prog[pointer + 3])] = "1" if p1 < p2 else "0"
			else:
				prog[int(prog[pointer + 3])] = "1" if p1 == p2 else "0"
			pointer = pointer + 4
		# 2 parameter instructions
		elif op in [5,6]:
			p1 = int(prog[int(prog[pointer + 1])]) if modes[2] == "0" else int(prog[pointer + 1])
			p2 = int(prog[int(prog[pointer + 2])]) if modes[1] == "0" else int(prog[pointer + 2])
			if op == 5:
				pointer = p2 if p1 == 1 else pointer + 3
			else:
				pointer = p2 if p1 == 0 else pointer + 3
		# 1 parameter instructions
		elif op in [3,4]:
			if op == 3:
				prog[int(prog[pointer + 1])] = parameters.pop()
			else:
				val = int(prog[int(prog[pointer + 1])]) if modes [2] == "0" else int(prog[pointer + 1])
				return (prog, val, pointer)
			pointer = pointer + 2
		elif op == 99:
			finished = True
		else:
			raise Exception("Unknown opcode: {}".format(op))
	print("------")
	return True