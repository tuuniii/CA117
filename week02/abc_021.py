#!/usr/bin/env python3

import sys

first = sys.stdin.readline().split()
order = sys.stdin.readline()

nums = []
for num in first:
  nums.append(int(num))
nums.sort()

for c in order:
  if c == "A":
    order = order.replace(c, str(nums[0]) + " ", 1)
  elif c == "C":
    order = order.replace(c, str(nums[2]) + " ", 1)
  elif c == "B":
    order = order.replace(c, str(nums[1]) + " ", 1)
print(order.strip())
