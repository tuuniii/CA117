#!/usr/bin/env python3

import sys

def anagram(l, r):
  if len(l) != len(r):
    return False
  for c in l:
    if c not in r:
      return False
    r = r.replace(c, '', 1)
  return True

for line in sys.stdin:
  left, right = line.strip().split()
  print(anagram(left, right))
