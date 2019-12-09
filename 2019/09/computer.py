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
	2 RELATIVE (position from rel base)

OP-CODES:
	1 ADD (add p1 + p2, save in p3)
	2 MULTIPLY (multiply p1 * p2, save in p3)
	3 GET-INPUT (read input from stack, save in p1)
	4 RETURN (return p1)
	5 JUMP-IF-TRUE (if p1 is non-zero set pointer to p2)
	6 JUMP-IF-FALSE (if p1 is zero set pointer to p2)
	7 LESS THAN (if p1 is less than p2 store 1 in p3, else store 0 in p3)
	8 EQUALS (if p1 equals p2 store 1 in p3, else store 0 in p3)
	9 REL (adjust relative base (increase or decrease by value))
	99 HALT
"""

def compute(program, parameters, pointer = 0):
	prog = program[:] + ["0"] * 100
	finished = False
	maxParamCount = 3
	offset = 0
	while not finished:
		instruction = prog[pointer].zfill(maxParamCount + 2)
		op = int(instruction[-2:])
		modes = str(instruction)[:-2]
		# 3 parameter instructions
		if op in [1,2,7,8]:
			# get values
			p1, p2, p3_adress
			# based on modes
			# p1 modes
			if modes[2] == "0":
				p1 = int(prog[int(prog[pointer + 1])])
			elif modes[2] == "1":
				p1 = int(prog[pointer + 1])
			elif modes[2] == "2":
				p1 = int(prog[int(prog[pointer + 1]) + offset])
			# p2 modes
			if modes[1] == "0":
				p2 = int(prog[int(prog[pointer + 2])])
			elif modes[1] == "1":
				p2 = int(prog[pointer + 2])
			elif modes[1] == "2":
				p2 = int(prog[int(prog[pointer + 1]) + offset])
			else:
				raise Exception("Invalid mode")
			# p3 modes
			if modes[0] == "0":
				p3_adress = int(prog[pointer + 3])
			elif modes[0] == "1":
				raise Exception("Invalid Mode (immediate not valid for register location)")
			elif modes[0] == "2":
				p3_adress = int(prog[pointer + 3]) + offset
			else:
				raise Exception("Invalid mode")
			# discern opcodes
			if op == 1:
				prog[p3_adress] = str(p1 + p2)
			elif op == 2:
				prog[p3_adress] = str(p1 * p2)
			elif op == 7:
				prog[p3_adress] = "1" if p1 < p2 else "0"
			elif op == 8:
				prog[p3_adress] = "1" if p1 == p2 else "0"
			else:
				raise Exception("Invalid OP")
			pointer = pointer + 4
		# 2 parameter instructions
		elif op in [5,6]:
			p1, p2
			# p1 modes
			if modes[2] == "0":
				p1 = int(prog[int(prog[pointer + 1])])
			elif modes[2] == "1":
				p1 = int(prog[pointer + 1])
			elif modes[2] == "2":
				p1 = int(prog[int(prog[pointer + 1]) + offset])
			else:
				raise Exception("Invalid mode")
			# p2 modes
			if modes[1] == "0":
				p2 = int(prog[int(prog[pointer + 2])])
			elif modes[1] == "1":
				p2 = int(prog[pointer + 2])
			elif modes[1] == "2":
				p2 = int(prog[int(prog[pointer + 1]) + offset])
			else:
				raise Exception("Invalid mode")
			# discern opcodes
			if op == 5:
				pointer = p2 if p1 != 0 else pointer + 3
			elif op == 6:
				pointer = p2 if p1 == 0 else pointer + 3
			else:
				raise Exception("invalid op")
		# 1 parameter instructions
		# 3 GET - l r
		# 4 RET - l i r 
		# 9 ADJ - l i r
		elif op in [3,4,9]:
			# discern op 3 because it is register location rather than value
			if op == 3:
				if modes[0] == "0":
					prog[int(prog[pointer + 1])] = parameters.pop()
				elif modes[0] == "1":
					raise Exception("Invalid mode (immediate not valid for register locations)")
				elif modes[0] == "2":
					prog[int(prog[pointer + 1]) + offset] = parameters.pop()
				pointer = pointer + 2
			else:
				# calculate value prameters for other ops
				p1
				if modes[2] == "0":
					p1 = int(prog[int(prog[pointer + 1])])
				elif modes[2] == "1":
					p1 = int(prog[pointer + 1])
				elif modes[2] == "2":
					p1 = int(prog[int(prog[pointer + 1]) + offset])
				else:
					raise Exception("Invalid mode") 
				if op == 4:
					pointer = pointer + 2
					return (prog, pointer, False, p1)
				elif op == 9:
					offset = offset + p1
					pointer = pointer + 2
				else:
					raise Exception("Invalid op")
		elif op == 99:
			return (prog, pointer, True, 0)
		else:
			raise Exception("Unknown opcode: {}".format(op))
	raise Exception("The program did not finish with OP 99")
