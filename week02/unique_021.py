#!/usr/bin/env python3

import sys
import re

text = sys.stdin.read().strip().lower()
text = re.sub("\W+", ' ', text).split()
unique = []

for word in text:
  if word not in unique:
    unique.append(word)

print(len(unique))
