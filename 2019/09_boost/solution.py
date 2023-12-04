from computer import runMultiple, runSingle

with open("input.txt", "r") as file:
    program = list(map(int, file.read().split(",")))

runMultiple([program[:], program[:]], [[1], [2]], ["Part 1:", "Part 2:"])
