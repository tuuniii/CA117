#!/usr/bin/env python3

import re
import sys

delimiters = [',', '.', ':']

for line in sys.stdin:
  line = line.lower().strip()
  line = re.sub('\W+', '', line)
  i = 0
  while i < len(line) and line[i] == line[len(line) - i - 1]:
    i += 1
  if i < len(line):
    print(False)
  else:
    print(True)
