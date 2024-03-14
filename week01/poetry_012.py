#!/usr/bin/env python3

import sys

poem = sys.stdin.readlines()
i = 0
max = 0
while i < len(poem):
  if len(poem[i].strip()) > max:
    max = len(poem[i]) - 1
  i += 1

for line in poem:
  print(f'{line.strip():^{int(max)}}')
