# -*- coding: utf-8 -*-
# % Python How To - https://www.w3schools.com/python/python_howto_remove_duplicates.asp

print(' How to Remove Duplicates From a Python List')
# How to Remove Duplicates From a Python List
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# Create a Function - How to Remove Duplicates From a Python List
def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)

print('\n How to Reverse a String in Python')
# How to Reverse a String in Python
txt = "Hello World"[::-1]
print(txt)

# Python - Slicing Strings - https://www.w3schools.com/python/python_strings_slicing.asp
print('txt = "Hello World"')
txt = "Hello World"
print(txt)

# Get the characters from position 1 to position 3 (not included):
print('txt = "Hello World"[1:3]')
txt = "Hello World"[1:3]
print(txt)

# Slice From the Start
print('txt = "Hello World"[:4]')
txt = "Hello World"[:4]
print(txt)

# Slice To the End
print('txt = "Hello World"[2:]')
txt = "Hello World"[2:]
print(txt)

# Negative Indexing
print('txt = "Hello World"[-3:-1]')
txt = "Hello World"[-3:-1]
print(txt)

txt = "0123456789ABCDEF"
print(txt)

# od -3 zprava po 2
print('txt = "0123456789ABCDEF"[-3::-2]')
txt = "0123456789ABCDEF"[-3::-2]
print(txt)
