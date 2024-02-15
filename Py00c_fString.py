#!/usr/bin/env python

# 5 Useful F-String Tricks In Python - https://youtu.be/EoNOWVYKyo0?si=PvL2jok74kgdLAfs
# Python f-string tips & cheat sheets - https://www.pythonmorsels.com/string-formatting
# datetime podruhe https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print('\t== integer ==')
n: int = 1_000_000_000
print(f'{n}')
print(f'{n:_}')
print(f'{n:,}')

print('\t== string ==')
var: str = 'abc'
print(f'{var:20}: ')
print(f'{var: >20}: ')
print(f'{var:_>20}: ')
print(f'{var:#<20}: ')
print(f'{var:|^20}: ')

print('\t== datetime ==')
from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%d.%m.%Y %H:%M:%S}')
print(f'{now:%c}')
print(f'{now:%I%p}')

print('\t== float ==')
n: float = 1234.5678
print(round(n, 2))
print(f'Result: {n:.2f}')
print(f'Result: {n:.0f}')
print(f'Result: {n:_.3f}')

print('\t== calculation ==')
a: int = 5
b: int = 10
my_var: str = 'Bob says hi'
print(f'{a + b=}')
print(f'{bool(a)=}')
print(f'{my_var=}')
print(f'{my_var=} {type(my_var)=}')

print('\t== my float ==')
# f-strings - https://bit.ly/4arWJSn
pi: float = 3.141592653589793
print(f"Number pi:{pi:,}")
print(f"Number pi:{pi:.3f}")
# format muze byt v promenne
formatted_float: str = "Number pi: {:.3f}".format(pi)
print(formatted_float, type(formatted_float))

print('\t== my datetime ==')
today: datetime = datetime.today()
print(f"Dnes je: {today}")
print(f"Dnes je: {today:%B %d, %Y}")
print(f"Nazev souboru: soubor_{today:%Y%m%d_%H%M%S}.txt")
print()
