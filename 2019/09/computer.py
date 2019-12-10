from typing import List

EXP_INVALID_MODE = "invalid mode: {}"
EXP_INVALID_POINTER = "pointer out of register range"
EXP_INVALID_OP = "invalid op code: {}"
MEMORY_SIZE = 10000
ROCKET = """
        |  
  *    / \ 
      / _ \ 
     |.o '.|  * 
     |'._.'| 
     |     | 
*  ,'|  |  |`. 
  /  |  |  |  \ 
  |,-'--|--'-.|
"""

def printRocket():
	for line in ROCKET.split("\n"):
		print(line)

def runMultiple(programs: List[List[int]], values: List[List[int]], messages: List[str] = [""]):
	printRocket();
	states = list(range(0, len(programs)))
	ss = list(range(0, len(programs)))
	
	for i in range(0, len(programs)):
		states[i] = compute(programs[i], values[i])
		print(("".join(" " * (8 - len(messages[i]) // 2)) + messages[i]))
		while True:
			print(("".join(" " * (8 - len(str(states[i][-2])) // 2)) + str(states[i][-2])))
			print("")
			ss[i] = compute(*states[i])
			if  ss[i][-1] == 99:
				break
			else:
				state = ss[i]
	return states

def runSingle(program: List[int], values: List[int], message: str = ""):
	printRocket()
	state = compute(program, values)
	print(("".join(" " * (8 - len(message) // 2)) + message))
	while True:
		print(("".join(" " * (8 - len(str(state[-2])) // 2)) + str(state[-2])))
		s = compute(*state)
		if  s[-1] == 99:
			return state
		else:
			state = s

""" Compute int codes with given parameters

Args:
	program (List[int]): The intcode program to run
	input (List[int]): Input parameters, if any
	pointer (int): Pointer value - part of state
	base (int): Base value - part of state
	last_value (int): Last returned value - part of state
	last_op (int): Last returned opcode - part of state

About:
	Instructions consist of operation codes and parameter modes as well as parameters
	Legal parameters depend on instruction given
	ABCDE
	321OP
	A,B,C give modes for param 3,2,1
	DE determine operation codes
	parameters are the next n values after the operation instruction and based on modes and operationcodes

Modes:
	0 POSITION (use value in adress as adress)
	1 IMMEDIATE (use value in adress)
	2 RELATIVE (use value in adress as adress after adding base to it)

OP-Codes:
	1 ADD parameter3^ <- parameter1 + parameter2
	2 MUL parameter3^ <- parameter1 * parameter2
	3 GET parameter1^ <- in
	4 RET parameter1 -> out
	5 JIT pointer <- parameter2 if parameter1 != 0
	6 JIF pointer <- parameter2 if parameter1 == 0
	7 LT parameter3^ <- 1 if parameter1 < parameter2 else 0
	8 EQ parameter3^ <- 1 if parameter1 == parameter2 else 0
	9 BSE base <- base + parameter1
	99 HLT stop execution
	^ parameters needs to be provided with mode 0 or 2
"""

def compute(prg: List[int], inp: List[int] = [], pnt: int = 0, bse: int = 0, last_val: int = 0, last_op: int = 0):
	# get value with provided index and mode
	def getVal(idx: int, mod: int):
		if mod == 0:
			return prg[prg[idx]]
		elif mod == 1:
			return prg[idx]
		elif mod == 2:
			return prg[prg[idx] + bse]
		else:
			raise Exception(EXP_INVALID_MODE.format(mod))
		return False

	# get address with provided index and mode
	def getAdr(idx: int, mod: int):
		if mod == 0:
			return prg[idx]
		if mod == 1:
			# these should never be used by a program
			# still need to be computed for general parameter assignment
			return 0
		if mod == 2:
			return prg[idx] + bse
		else:
			raise Exception(EXP_INVALID_MODE.format(mod))

	prg = prg[:] + [0] * (MEMORY_SIZE - len(prg))
	op = 0
	while op != 99:
		op = prg[pnt] % 100
		mod1 = prg[pnt] // 100 % 10 
		mod2 = prg[pnt] // 1000 % 10 
		mod3 = prg[pnt] // 10000 % 10
		# parameters
		# exceptions are out of range for various parameters
		# occurring if they're used with wrong modes for this specific input
		try: p1 = getVal(pnt + 1, mod1)
		except: p1 = 0
		try: p2 = getVal(pnt + 2, mod2)
		except: p2 = 0
		try: p3 = getVal(pnt + 3, mod3)
		except: p3 = 0
		try: p1_a = getAdr(pnt + 1, mod1)
		except: pass
		try: p2_a = getAdr(pnt + 2, mod2)
		except: pass
		try: p3_a = getAdr(pnt + 3, mod3)
		except: pass
		# op-handling
		if op == 1:
			prg[p3_a] = p1 + p2
			pnt += 4
		elif op == 2:
			prg[p3_a] = p1 * p2
			pnt += 4
		elif op == 3:
			val = inp.pop()
			prg[p1_a] = val
			pnt += 2
		elif op == 4:
			pnt += 2
			return (prg, inp, pnt, bse, p1 ,op)
		elif op == 5:
			pnt = p2 if p1 != 0 else pnt + 3
		elif op == 6:
			pnt = p2 if p1 == 0 else pnt + 3
		elif op == 7:
			prg[p3_a] = 1 if p1 < p2 else 0
			pnt += 4
		elif op == 8:
			prg[p3_a] = 1 if p1 == p2 else 0
			pnt += 4
		elif op == 9:
			bse += p1
			pnt += 2
		elif op == 99:
			return (prg, inp, pnt, bse, 0, op)
		else:
			raise Exception(EXP_INVALID_OP.format(op))
	return False