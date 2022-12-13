# -*- coding: utf-8 -*-

import itertools
print('Sequence Containers Indexing - lst[start slice:end slice:step]')
lst = [10, 20, 30, 40, 50]
print('lst:', lst)
print('lst[:-1]', lst[:-1])
# Reverse list by slicing
print('lst[::-1]', lst[::-1])
print('lst[1:3]', lst[1:3])
print('lst[:3]', lst[:3])
print('lst[1:-1]', lst[1:-1])
print('lst[::-2]', lst[::-2])
print('lst[-3:-1]', lst[-3:-1])
print('lst[3:]', lst[3:])
print('lst[::2]', lst[::2])
# shallow copy of sequence
print('lst[:]', lst[:])
# zrusi 3
print('lst:', lst)
lst[1:4] = [15, 25]
print('lst[1:4] = [15, 25] \nlst:', lst)

lst = [10, 20, 30, 40, 50]
lst2 = lst[:]
lst[1:4] = [15, 25]

print()
print('lst:', lst)
print('lst2:', lst2)

# kopie 5x za sebe
lst5 = lst*5
print('lst5:', lst5)

# spojeni za sebe
lstA = lst + lst2
print('lstA:', lstA)
# Pozice
print('lstA.index(40):', lstA.index(40))
# Vyskyt
print('lstA.count(50):', lstA.count(50))
print()

# Prohozeni promenych
a = 1
b = 2
print('a:', a)
print('b:', b)
a, b = b, a
print('a:', a)
print('b:', b)
print()

# unpacking of sequence in item and list
seq = [11, 12, 13, 14]
a, *b = seq
print('a, *b = seq:', seq)
print('a:', a)
print('b:', b)

*a, b = seq
print('*a, b = seq:', seq)
print('a:', a)
print('b:', b)

# Flatten the lists
a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(a)
print(b)  # [1, 2, 3, 4, 5, 6]

# Detecting New Elements
list1 = [14, 5, 6, 8, 11, 13]
list2 = [8, 5, 14]
new = list(set(list1) - set(list2))
print(new)  # [11, 13, 6]
print()

# slice for strings
# Python - Slicing Strings - https://www.w3schools.com/python/python_strings_slicing.asp
print('txt = "Hello World"')
txt = "Hello World"
print(txt)
print('\n How to Reverse a String in Python')
# How to Reverse a String in Python
print('txt = "Hello World"[::-1]')
txt = "Hello World"[::-1]
print(txt)
# Get the characters from position 1 to position 3 (not included):
print('txt = "Hello World"[1:3]')
txt = "Hello World"[1:3]
print(txt)
