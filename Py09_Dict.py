# -*- coding: utf-8 -*-
# % Python How To - https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# Python Dictionaries - https://www.w3schools.com/python/python_dictionaries.asp

# Python Dictionary - https://bit.ly/3MPQkWd

# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers, '\n  len(numbers)',len(numbers),'\n  type(numbers)',type(numbers))

# Accessing Elements from Dictionary
print('numbers[2]:', numbers[2])

# Add Elements to a Python Dictionary
numbers[0] = 'Zero'
print(numbers)

# Removing elements from Dictionary
del numbers[2]
print(numbers)

# Membership Test for Dictionary Keys
print('1 in numbers: ',1 in numbers) # prints True
print('2 in numbers: ',2 in numbers) # prints False

# Iterating through a Dictionary
for i in numbers:
  print(i, ':',numbers[i])

# keys()
print('numbers.keys():   ', numbers.keys(), type(numbers.keys()))
# values()
print('numbers.values(): ', numbers.values(), type(numbers.values()))
# items
print('numbers.items():  ', numbers.items(), type(numbers.items()))

# sorted()	Return a new sorted list of keys in the dictionary.
b = sorted(numbers)
print (b, type(b))
