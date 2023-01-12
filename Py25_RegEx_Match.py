#!/usr/bin/env python3
# RegEx - https://regex101.com
# https://www.w3schools.com/python/python_regex.asp
# What is the difference between re.search and re.match? - https://bit.ly/3QI0hXz
import re

# example code:
string_with_newlines = """something
someotherthing"""

print("'re.match('some'  ",re.match('some', string_with_newlines))  # matches
print("'re.match('someo  ",re.match('someother', string_with_newlines))  # won't match
print("'re.match('^someo ",re.match('^someother', string_with_newlines, re.MULTILINE))  # also won't match
print("'re.search('someot",re.search('someother', string_with_newlines))  # finds something
print("'re.search('^someo",re.search('^someother', string_with_newlines, re.MULTILINE))  # also finds something

print("\nre.compile('thing$', re.MULTILINE)")
m = re.compile('thing$', re.MULTILINE)
print(m.match(string_with_newlines))  # no match
print(m.match(string_with_newlines, pos=4))  # matches
print(m.search(string_with_newlines, re.MULTILINE))  # also matches
