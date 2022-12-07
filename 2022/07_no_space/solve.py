#!/usr/bin/env python3
import sys
import pprint


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

####


def dir_sizes(elem, b=[]):
    match elem:
        case (_, s):
            return (s, b)
        case (_, _, children):
            sm = sum(map(lambda x: dir_sizes(x)[0], children))
            b.append(sm)
            return (sm, b)


# dir := (name, parent, children)
# file := (name, size)
root = ("root", None, [])
current = root

total_space = 70000000
size_update = 30000000

for raw_line in sys.stdin:
    line = raw_line.strip()

    match line.split(" "):
        case "$", "cd", "/":
            current = root
        case "$", "cd", "..":
            current = current[1]
        case "$", "cd", to:
            for (i, e) in enumerate(current[2]):
                if e[0] == to:
                    current = current = e
        case "$", "ls":
            continue
        case "dir", name:
            current[2].append(
                (name, current, [])
            )
        case s, name if s.isdigit():
            current[2].append(
                (name, int(s))
            )

(total_size, sizes) = dir_sizes(root)
current_space = total_space - total_size

print(sum([x for x in sizes if x <= 100000]))
print(min([x for x in sizes if current_space+x >= size_update]))
