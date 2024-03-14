#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  i = 0
  while i < len(line) and line[i][0] != "m":
    i += 1
  if i < len(line):
    line[i] = line[i].capitalize()
  print(" ".join(line))
