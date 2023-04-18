# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# % CoreyMSchafer/code_snippets - https://is.gd/qP1inR
# 1 WhiteBoard

# Python Data Types - https://www.w3schools.com/python/python_datatypes.asp
# string
x = "Hello World"
print("x: ", x, " - type: ", type(x))
# int
x = 3
print("x: ", x, " - type: ", type(x))
# int hex
x = 0x10
print("x: ", x, " - type: ", type(x))
# string
x = '3.14'
print("x: '", x, "' - type: ", type(x))
# float
x = 3.14
print("x: ", x, " - type: ", type(x))
# list
x = ["apple", "banana", "cherry"]
print("x: ", x, " - type: ", type(x))
# tuple
x = ("apple", "banana", "cherry")
print("x: ", x, " - type: ", type(x))
# range
x = range(5)
print("x: ", x, " - type: ", type(x))
# dict
x = {"name": "John", "age": 36}
print("x: ", x, " - type: ", type(x))
# set
x = {"apple", "banana", "cherry"}
print("x: ", x, " - type: ", type(x))

# frozenset
x = frozenset({"apple", "banana", "cherry"})
print("x: ", x, " - type: ", type(x))
# 	bool
x = True
print("x: ", x, " - type: ", type(x))
# bytes
x = b"Hello"
print("x: ", x, " - type: ", type(x))
# 	bytearray
x = bytearray(5)
print("x: ", x, " - type: ", type(x))
# memoryview
x = memoryview(bytes(5))
print("x: ", x, " - type: ", type(x))

# Python 2 vs 3
#  print - print()
#  print('{} is less than {}.', format(a,b)) - print('{} is less than {}.' . format(a,b))
#  xrange (1,101) - range (1,101) a range je nyni typ mujRange: range(0, 3)  - type:  <class 'range'>
#  iteritems - items
