#!/usr/bin/env python

# Slice object
numbers: list[int] = list(range(1, 11))
print(f'{numbers=}')
print(f'{numbers[::-1]=}')
text: str = 'Hello, world!'
print(f'{text=}')
print(f'{text[::-1]=}\n')

# ::-1 - slice in variable
rev: slice = slice(None, None, -1)
print(numbers[rev])
print(text[rev])
print()
