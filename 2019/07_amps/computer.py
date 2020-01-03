""" Computes int codes with given parameters

Args:
	program (string[]): The program to run
	parameters (string[]): Parmeters the program can read from
	pointer (int): Starting point for the pointer, 0 if none

About:
	Instructions consist of OP-CODES and parameter modes as well as parameters
	Legal parameters depend on instruction given
	ABCDE
	321OP
	A,B,C give modes for param 3,2,1

MODES:
	0 POSITION (use value as position)
	1 IMMEDIATE (use value as direct value)

OP-CODES:
	1 ADD (add p1 + p2, save in p3)
	2 MULTIPLY (multiply p1 * p2, save in p3)
	3 GET-INPUT (get input, save in p1)
	4 RETURN (print p1)
	5 JUMP-IF-TRUE (if p1 is non-zero set pointer to p2)
	6 JUMP-IF-FALSE (if p1 is zero set pointer to p2)
	7 LESS THAN (if p1 is less than p2 store 1 in p3, else store 0 in p3)
	8 EQUALS (if p1 equals p2 store 1 in p3, else store 0 in p3)
	99 HALT
"""

def compute(program, parameters, pointer = 0):
	prog = program[:]
	finished = False
	maxParamCount = 3
	while not finished:
		instruction = prog[pointer].zfill(maxParamCount + 2)
		op = int(instruction[-2:])
		modes = str(instruction)[:-2]
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
				pointer = p2 if p1 != 0 else pointer + 3
			else:
				pointer = p2 if p1 == 0 else pointer + 3
		# 1 parameter instructions
		elif op in [3,4]:
			if op == 3:
				prog[int(prog[pointer + 1])] = parameters.pop()
				pointer = pointer + 2
			else:
				val = int(prog[int(prog[pointer + 1])]) if modes [2] == "0" else int(prog[pointer + 1])
				pointer = pointer + 2
				return (prog, pointer, False, val)
		elif op == 99:
			return (prog, pointer, True, 0)
		else:
			raise Exception("Unknown opcode: {}".format(op))
	raise Exception("The program did not finish with OP 99")