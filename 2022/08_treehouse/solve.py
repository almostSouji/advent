#!/usr/bin/env python3
import sys
import pprint
from numpy import prod


def debug(*args, pretty=False, **kwargs):
    "print() to stderr for debuggin purposes"
    if pretty:
        pprint.pprint(*args, **kwargs, stream=sys.stderr)
    else:
        print(
            *args,
            **kwargs,
            file=sys.stderr,
        )


def print_field(field):
    for row in field:
        debug(row)


####


def update_tree(field, i, j, highest):
    tree = field[i][j]
    val = tree[0]

    if val > highest:
        field[i][j] = (val, "#", 1)
        highest = val

    return highest


def score_tree(field, i, j):
    x_dim, y_dim = len(field[0]), len(field)
    tree = field[i][j]
    scores = []

    s = 0
    for x in range(i + 1, x_dim):
        s += 1
        if field[x][j][0] >= tree[0]:
            break
    scores.append(s)

    s = 0
    for x in range(i - 1, -1, -1):
        s += 1
        if field[x][j][0] >= tree[0]:
            break
    scores.append(s)

    s = 0
    for x in range(j + 1, y_dim):
        s += 1
        if field[i][x][0] >= tree[0]:
            break
    scores.append(s)

    s = 0
    for x in range(j - 1, -1, -1):
        s += 1
        if field[i][x][0] >= tree[0]:
            break
    scores.append(s)

    hei, sym, _ = tree
    field[i][j] = (hei, sym, prod(scores))
    return field


field = []

for raw_line in sys.stdin:
    line = raw_line.strip()
    if len(line) == 0:
        continue
    field.append([(int(x), " ", 1) for x in list(line)])

for i in range(len(field)):
    highest = -1
    for j in range(len(field[0])):
        highest = update_tree(field, i, j, highest)

    highest = -1
    for j in range(len(field[0]) - 1, -1, -1):
        highest = update_tree(field, i, j, highest)

for j in range(len(field[0])):
    highest = -1
    for i in range(len(field)):
        highest = update_tree(field, i, j, highest)

    highest = -1
    for i in range(len(field) - 1, -1, -1):
        highest = update_tree(field, i, j, highest)

print(sum([len([element for element in row if element[1] == "#"]) for row in field]))

for i in range(len(field)):
    for j in range(len(field[0])):
        score_tree(field, i, j)

print(max([max([element[2] for element in row]) for row in field]))
