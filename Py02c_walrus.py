#!/usr/bin/env python
# 5 Uncommon Python Features I Love https://youtu.be/sQ1Q96-Vhjk?si=olMWn2-BDlf0n7Jc

# Walrus Operator (:=) = mrož - prirazeni hodboty a prace s hodnotou v jednom kroku

def f(x):  # a function that performs some complex math
  return x - 1
# without walrus - f(x) is called 2 times
results = [f(x) for x in range(10) if f(x) > 3]
print(f'{results=}')
# with walrus - f(x) is called only 1 times
results_walrus = [result for x in range(10) if (result := f(x)) > 3]
print(f'{results_walrus=}')
print(f'{(result := f(2))=}')  # prirazeni hodboty a prace s hodnotou v jednom kroku
print(f'{result=}')

users: dict[int, str] = {0: 'Bob', 1: 'Mario'}
# without walrus operator 2 lines needed
#    user: str | None = users.get(1)
#    if user:
# walrus operator - all in 1 line
if user := users.get(3):  # 0 or 1 exists, the others NOT
  print(f'{user} exists!')
else:
  print('No user found...')

# function returns dict via walrus
def get_info(text_str: str) -> dict:
  return {'words': (words := text_str.split()),
          'word_count': len(words),
          'character_count': len(''.join(words))}
# use get_info
print(get_info('Bob'))
print(get_info('Hello, Bob'))
print(get_info('My name is Bob!'))
