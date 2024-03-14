#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
vowels = 'aeiou'

print("Shortest word containing all vowels:", min([word.strip() for word in words if all(vowel in word for vowel in vowels)], key=len))
print("Words ending in iary:", len([word for word in words if "iary" in word.lower()]))
##print("Words with most e's:", [word.strip() for word in words if word.count('e'))])
count = []
for word in words:
  count.append(word.count('e'))
highest = max(count)
print("Words with most e's:", [word.strip() for word in words if word.count('e') == highest])
