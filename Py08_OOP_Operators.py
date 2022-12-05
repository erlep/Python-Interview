# -*- coding: utf-8 -*-
# How to overload an operator in Python - https://tny.im/KYrsH

class Fruit:
  def __init__(self, weight, name="none"):
    self.name = name
    self.weight = weight

  def __add__(self, x):
    if isinstance(x, Fruit):
      return Fruit(self.weight + x.weight)
    if isinstance(x, int):
      return Fruit(self.weight + x, self.name)

  def __eq__(self, x):
    # Comparing names and not weights:
    if self.name == x.name:
      print("Both are the same fruits")
      return True
    else:
      print(self.name, "and", x.name, "are different fruits.")
      return False

  # Overloading __str__() to use print(Fruit):
  def __str__(self):
    if self.name == "none":
      return "Weight: {0}\n".format(self.weight)
    else:
      return "Name: {0}, Weight: {1}\n".format(self.name, self.weight)

  # Overloading __repr__() to use print(repr(Fruit)):
  def __repr__(self):
    if self.name == "none":
      return "repr: Weight: {0}\n".format(self.weight)
    else:
      return "repr: Name: {0}, Weight: {1}\n".format(self.name, self.weight)

  # __call__ enables to write classes where the instances behave like functions
  # __call__ in Python - https://www.geeksforgeeks.org/__call__-in-python/
  def __call__(self, a, b):
    self.weight += a + b
    return self.weight

# Fruit
a = Fruit(5, "Strawberry")
b = Fruit(100, "Watermelon")
c = Fruit(20, "Mango")
d = Fruit(1)

# Fruit operations
print('a, repr(a), typeof(a) \n', a, repr(a), type(a), '\n')
print('a, b, c, d  \n', a, b, c, d)
print('a + b + c + d ', a+b+c+d, '\n')
print('a + 5 ', a + 5, '\n')
print('a == b ', a == b, '\n')
print('d(2,3) returns 6 (1+2+3): ', d(2, 3), '\n')  # 6=1+2+3
