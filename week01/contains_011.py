#!/usr/bin/env python3

import sys

def contains(left, right):
  '''Return True if all of left contained in right and False otherwise'''
  for c in left:
    if c not in right:
      return False
    right = right.replace(c, '', 1)
  return True

for line in sys.stdin:
  left, right = line.strip().split()
  print(contains(left.lower(), right.lower()))
