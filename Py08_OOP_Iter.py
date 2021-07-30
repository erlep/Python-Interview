# -*- coding: utf-8 -*-
# Python Iterators - https://bit.ly/3zTc4Za

class InfIter:
  """Infinite iterator to return all
      odd numbers"""

  def __init__(self, max=0):
    self.max = max

  def __iter__(self):
    self.num = 1
    return self

  def __next__(self):
    if self.num <= self.max:
      self.num += 2
      return self.num
    else:
      raise StopIteration

  # Overloading __str__() to use print(InfIter):
  def __str__(self):
    return "InfIter: {0}".format(self.num)

a = iter(InfIter(20))
print(a)
next(a)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print('\n  For Loop')
for i in a:
  print(i)
