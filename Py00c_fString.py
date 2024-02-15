#!/usr/bin/env python

# 5 Useful F-String Tricks In Python - https://youtu.be/EoNOWVYKyo0?si=PvL2jok74kgdLAfs
# Python f-string tips & cheat sheets - https://www.pythonmorsels.com/string-formatting
# datetime podruhe https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

from datetime import datetime

print('\t=== integer ===')
i: int = 1_000_000_000
print(f'{i}')
print(f'{i:_}')
print(f'{i:,}')

print('\t=== float ===')  # f-strings float - https://bit.ly/4arWJSn
f: float = 1234.5678
print(round(f, 3))
print(f'Result: {f:.0f}')
print(f'Result: {f:.3f}')
print(f'Result: {f:_.3f}')

print('\t=== f-string in variable ===')  # format muze byt v promenne
formatted_float: str = "Number pi: {:.2f}".format(f)
print(formatted_float)
print(f'{formatted_float=} {type(formatted_float)=}')

print('\t=== string ===')
var: str = 'abc'
print(f'{var:20}: ')
print(f'{var: >20}: ')
print(f'{var:_>20}: ')
print(f'{var:#<20}: ')
print(f'{var:|^20}: ')

print('\t=== evaluation ===')
a: int = 5
b: int = 10
my_var: str = 'Bob says hi'
print(f'{a + b=}')
print(f'{bool(a)=}')
print(f'{my_var=}')
print(f'{my_var=} {type(my_var)=}')

print('\t=== datetime ===')
now: datetime = datetime.now()
print(f'Now: {now}')
print(f'Now: {now:%d.%m.%Y %H:%M:%S}')
print(f'Now: {now:%c}')
print(f'Now: {now:%I%p} - imperial')
print(f"Now: {now:%B %d, %Y}")
print(f"Nazev souboru: soubor_{now:%Y%m%d_%H%M%S}.txt")
print()
