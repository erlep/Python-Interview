#!python3
# Python f-strings can do more than you thought - https://youtu.be/BxUxX1Ku1EQ
# https://github.com/mCodingLLC/VideosSampleCode

import datetime
import io
import sys

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

###  f-strings ###

def simple():
  # f-Strings - https://bit.ly/3H1a7yl
  name = "Pepa " + \
      "Zdepa"
  age = 99
  print(f"Hello, {name}. You are {age}.")
  print()

def padding():
  for i in range(1, 4):
    print(f'The number is {i:03}')
  st = 'abc'
  print(f'{st:_>12}')
  print(f'{st:_<12}')
  print(f'{st:12}')
  print(f'{st:^12}')
  x12 = 'x' * 12  # 12 x
  print(f'{x12:^12}')  # zarovnani na stred na 12 znaku
  print()

def equals_debugging():
  str_value = "other 🐶"
  num_value = 123
  print(f'the value is {str_value}')
  print(f'Hodnota: {num_value=}')
  print(f'Operace: {num_value % 2=}')
  print()

def conversions():
  str_value = "other 🐶"
  print(f'prevod na str: {str_value!s}')
  print(f"prevod na 'str': {str_value!r}")
  print()

class MyClass:
  def __format__(self, format_spec) -> str:
    print(f'MyClass __format__ called with {format_spec=!r}')
    return "MyClass()"

def formatting():
  num_value = 123.456
  print(f'{num_value:.2f}')
  now = datetime.datetime.now()
  print(f'{now=:%Y-%m-%d %H:%M:%S}')
  print(f'{MyClass():blah blah %%MYFORMAT%%}')

  nested_format = ".2f"
  print(f'{num_value:{nested_format}}')
  print()

# String Formatting Comparison - https://bit.ly/3Lb7JcA
def Example():
  from string import Template
  name = "FINXTERS!"
  print('0. Hello', name)
  print('1. Hello %s' % name)
  print('2. Hello {}'.format(name))
  print(f"3. Hello {name}")
  temp = Template("4. Hello $name")
  print(temp.substitute(name=name))

  # The ** operator does something similar, but with keyword arguments
  date_info = {'year': "2020", 'month': "01", 'day': "01"}
  filename = "{year}-{month}-{day}.txt".format(**date_info)
  print('filename = "{year}-{month}-{day}.txt".format(**date_info)', filename)
  print()

  # floats to two decimal points
  print('%.2f' % 3.141592)
  print('%.2f' % 3.141592, ' a druhe cislo je %.3f ' % 1.2345678)
  print()

  # Python f-string tips & cheat sheets - https://www.pythonmorsels.com/string-formatting
  # datetime podruhe https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics
  # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
  today = datetime.datetime.today()
  print(f"Dnes je: {today}")
  print(f"Dnes je: {today:%B %d, %Y}")
  print(f"Nazev souboru: soubor_{today:%Y%m%d_%H%M%S}.txt")

def main():
  simple()
  padding()
  equals_debugging()
  conversions()
  formatting()
  Example()

if __name__ == '__main__':
  main()
