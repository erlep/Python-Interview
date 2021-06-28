# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 5 - Python Data Types - https://www.w3schools.com/python/python_datatypes.asp
#    when to use - go python list vs array vs tuple vs set - https://is.gd/AlND3o

#  Tuples are fixed size in nature whereas lists are dynamic.
#  In other words, a tuple is immutable whereas a list is mutable.
#
#  - You can't add elements to a tuple. Tuples have no append or extend method.
#  - You can't remove elements from a tuple. Tuples have no remove or pop method.
#  - You can find elements in a tuple, since this doesn�t change the tuple.
#  - You can also use the in operator to check if an element exists in the tuple.
#                                                            Mutable Ordered Change
#  List  - lze menit prvky, pristup dle indexu                   1     1       1
#  Tuple - je rychlejsi, a mensi velikost                        0     1       0
#  Set   - optimalizace na zjisteni zda obsahuje element         1     0       0
#  Tuples have structure, lists have order

# list tuple range dict set - list-tuple-range-dict-set
# Lists    - [] - https://www.w3schools.com/python/python_lists_methods.asp
# Tuples   - () - https://www.w3schools.com/python/python_tuples_methods.asp
# Sets     - {} - https://www.w3schools.com/python/python_sets_methods.asp
# Dictionaries - {"key":"value"} - https://www.w3schools.com/python/python_dictionaries_methods.asp

#  # Size
#  a = tuple(range(1000))
#  b = list(range(1000))
#  a.__sizeof__() # 8024
#  b.__sizeof__() # 9088
#
#  # Permitted operations
#  b    = [1,2]
#  b[0] = 3       # [3, 2]
#  a    = (1,2)
#  a[0] = 3       # Error
#
#  # Usage - As a list is mutable, it can't be used as a key in a dictionary, whereas a tuple can be used.
#  a    = (1,2)
#  b    = [1,2]
#  c = {a: 1}     # OK
#  c = {b: 1}     # Error


# list []
x = ["cherry", "apple", "banana", "banana"]
print('\n list - x = ["apple", "banana", "cherry", "banana"]')
print("x: ", x, " - type: ", type(x))
print('for i in x:')
for i in x:
  print(i)
print('for i, fruit in enumerate(x):')
for i, fruit in enumerate(x, start=11):
  print('i:', i, ' fruit:', fruit)


# tuple ()
x = ("cherry", "apple", "banana", "banana")
print('\n tuple - x = ("apple", "banana", "cherry", "banana")')
print("x: ", x, " - type: ", type(x))
for i in x:
  print(i)


# set  {}
x = {"cherry", "apple", "banana", "banana"}
print('\n set - x = {"cherry", "apple", "banana", "banana"}')
print("x: ", x, " - type: ", type(x))
for i in x:
  print(i)
# Optimalizace na rychlost
obsahuje = "banana" in x
print("Je tam banan?", obsahuje)


# dict  {:}
print(
    '\n dict - x = {"name" : "John", "age" : 36, "Occupation" : "Teacher", "age" : 36}'
)
x = {"name": "John", "age": 36, "Occupation": "Teacher", "age": 36}
print("x: ", x, " - type: ", type(x))
for key, val in x.items():
  print("key:", key, "  val:", val)


# range
print("\n range - x = range (3)")
x = range(3)
print("x: ", x, " - type: ", type(x))
for i in x:
  print(i)


print("\nOkDone.")
