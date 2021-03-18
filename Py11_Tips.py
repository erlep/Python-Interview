# -*- coding: utf-8 -*-
# How to Stand Out in a Python Coding Interview - https://is.gd/wDs2GS

import itertools
import string
from collections import Counter
from collections import defaultdict

# Use List Comprehensions Instead of map() and filter()
numbers = [4, 2, 1, 6, 9, 7]
print(numbers)
def square(x):
  ''' fce vraci ^2 '''
  return x*x
# use list(map(
st = list(map(square, numbers))
print(st)
# use fce(x) for x in
st = [square(x) for x in numbers]
print(st)

# filter() and its equivalent list comprehension
def is_odd(x):
  ''' fce vraci true pro liche resp ted je 'not' - sude '''
  return (bool(not(x % 2)))
# list(filter(fce
st = list(filter(is_odd, numbers))
print(st)
# x for x in xx if
st = [x for x in numbers if is_odd(x)]
print(st)

# Format strings With f-Strings
def get_name_and_decades(name, age):
  return f"My name is {name} and I'm {age / 10:.5f} decades old."
st = get_name_and_decades("Maria", 31)
print(st)

# Sort Complex Lists With sorted()
st = sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
print(st)

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5}, ]
st = sorted(animals, key=lambda animal: animal['age'], reverse=True)
print(st)

# Store Unique Values With Sets
# list wrong - not Unique
# words = []
# words.append(word)
# use Set
# words = set()
# words.add(get_random_word())

# Save Memory With Generators
st = sum([i * i for i in range(1, 1001)])
print(st)

# Define Default Values in Dictionaries With .get() and .setdefault()
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
# Wrong
if 'name' in cowboy:
  name = cowboy['name']
else:
  name = 'The Man with No Name'
st = name
print(st)
# Correct - use .get()
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
st = name = cowboy.setdefault('name', 'The Man with No Name')
print(st)
st = cowboy
print(st)

# Handle Missing Dictionary Keys With collections.defaultdict()
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
student_grades = {}
student_grades = defaultdict(list)
for name, grade in grades:
  student_grades[name].append(grade)
st = student_grades
print(st)

# Count Hashable Objects With collections.Counter
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
st = friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
print('friends\n', st)
# permutations
st = list(itertools.permutations(friends, r=2))
print('permutations\n', st)
# combinations
st = list(itertools.combinations(friends, r=2))
print('combinations\n', st)
