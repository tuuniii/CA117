#!/usr/bin/env python3

import sys
lines = sys.stdin.read().split()

i = 0
while i < len(lines):
  if len(lines[i]) % 2 == 0:
    print("No middle character!")
  else:
    print(lines[i][len(lines[i]) // 2])
  i += 1
