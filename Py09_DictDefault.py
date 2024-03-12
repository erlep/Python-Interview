#!/usr/bin/env python

# 5 Must-Know HIDDEN Features - https://youtu.be/nrN3Gq1A92Y?si=tCkknbGatUT5w_M4

char_count = {}
string = "aaaabbbcccbsbsbsaaa"

# classic dictionary
for char in string:
  if char not in char_count:
    char_count[char] = 0
  char_count[char] += 1

print(f'{char_count=}')

# defaultdict
from collections import defaultdict
def default():
  return 0

char_count_def = defaultdict(default)
for char in string:
  char_count_def[char] += 1

print(f'{char_count_def=}')
