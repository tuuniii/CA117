#!/usr/bin/env python3

import sys

es = ["ch", "sh", "x", "s", "z", "o"]
vowels = ["a", "o", "u", "e", "i"]

for line in sys.stdin:
  line = line.strip()
  if line[-2:] in es:
    print(line + 'es')
  elif line[-1] in es:
    print(line + 'es')
  elif line[-1] == "y" and line[-2] not in vowels:
    print(line[:-1] + 'ies')
  elif line[-1] == "f":
    print(line[:-1] + 'ves')
  elif line[-2:] == "fe":
    print(line[:-2] + 'ves')
  elif line[-1] == "o":
    print(line + 'es')
  else:
    print(line + 's')
