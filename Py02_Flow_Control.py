# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

#  "python.formatting.provider": "autopep8",
#  "python.formatting.autopep8Args": ["--indent-size=2"]

# 2 Flow Control
print("\t for  ====================")
for i in range(1, 10, 2):
  if i >= 7:
    break
  elif i == 3:
    # zadny kod
    pass
  else:
    print(i)
else:
  print("loop exited normally")


print("\t for in  ====================")
fruits = ["apple", "banana", "cherry"]
print("fruits: ", fruits, " - type: ", type(fruits))
for x in fruits:
  print(x)

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

# Iterate With enumerate() Instead of range()
print("\t for in enumerate(,start)  ====================")
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
  if i == 54:
    continue
  print(i, num)
else:
  print("loop exited normally")

print("OkDone.")
