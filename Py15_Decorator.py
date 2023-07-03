#!/usr/bin/env python

from functools import wraps

def memoize(func):
  print('Adding memoize to', func.__name__)
  cache = {}
  @wraps(func) # to propagate docstring
  def inner(*args):
    if args in cache:
      print ('to uz znam ',args ,' ' ,sep='',end='')
      return cache[args]
    result =  func(*args)
    cache[args] = result
    return result
  return inner

@memoize
def add(x, y):
  ' secte 2 cisla '
  print(f'Adding {x} + {y} = ',end='')
  return x + y

print(add(3, 4))
print(add(6, 9))
print(add(3, 4))
print(add(6, 9))
print(add(6, 9))
