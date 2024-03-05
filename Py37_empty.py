#!/usr/bin/env python

# Type Annotations
def upper_everything(elements: list[str]) -> list[str]:
  return [element.upper() for element in elements]
loud_list: list[str] = upper_everything(['Mario', 'James', 'Sandra'])
print('loud_list', loud_list)
# Type Annotations
sample: list[str | int] = ['a', 1, 'b', 2]
print('sample', sample, '\n')

# List comprehensions
names: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']
Long_names: list[str] = [name for name in names if len(name) > 7]
print(f'Long names: {Long_names} ')
# without variable
print(f'Long names: {[name for name in names if len(name) > 7]} ')

# 5 Uncommon Python Features I Love https://youtu.be/sQ1Q96-Vhjk?si=olMWn2-BDlf0n7Jc

# Slice object
numbers: list[int] = list(range(1, 11))
text: str = 'Hello, world!'
print(numbers[::-1])
print(text[::-1])
# ::-1
rev: slice = slice(None, None, -1)
print(numbers[rev])
print(text[rev])
print()

# Sets
set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}
# Combine: | → union (vertical bar char)
print('| ', set_a | set_b)
# & → intersection
print('& ', set_a & set_b)
# - ^ → difference/symmetric diff.
print('- ', set_a - set_b)
print('- ', set_b - set_a)
# pouze unikatni = doplnek do pruniku
print('^ ', set_a ^ set_b)
# < <= > >= → inclusion relations
print('<=', set_a <= set_b)
print()

# f-String for class
class Book:
  def __init__(self, title: str, pages: int) -> None:
    self.title = title
    self.pages = pages
  def __format__(self, format_spec: any) -> str:
    match format_spec:
      case 'time':
        return f'{self.pages / 60:.2f}h'
      case 'caps':
        return self. title.upper()
      case _:
        raise ValueError(f'Unknown specifier for Book()')

def main() -> None:
  hairy_potter: Book = Book('Very Hairy Potter', 300)
  python_daily: Book = Book('Python Daily', 20)
  print(f' {hairy_potter:caps}')
  print(f'Read time: {hairy_potter:time}')

  print(f' {python_daily:caps}')
  print(f'Read time: {python_daily:time}')
  print()

# def main() -> None:
#   users: dict[int, str] = {0: 'Bob', 1: 'Mario'}
#   # user: str | None = users.get(1)
#   # if user:
#   # walrus operator
#   if user := users.get(1):
#     print(f'{user} exists!')
#   else:
#     print('No user found...')

# def get_info(text_str: str) -> dict:
#   return {'words': (words := text_str.split()),
#           'word_count': len(words),
#           'character_count': len(''.join(words))}

# def main() -> None:
#   print(get_info('Bob'))
#   print(get_info('Hello, Bob'))
#   print(get_info('My name is Bob!'))

# if __name__ == "__main__":
#   main()
