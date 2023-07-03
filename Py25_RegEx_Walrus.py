#!/usr/bin/env python3
# RegEx - https://regex101.com
# https://www.w3schools.com/python/python_regex.asp

# The Walrus Operator
# ● Assignment as an expression: x := 3
# ● New in Python 3.8

import re

email_address = 'abc@def.xy'

# old style
match = re.match(r'\w+@(\w+\.\w+)', email_address)
if match is not None:
  domain = match.groups(1)
  print("domain", domain)

# The Walrus Operator
if match := re.match(r'\w+@(\w+\.\w+)', email_address):
  domain = match.groups(1)
  print("domain", domain)
