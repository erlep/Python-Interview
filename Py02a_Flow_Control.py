# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# Python If ... Else - https://www.w3schools.com/python/python_conditions.asp

#  "python.formatting.provider": "autopep8",
#  "python.formatting.autopep8Args": ["--indent-size=2"]

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
while i <= 5:
  print(i)
  i += 1
else:
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


print("OkDone.")
