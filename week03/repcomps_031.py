#!/usr/bin/env python3

import sys

def helper(line):
  list = [n for n in range(1, int(line) + 1)]
  return [0 if n % 3 != 0 else n for n in list]

for line in sys.stdin:
  print("Non-multiples of 3 replaced:", helper(line))
