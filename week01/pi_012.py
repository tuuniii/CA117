#!/usr/bin/env python3

import sys
from math import pi

for num in sys.stdin:
  print(f'{pi:1.{int(num)}f}')
