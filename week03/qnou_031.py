#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

print("Words with q but no u:", [word.strip() for word in words if word.lower().count("q") >= 2 and word.lower().count("qu") < 2 or "qu" not in word.lower().strip()])
