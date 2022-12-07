#!/usr/bin/env python3
import sys
import pprint
from collections import namedtuple


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
        case File(_, s):
            return (s, b)
        case Dir(_, _, children):
            sm = sum([dir_sizes(x)[0] for x in children])
            b.append(sm)
            return (sm, b)


Dir = namedtuple("Dir", ["name", "parent", "children"])
File = namedtuple("File", ["name", "size"])

root = Dir("root", None, [])
current = root

MAX_SIZE = 100_000
TOTAL_SPACE = 70_000_000
SIZE_UPDATE = 30_000_000

for raw_line in sys.stdin:
    line = raw_line.strip()

    match line.split(" "):
        case "$", "cd", "/":
            current = root
        case "$", "cd", "..":
            current = current.parent
        case "$", "cd", to:
            for (i, e) in enumerate(current.children):
                if e.name == to:
                    current = e
        case "$", "ls":
            continue
        case "dir", name:
            current.children.append(
                Dir(name, current, [])
            )
        case s, name if s.isdigit():
            current.children.append(
                File(name, int(s))
            )

(total_size, sizes) = dir_sizes(root)
current_space = TOTAL_SPACE - total_size

print(sum([x for x in sizes if x <= MAX_SIZE]))
print(min([x for x in sizes if current_space+x >= SIZE_UPDATE]))
