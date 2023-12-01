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

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_rev = [word[::-1] for word in numbers]

def find_num(text, alphabet, allow_alphabet=False): 
    buffer = ""
    for c in text:
        if c.isdigit():
            return c
        elif allow_alphabet:
            buffer += c
            for i, word in enumerate(alphabet):
                if word in buffer:
                    return str(i + 1)

s = 0
s2 = 0
for line in open(0):
  ns = [find_num(line, numbers), find_num(line[::-1], numbers)]
  ns2 = [find_num(line, numbers, True), find_num(line[::-1], numbers_rev, True)]
  s += int(ns[0]+ns[-1])
  s2 += int(ns2[0]+ns2[-1])

print(s)
print(s2)
