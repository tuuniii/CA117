#!/usr/bin/env python3

import sys

for line in sys.stdin:
  classCount = [0, 0, 0, 0]
  line = line.strip()
  for c in line:
    if c.islower():
      classCount[1] = 1
    elif c.isdigit():
      classCount[0] = 1
    elif c.isalpha():
      classCount[2] = 1
    else:
      classCount[3] = 1
  print(sum(classCount))
