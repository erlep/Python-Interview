#!/usr/bin/env python

# MRO (method resolution order) - https://bit.ly/4adGHLj
# Python Inheritance Explained: Complete Guide - https://ioflood.com/blog/python-inheritance/

class A:
  def __init__(self):
    print("-> A")
    super(A, self).__init__()
    print("<- A")

class B:
  def __init__(self):
    print("-> B")
    super(B, self).__init__()
    print("<- B")

class C(A, B):
  def __init__(self):
    print("-> C")
    # Use super here, instead of explicit calls to __init__
    super(C, self).__init__()
    print("<- C")
  def bases(self):
    print("\nbases from C")
    for cls in C.__bases__:
      print(f'{cls=}  {type(cls)=}')

print(f'{C()=}')
c = C()
c.bases()
print(f'\n{C.mro()=}')
print(f'\n{C.__mro__=}')
