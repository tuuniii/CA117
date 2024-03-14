#!/usr/bin/env python3

import sys

litres = int(sys.stdin.readline())
buckets = sys.stdin.readline().split()
count = 0

i = 0
while i < len(buckets) and litres > 0:
  litres -= int(buckets[i])
  if litres >= 0:
    i += 1
print(i)
