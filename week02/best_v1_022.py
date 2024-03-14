#!/usr/bin/env python3

import sys

try:
  with open(sys.argv[1], 'r') as f:
    max = 0
    for line in f:
      tokens = line.strip().split()
      mark = int(tokens[0])
      name = tokens[1:]
      if max < mark:
        max = mark
        beststud = " ".join(tokens[1:])
    print(f"Best student: {beststud}")
    print(f"Best mark: {max}")
except FileCouldntOpen:
  print(f"The file {sys.argv[1]} could not be opened.")
