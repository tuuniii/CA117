#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
  line = lines[i].strip()
  if line[1:-1] != "":
    print(line[1:-1])
  i += 1
