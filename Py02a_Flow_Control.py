﻿# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# Python If ... Else - https://www.w3schools.com/python/python_conditions.asp

#  "python.formatting.provider": "autopep8",
#  "python.formatting.autopep8Args": ["--indent-size=2"]
from inspect import currentframe, getframeinfo
import sys

# Flow Control
# -----------------------------------------------

# for in range()
# -----------------------------------------------
print("\t for in range() ====================")
for i in range(1, 12, 2):
  if i >= 9:
    break
  elif i == 3:
    # delej dalsi I
    continue
  elif i == 7:
    # zadny kod
    pass
  else:
    print(i)
else:
  print("loop exited normally")

# while
# -----------------------------------------------
print("\t while  ====================")
i = 1
while i <= 7:
  print(i)
  i += 1
  # fix pylint - Else clause on loop without a break statement
  if i > 5:
    break
else:  # no break
  print("loop exited normally")

# enumerate
# -----------------------------------------------
print("\t enumerate ====================")
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
  print(i, num)

# if
# -----------------------------------------------
print("\t if  ====================")
a = 10
b = 20
if a < b:
  print("{} is less than {}.".format(a, b))
elif a == 20:
  print("{} is equal to  {}.".format(a, b))
else:
  print("{} is greater than {}.".format(a, b))


# if - in 1 line if
# -----------------------------------------------
print("\t if - in 1 line if  ====================")
condition = True
x = 1 if condition else 0
print(x)

# if - value in a list
# -----------------------------------------------
print("\t if - value in a list  ====================")
L = [4, 2, 3, 1, 5, 6]
b = 5
x = b in L
print('b in a ', x)

# try - except
# -----------------------------------------------
print("\t try - except  ====================")
def divide_numhere(num1, nun2):
  try:
    result = num1 / nun2
  except TypeError:
    return "Please enter two integers or floats"
  except ZeroDivisionError:
    return "Can't divide by zero"
  return result
output = divide_numhere(5, '10')
print("try - except output: ", output)

# try - except - https://wiki.python.org/moin/HandlingExceptions
# -----------------------------------------------
print("\n\t try - except  - General ====================")
(x, y) = (5, 0)
try:
  z = x/y
except:  # catch *all* exceptions # pylint: disable=bare-except
  e = sys.exc_info()[0]
  print("Error: ", e)

# try - except - https://wiki.python.org/moin/HandlingExceptions
# -----------------------------------------------
print("\n\t try - except  - General V2====================")
(x, y) = (5, 0)
try:
  z = x/y
except ZeroDivisionError:
  print("Delis nulou.")
except Exception as ex:  # pylint: disable=broad-except
  print("The exception message is:", ex)

# match - case - New In Python 3.10 - https://bit.ly/48Sql9M
# -----------------------------------------------
print("\n\t match - case - Python => 3.10 ================")
def check_grade(grade: str) -> None:
  match grade:
    case "A":
      print("Excellent!")
    case "B":
      print("Good!")
    case "C":
      print("Average!")
    case _:
      print("Invalid grade!")
check_grade("A")  # Output: Excellent!
check_grade("B")  # Output: Good!
check_grade("D")  # Output: Invalid grade!

# filename and line number of Python script - https://bit.ly/307ZMjo
# -----------------------------------------------
print('\nfilename and line number of Python script - Before Pos')
frameinfo = getframeinfo(currentframe())  # type: ignore
print('File:', frameinfo.filename, '  Line:', frameinfo.lineno)
print('After Pos\n')

# Determine if variable is defined - https://bit.ly/3wLgbr8
# myVar = 1
if "myVar" in (locals() or globals()):
  # `myVar` exists
  # print('myVar exists. Value:', myVar)
  print('myVar exists.')
else:
  print("myVar DOESN'T exists.")
# To check if an object has an attribute:
# if hasattr(obj, 'attr_name'):
#   # obj.attr_name exists.

# assert - https://www.w3schools.com/python/ref_keyword_assert.asp
# -----------------------------------------------
print("\n\t assert =======================================")
t = "hello"
# if condition returns False, AssertionError is raised:
# assert t == "goodbye", "t should be 'hello'"
assert t == "hello", "t should be 'hello'"

print("OkDone.")
