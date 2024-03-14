#!/usr/bin/env python3

import sys
import calendar

poem = ['Monday\'s child is fair of face.', 'Tuesday\'s child is full of grace.',
'Wednesday\'s child is full of woe.', 'Thursday\'s child has far to go.',
'Friday\'s child is loving and giving.', 'Saturday\'s child works hard for a living.',
'Sunday\'s child is fair and wise and good in every way.']

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for line in sys.stdin:
  day, month, year = line.strip().split()
  wday = calendar.weekday(int(year), int(month), int(day))
  print(f"You were born on a {weekday[wday]} and " + poem[wday])
