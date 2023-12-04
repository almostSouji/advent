import math

with open("input.txt", "r") as file:
    data = file.read()


def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


targetchunk = []
targetchunkzeros = math.inf
chunks = list(chunk_list(data, 25 * 6))

for chunk in chunks:
    zeros = len([letter for letter in chunk if letter == "0"])
    if zeros < targetchunkzeros:
        targetchunk = chunk
        targetchunkzeros = zeros

ones = len([letter for letter in targetchunk if letter == "1"])
twos = len([letter for letter in targetchunk if letter == "2"])

print("Part 1: Answer: {} * {} = {}".format(ones, twos, ones * twos))

colormap = {"0": " ", "1": "0", "2": " "}  # black  # white  # transparent


def compress(pixel, layerlist):
    for layer in layerlist:
        if layer[pixel] != "2":
            return layer[pixel]


picture = [colormap[compress(pixel, chunks)] for pixel in range(25 * 6)]

print("Part 2: Password:\n")
for chunk in chunk_list("".join(picture), 25):
    print(chunk)
