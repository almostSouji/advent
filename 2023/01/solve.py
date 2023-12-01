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

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
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
                    return str(i)


nums = []
nums2 = []
for line in open(0):
  ns = [find_num(line, numbers), find_num(line[::-1], numbers)]
  ns2 = [find_num(line, numbers, True), find_num(line[::-1], numbers_rev, True)]
  nums.append(int( ns[0]+ns[-1]))
  nums2.append(int(ns2[0]+ns2[-1]))

print(sum(nums))
print(sum(nums2))
