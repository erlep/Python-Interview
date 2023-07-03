#!/usr/bin/env python
# Abstract Base Classes for Containers - https://docs.python.org/3/library/collections.abc.html

#######################################
# yield for class
class FRange:
  def __init__(self, start,stop,step):
    self.start = start
    self.stop = stop
    self.step = step
  def __iter__(self):
    n = self.start
    while n < self.stop:
      yield n
      n += self.step


f = FRange(0, 2, 0.25)
for x in f:
  print(x, end=' ')
print()

for x in f:
  print(x, end=' ')
print()

