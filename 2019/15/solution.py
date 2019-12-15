from computer import compute
from typing import List
with open("input.txt", "r") as file:
	program = list(map(int, file.read().split(",")))