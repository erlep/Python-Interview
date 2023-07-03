#!/usr/bin/env python

# Porovnání vůči nule
a = 1
if a != 0:
  print('a neni 0  hodnota a:', a)
else:
  print('a je 0    hodnota a:', a)

if a:
  print('a neni 0  hodnota a:', a)
else:
  print('a je 0    hodnota a:', a)

if not (a):
  print('a je 0    hodnota a:', a)
else:
  print('a neni 0  hodnota a:', a)

# Dělitelnost: % remainder
if a % 2:
  print('a je liche  hodnota a:', a)
else:
  print('a je sude   hodnota a:', a)
# % - ÷ remainder
if not (a % 2):
  print('a je sude   hodnota a:', a)
else:
  print('a je liche  hodnota a:', a)

# Empty list
myList = []
if myList:
  print('myList neni prazdny. Delka:', len(myList))
else:
  print('myList JE prazdny. Delka:', len(myList))

myList.append('x')
if myList:
  print('myList neni prazdny. Delka:', len(myList))
else:
  print('myList JE prazdny. Delka:', len(myList))
