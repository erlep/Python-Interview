#!/usr/bin/env python

# What differences are between `format()` and `str()`? https://bit.ly/3TgnIZH

# class Person:
#   def __init__(self, name):
#     self.name = name
#   def __repr__(self):
#     return f"Person(name='{self.name}')"

# p = Person("John Smith")
# print(repr(p))  # Prints "Person(name='John Smith')"
# print(str(p))   # Prints "Person(name='John Smith')"

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __repr__(self):
#     return f'Person(name="{self.name}", age={self.age})'
#   def __str__(self):
#     return str(self.name)

# p = Person(name="John Smith", age=22)
# # This prints the str of p
# print("{!s}".format(p))  # John Smith
# # This prints the representation of p
# print("{!r}".format(p))  # Person(name="John Smith", age=22)


# The main difference between __format__ and the other two methods
# is that it also accepts a format_spec that can be used to style the returned string.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __repr__(self):
    return f'Person(name="{self.name}", age={self.age})'
  def __str__(self):
    return str(self.name)
  def __format__(self, format_spec):
    if format_spec == 'age':  # get a persons age
      return f"{self.name} is {self.age} years old"
    if format_spec == 'birthday':
      return "Yesterday"
    return str(self)  # A default case

p = Person(name="John Smith", age=22)
# This prints the str of p;               # print("{!s}".format(p))  # John Smith
print(f'str:  {p=!s}')  # John Smith
# This prints the representation of p     # print("{!r}".format(p))  # Person(name="John Smith", age=22)
print(f'repr: {p=!r}')  # Person(name="John Smith", age=22)
# print("{:age}".format(p))
print(f'{p:age}')  # John Smith is 22 years old
# print("{:birthday}".format(p))
print(f'{p:birthday}')  # Yesterday
# John Smith is 22 years old and his birthday was Yesterday
print(f"{p:age} and his birthday was {p:birthday}")
