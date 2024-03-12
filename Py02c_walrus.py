#!/usr/bin/env python
# 5 Uncommon Python Features I Love https://youtu.be/sQ1Q96-Vhjk?si=olMWn2-BDlf0n7Jc

# walrus operator = mrož
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

