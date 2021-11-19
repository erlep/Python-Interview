# -*- coding: utf-8 -*-
# How to Stand Out in a Python Coding Interview - https://is.gd/wDs2GS

import itertools
import string
from collections import Counter
from collections import defaultdict


# enumerate(
# -----------------------------------------------------
#  Iterate With enumerate() Instead of range()
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
  if num % 3 == 0 and num % 5 == 0:
    numbers[i] = 'delitelne 3 a 5'
  elif num % 3 == 0:
    numbers[i] = 'delitelne 3'
  elif num % 5 == 0:
    numbers[i] = 'delitelne 5'
# ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
print(numbers)

# horsi reseni vvvvvvvv
numbers = [45, 22, 14, 65, 97, 72]
for i in range(len(numbers)):
  if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
    numbers[i] = 'delitelne 3 a 5'
  elif numbers[i] % 3 == 0:
    numbers[i] = 'delitelne 3'
  elif numbers[i] % 5 == 0:
    numbers[i] = 'delitelne 5'
# ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
print(numbers)


# list(
# -----------------------------------------------------
# Use List Comprehensions Instead of map() and filter()
numbers = [4, 2, 1, 6, 9, 7]
print(numbers)
def square(x):
  ''' fce vraci ^2 '''
  return x*x
# HORSI - use list(map(
print(' --- use list(map(')
st = list(map(square, numbers))
print(st)

# LEPSI - use fce(x) for x in
# ..............................
print(' --- use fce(x) for x in')
st = [square(x) for x in numbers]
print(st)


# list(
# -----------------------------------------------------
# filter() and its equivalent list comprehension
def is_odd(x):
  ''' fce vraci true pro liche resp ted je 'not' - sude '''
  return (bool(not(x % 2)))
# HORSI - list(filter(fce
print('--- list(filter(fce')
st = list(filter(is_odd, numbers))
print(st)
# LEPSI - x for x in xx if
# ..............................
print('--- x for x in xx if')
st = [x for x in numbers if is_odd(x)]
print(st)

# Format strings With f-Strings
# -----------------------------------------------------
print('--- Format strings With f-Strings')
def get_name_and_decades(nm, age):
  return f"My name is {nm} and I'm {age / 10:.5f} decades old."
st = get_name_and_decades("Maria", 31)
print(st)


# sorted()
# -----------------------------------------------------
# Sort Complex Lists With sorted()
print('--- Sort Complex Lists With sorted()')
st = sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
print(st)

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5}, ]
st = sorted(animals, key=lambda animal: animal['age'], reverse=True)
print(st)


# Store Unique Values With Sets
# -----------------------------------------------------
print('\n --- Store Unique Values With Sets)')
listA = [2, 2, 6, 5, 3, 0, 2, 1, 2, 8, 2, ]
setA = set(listA)
print(listA)
print(setA)


# Save Memory With Generators
# -----------------------------------------------------
print('--- sum([i * i for i in range(1, 1001)])')
st = sum([i * i for i in range(1, 1001)])
print(st)


# Define Default Values in Dictionaries With .get() and .setdefault()
# -----------------------------------------------------
print('--- Define Default Values in Dictionaries With .get() and .setdefault()')
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
# Wrong
if 'name' in cowboy:
  name = cowboy['name']
else:
  name = 'The Man with No Name'
st = name
print(st)
# Correct - use .get()
print("--- get('name', 'The Man with No Name')")
st = name = cowboy.get('name', 'The Man with No Name')
print(st)
st = cowboy
print(st)
# Wrong
if 'name' not in cowboy:
  cowboy['name'] = 'The Man with No Name'
st = name = cowboy['name']
print(st)
# Correct use -  .setdefault()
print('--- .setdefault()')
st = name = cowboy.setdefault('name', 'The Man with No Name')
print(st)
st = cowboy
print(st)


# Handle Missing Dictionary Keys With collections.defaultdict()
# -----------------------------------------------------
print('--- Handle Missing Dictionary Keys With collections.defaultdict()')
grades = [
    ('elliot', 91),
    ('neelam', 89),
    ('bianca', 81),
    ('elliot', 70),
    ('neelam', 98),
    ('elliot', 88)]
# Wrong
student_grades = {}
for name, grade in grades:
  if name not in student_grades:
    student_grades[name] = []
  student_grades[name].append(grade)
st = student_grades
print(st)
# Correct use -  defaultdict(list)
print('--- defaultdict(list)')
student_grades = {}
student_grades = defaultdict(list)
for name, grade in grades:
  student_grades[name].append(grade)
st = student_grades
print(st)


# Count Hashable Objects With collections.Counter
print('--- Count Hashable Objects With collections.Counter')
words = "if there was there was but if \
there was not there was not".split()
print(words)
counts = Counter(words)
# Correct use -  defaultdict(list)
print(counts)
st = counts.most_common(3)
print(st)


# Access Common String Groups With string Constants
"""
string.ascii_letters
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.hexdigits
string.octdigits
string.punctuation
string.printable
string.whitespace
 """
# string.ascii_uppercase
def is_upper(word):
  for letter in word:
    if letter not in string.ascii_uppercase:
      return False
  return True
st = is_upper('Thanks Geir')
print(st)
st = is_upper('LOL')
print(st)


# Generate Permutations and Combinations With itertools
print('--- Permutations and Combinations')
st = friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
print('friends\n', st)
# permutations
st = list(itertools.permutations(friends, r=2))
print('permutations\n', st)
# combinations
st = list(itertools.combinations(friends, r=2))
print('combinations\n', st)

print('--- OkDone.')
