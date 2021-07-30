# -*- coding: utf-8 -*-
# Python Iterators - https://bit.ly/3zTc4Za

class InfIter:
  """Infinite iterator to return all
      odd numbers"""

  def __iter__(self):
    self.num = 1
    return self

  def __next__(self):
    self.num += 2
    return self.num

  # Overloading __str__() to use print(InfIter):
  def __str__(self):
    return "InfIter: {0}".format(self.num)

a = iter(InfIter())
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
