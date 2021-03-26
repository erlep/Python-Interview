# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# Python If ... Else - https://www.w3schools.com/python/python_conditions.asp

#  "python.formatting.provider": "autopep8",
#  "python.formatting.autopep8Args": ["--indent-size=2"]

# 2a Flow Control
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

print("\t while  ====================")
i = 1
while i <= 5:
  print(i)
  i += 1
else:
  print("loop exited normally")

print("\t if  ====================")
a = 10
b = 20
if a < b:
  print("{} is less than {}.".format(a, b))
elif a == 20:
  print("{} is equal to  {}.".format(a, b))
else:
  print("{} is greater than {}.".format(a, b))

print("\t if - in 1 line if  ====================")
condition = True
x = 1 if condition else 0
print(x)

print("OkDone.")
