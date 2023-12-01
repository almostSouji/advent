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

nums = []
nums2 = []
for line in open(0):
  buffer = ""
  buffer2 = ""
  wordbuffer = ""
  for c in line:
      if c.isdigit():
          buffer += c
          buffer2 += c
          break
              
      else:
          wordbuffer += c
          for i, word in enumerate(numbers):
              if word in wordbuffer:
                  buffer2 += str(i)
                  break
  wordbuffer = ""
  for c in line[::-1]:
      if c.isdigit():
          buffer += c
          buffer2 += c
          break
      else:
          wordbuffer += c
          for i, word in enumerate(numbers):
              if word[::-1] in wordbuffer:
                  buffer2 += str(i)
                  break
          else:
              continue
          break

  nums.append(int(buffer[0]+buffer[-1]))
  nums2.append(int(buffer2[0]+buffer2[-1])) 

  buffer = ""
  buffer2 = ""

print(sum(nums))
print(sum(nums2))
