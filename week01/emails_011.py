#!/usr/bin/env python3

import sys

for line in sys.stdin:
  tokens = line.strip().split(".")
  name = tokens[0]
  right = tokens[1].split("@")
  surname = right[0]
  i = 0
  while i < len(surname) and surname[i] >= "a" and surname[i] <= "z":
    i += 1
  surname = surname[:i]
  print(name.capitalize() + " " + surname.capitalize())
