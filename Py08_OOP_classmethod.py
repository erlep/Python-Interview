#!/usr/bin/env python

# Calling super() inside a class' classmethod to get at the metaclass method - https://bit.ly/43cZCn6

class A:
  @classmethod
  def f(cls):
    return 1
class B(A):
  pass
class C(A):
  @classmethod
  def f(cls):
    return 2
class D(B, C):
  @classmethod
  def f(cls):
    return super().f() + 1

print(f'{A.f()=}')
print(f'{B.f()=}')
print(f'{C.f()=}')
print(f'{D.f()=}')
