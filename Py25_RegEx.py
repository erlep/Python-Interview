#!/usr/bin/env python3
# RegEx - https://regex101.com
# https://www.w3schools.com/python/python_regex.asp
# What is the difference between re.search and re.match? - https://bit.ly/3QI0hXz
import re

# Pattern Matching Functions
# ● match : matches from the start of the text
# ● search : match anywhere in the text

# example code:
my_string = ' 1   2        3   '

# match
print('match')
parsed = re.match(r"(\d)\s+(\d)\s+(\d)", my_string)
print('parsed:', parsed)
if parsed:
  print('RegEx nula: >>', parsed[0], '<<')
  print('RegEx jedna', parsed[1], '  dva', parsed[2], '  tri', parsed[3])
else:
  print('Nic nenasel.')
print()

# search
print('search')
parsed = re.search(r"(\d)\s+(\d)\s+(\d)", my_string)
print('parsed:', parsed)
if parsed:
  print('RegEx nula: >>', parsed[0], '<<')
  print('RegEx jedna', parsed[1], '  dva', parsed[2], '  tri', parsed[3])
else:
  print('Nic nenasel.')
print()

# search with ':=' - The Walrus Operator
print("search with ':=' - The Walrus Operator")
if parsed := re.search(r"(\d)\s+(\d)\s+(\d)", my_string):
  print('RegEx nula: >>', parsed[0], '<<')
  print('RegEx jedna', parsed[1], '  dva', parsed[2], '  tri', parsed[3])
else:
  print('Nic nenasel.')
print()

# split
txt = "The rain in Spain"
x = re.split(r"\s", txt)
print('Split: \n',x, '\n',type(x))
print()

# sub
txt = "The rain in Spain"
x = re.sub(r"\s", "_", txt)
print('sub: \n',x, '\n',type(x))
print()

# sub with groups
text = "This course is attended by Sarah and Aisha"
pattern = r"^This course is attended by (.+) and (.+)$"
replace = r"Attendes are: \2 and \1."
x = re.sub(pattern, replace, text)
print('sub: \n',x, '\n',type(x))
print()
