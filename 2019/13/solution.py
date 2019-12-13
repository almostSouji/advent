from computer import compute

with open("input.txt", "r") as file:
	program = list(map(int, file.read().split(",")))

def start(program: List[int], values: List[int], message: str = ""):
	state = compute(program, values)
	while True:
		s = compute(*state)
		if  s[-1] == 99:
			return state
		else:
			state = s
