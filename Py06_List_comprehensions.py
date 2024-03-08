#!/usr/bin/env python

# List comprehensions
names: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']
print(f'names: {names=} ')
Long_names: list[str] = [name for name in names if len(name) > 7]
print(f'Long names: {Long_names=} ')

# without variable
print(f'Long names: {[name for name in names if len(name) > 7]} ')
