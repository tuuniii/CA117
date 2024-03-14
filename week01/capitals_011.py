#!/usr/bin/env python3

import sys
lines = sys.stdin.read().split()

i = 0
while i < len(lines):
  line = lines[i].capitalize()
  line = line[:-1] + line[-1].capitalize()
  print(line)
  i += 1
