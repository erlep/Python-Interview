#!/usr/bin/env python

# MRO (method resolution order) - https://bit.ly/4adGHLj
# Python Inheritance Explained: Complete Guide - https://ioflood.com/blog/python-inheritance/

class A:
  def __init__(self):
    print("-> A")
    super(A, self).__init__()
    print("<- A")

class B(A):
  def __init__(self):
    print("-> B")
    super(B, self).__init__()
    print("<- B")

class C(A):
  def __init__(self):
    print("-> C")
    super(C, self).__init__()
    print("<- C")

class D(B, C):
  def __init__(self):
    print("-> D")
    # Use super here, instead of explicit calls to __init__
    super(D, self).__init__()
    print("<- D")
  def bases(self):
    print("\nbases from D")
    for cls in D.__bases__:
      print(f'{cls=}  {type(cls)=}')

# print(f'{D()=}')
d = D()
d.bases()
print(f'\n{D.mro()=}')
print(f'\n{D.__mro__=}')
