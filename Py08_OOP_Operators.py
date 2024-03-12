# -*- coding: utf-8 -*-
# How to overload an operator in Python - https://tny.im/KYrsH
# How do I type hint a method with the type of the enclosing class? - https://bit.ly/48NXdQR

class Fruit(object):
  def __init__(self, weight: int, name: str = "none") -> None:
    self.name = name
    self.weight = weight
  def __add__(self, x: 'Fruit | int') -> 'Fruit':
    '+ method'
    if isinstance(x, Fruit):
      return Fruit(self.weight + x.weight)
    if isinstance(x, int):
      return Fruit(self.weight + x, self.name)
    return Fruit(0)
  def __eq__(self, other: object) -> bool:
    '== method'
    # Comparing names and not weights:
    if not isinstance(other, Fruit):
      return NotImplemented
    if self.name == other.name:
      print("Both are the same fruits.")
      return True
    # else
    print(self.name, "and", other.name, "are different fruits.")
    return False
  # Overloading __str__() to use print(Fruit):
  # __str__ goal is to be readable
  def __str__(self) -> str:
    'str() method'
    if self.name == "none":
      return "str:  Weight: {0}".format(self.weight)
    # else:
    return "str:  Name: {0}, Weight: {1}".format(self.name, self.weight)

  # Overloading __repr__() to use print(repr(Fruit)):
  # __repr__ goal is to be unambiguous
  def __repr__(self) -> str:
    'repr() method'
    if self.name == "none":
      return "repr: Weight: {0}".format(self.weight)
    else:
      return "repr: Name: {0}, Weight: {1}".format(self.name, self.weight)

  # Overloading __format__() to use print(f'{a:name}')
  # __format__ goal is to accepts a format_spec that can be used to style the returned string - https://bit.ly/3TgnIZH
  def __format__(self, format_spec: str) -> str:
    'format() method'
    if format_spec == 'name':
      return f"frmt: Fruit name: {self.name}"
    if format_spec == 'weight':
      return f"frmt: Fruit weight: {self.weight}"
    return str(self)  # A default case

  # __call__ in Python - https://www.geeksforgeeks.org/__call__-in-python/
  def __call__(self, weight_1: int, weight_2: int) -> int:
    '__call__ enables to write classes where the instances behave like functions'
    self.weight += weight_1 + weight_2
    return self.weight

# Fruit
a = Fruit(5, "Strawberry")
b = Fruit(100, "Watermelon")
c = Fruit(20, "Mango")
d = Fruit(1)
# Fruit operations
print('⚡a, repr(a), typeof(a) \n', a, repr(a), type(a))
print('⚡a, b, c, d  \n', a, b, c, d)
print('⚡a + b + c + d ', a + b + c + d)
print('⚡a + 5 ', a + 5)
print('⚡a == b ', a == b)
print('⚡d(2,3) returns 6 (1+2+3): ', d(2, 3))  # 6=1+2+3
# __format__ class f-string formats
print('\n__format__ class f-string formats:')
# This prints the str of a;
print(f'⚡str:  {a=!s}')
# This prints the representation of a
print(f'⚡repr: {a=!r}')
# print("{:name}".format(a))
print(f'⚡{a:name}')
# print("{:weight}".format(a))
print(f'⚡{a:weight}')
# John Smith is 22 years old and his birthday was Yesterday
print(f"⚡{a:name} has weight {a:weight}")
