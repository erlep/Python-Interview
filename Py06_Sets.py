#!/usr/bin/env python

# Sets
set_a: set[int] = {1, 2, 3, 4}
set_b: set[int] = {3, 4, 5, 6}
print(f'{set_a=}')
print(f'{set_b=}')
# Combine: | → union (vertical bar char)
print(f'| {set_a | set_b=}')
# & → intersection
print(f'& {set_a & set_b=}')
# - ^ → difference/symmetric diff.
print(f'- {set_a - set_b=}')
print(f'- {set_b - set_a=}')
# pouze unikatni = doplnek do pruniku
print(f'^ {set_a ^ set_b=}')
# < <= > >= → inclusion relations
print(f'<={set_a <= set_b=}')
print()

# test
