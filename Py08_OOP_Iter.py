# -*- coding: utf-8 -*-
# Python Iterators - https://bit.ly/3zTc4Za
# dual iterator in one python object - https://bit.ly/3ldKDW4
# https://www.w3schools.com/python/gloss_python_iterator_stop.asp

class InfIter:
  """Infinite iterator to return all  odd numbers"""
  def __init__(self, maxi=0):
    self.max = maxi
    self.num = 0
  def __iter__(self):
    self.num = 1
    return self
  def __next__(self):
    if self.num <= self.max:
      num = self.num
      self.num += 2
      return num
    else:
      raise StopIteration

  # Overloading __str__() to use print(InfIter):
  def __str__(self):
    return "InfIter: {0}".format(self.num)

a = iter(InfIter(20))
print(a)  # InfIter: 1
next(a)
print(a)  # InfIter: 3
print(next(a))  # 3
print(next(a))  # 5
print(next(a))  # 7

print('\n  For Loop')
for i, j in enumerate(InfIter(10)):
  print(i, ': ', j)
