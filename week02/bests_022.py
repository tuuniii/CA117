#!/usr/bin/env python3

import sys

try:
  with open(sys.argv[1], 'r') as f:
    beststud = {}
    for line in f:
      try:
        tokens = line.strip().split()
        mark = int(tokens[0])
        name = tokens[1:]
        beststud[" ".join(name)] = mark
      except ValueError:
        print(f"Invalid mark {tokens[0]} encountered. Skipping.")

except FileCouldntOpen:
  print(f"The file {sys.argv[1]} could not be opened.")

finally:
    highest = max(beststud.values())
    toppers_list = [name for name, score in beststud.items() if score == highest]
    str1 = ', '.join(toppers_list)
    print(f"Best student(s): {str1}")
    print(f"Best mark: {highest}")
