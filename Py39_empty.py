#!/usr/bin/env python

class A(object):
  def __init__(self):
    print("-> A")
    super(A, self).__init__()
    print("<- A")

class B(object):
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

print(C())
