#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

print("Words containing 17 letters:", [word.strip() for word in words if len(word) == 18])
print("Words containing 18+ letters:", [word.strip() for word in words if len(word) >= 19])
print("Words with 4 a's:", [word.strip() for word in words if word.lower().count('a') == 4])
print("Words with 2+ q's:", [word.strip() for word in words if word.lower().count("q") >= 2])
print("Words containing cie:", [word.strip() for word in words if "cie" in word.lower()])
print("Anagrams of angle:", [word.strip() for word in words if sorted("angle") == sorted(word.lower().strip()) and word.lower().strip() != "angle"])
