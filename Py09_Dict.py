# -*- coding: utf-8 -*-
# % Python How To - https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# Python Dictionaries - https://www.w3schools.com/python/python_dictionaries.asp
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

# Python Dictionaries - https://www.w3schools.com/python/python_dictionaries.asp
# Python Dictionary Methods - https://www.w3schools.com/python/python_dictionaries_methods.asp
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print('\n dict: ', car)
print('len(car): ', len(car))
print('car["model"]', car["model"])

# keys
x = car.keys()
print('car.keys()', car.keys())
# add
car["color"] = "white"
print('after car["color"] = "white"', x)
print(x)  # after the change
# values
x = car.values()
print('car.values()', car.values())
# items
x = car.items()
print('car.items()', car.items())
# Check if Key Exists
if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Loop - items
for x in car.items():
  print(x)
# Loop - items
for x in car.keys():
  print(x, ':', car[x])

# Check if a given key already exists in a dictionary - https://is.gd/kXr8Pu
d = {"key1": 10, "key2": 23}
if "key1" in d:
  print("this will execute")

if "nonexistent key" in d:
  print("this will not")
