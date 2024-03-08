#!/usr/bin/env python

# Type hints cheat sheet - https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# Python Type Hints Cheat Sheet - https://uhtred.dev/insights/python-type-hints-cheat-sheet
# Python Type Hints Cheatsheet - https://www.kuniga.me/docs/python/types.html
# Typing - https://www.pythonsheets.com/notes/python-typing.html
# mypy Py01_Type_Annotation.py

# This is how we declare the type of a variable.
# It is not necessary to initialize a variable to declare its type
name: str
# Declaring the type and initializing the variable
fullname: str = 'Uhtred Miller'

# basic types
s_var: str = 'string'
i_var: int = 7
f_var: float = 0.5
b_var: bytes = b'string'
boole: bool = True

# for fixed-length tuples
t_var1: tuple[int, str, float] = (8, 'string', 5.6)
# for tuples of varying size
t_var2: tuple[int, ...] = (3, 4, 5)  # t_var3: tuple[int] = (3, 4, 5) - nefunguje

# Type Annotations
sample: list[str | int] = ['a', 1, 'b', 2]
print('sample', sample, '\n')

# for collections
l_lst: list[str] = ['a', 'b', 'c']
s_set: set[int] = {1, 2, 3}

# for dictionaries, the first index is the type
# of the key and the second is the type of the value
d_var: dict[str, int] = {'age': 25, 'year': 2023}

# Union and optional
# for union of types, when a variable
# can be one of several types.
o_var1: None | str = 'string'
o_var2: str | int | float = 45
# very useful for sequences with values of varying types
o_var3: list[str | int] = [4, 5, 'a', 4, 'b']

# Optional, from the typing module for values that could be None
from typing import Optional
v_opt: Optional[str] = 'hello, world!' if boole else None
if v_opt is not None:
  # the type checker will know v is not None
  print('not None ', v_opt.upper())
# on the other hand, if you know that the value of v never
# will be None by some logic that the type checker
# doesn't understand, you can use the assert to inform the type checker
assert v_opt is not None
print(v_opt.title())

pseudo_int: int = 'a'  # type: ignore

# funkce inc
def inc(value: int, amount: int = 1) -> int:
  'vrati soucet value a amout'
  return value + amount
print(f'Soucet: {inc(2, 3)=}')

# Type Annotations
def upper_everything(elements: list[str]) -> list[str]:
  return [element.upper() for element in elements]
loud_list: list[str] = upper_everything(['Mario', 'James', 'Sandra'])
print('loud_list', loud_list)
