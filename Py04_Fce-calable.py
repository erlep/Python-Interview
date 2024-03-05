#!/usr/bin/env python

# 5 Uncommon Python Features I Love https://youtu.be/sQ1Q96-Vhjk?si=olMWn2-BDlf0n7Jc

from typing import Callable

def multiply_setup(a: float) -> Callable:
  def multiply(b: float) -> float:
    return a * b
  return multiply

double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(double(5))
print(double(3))
print(double(100))
print()

print(triple(5))
print(triple(3))
print(triple(100))

print('\nOkDone.')
