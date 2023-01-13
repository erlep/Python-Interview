﻿#!/usr/bin/env python3
# RegEx - https://regex101.com
# https://www.w3schools.com/python/python_regex.asp
# What is the difference between re.search and re.match? - https://bit.ly/3QI0hXz
import re

# example code:
my_string = '1   2        3   '

parsed = re.match(r"(\d)\s+(\d)\s+(\d)", my_string)
if parsed:
  print('RegEx: nula', parsed[0])
  print('RegEx: jedna', parsed[1], '  dva', parsed[2], '  tri', parsed[3])
else:
  print('Nic nenasel.')