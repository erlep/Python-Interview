# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 7 Generators  CoreyMSchafer/code_snippets/Generators - https://is.gd/BDQHlf
#  # Fibonacci Sequence - https://en.wikipedia.org/wiki/Fibonacci_number
# a, b = 0, 1
# for i in range(21):
#   print(i, ': ', a)
#   a, b = b, a+b

#  # Fibonacci Sequence - https://en.wikipedia.org/wiki/Fibonacci_number
# Fibonacci Generator
print("Fibonacci Generator")
def fib(num):
  '''Fibonacci Generator'''
  a, b = 0, 1
  for i in range(num):
    # print( 'i:',i,' a:',a, ' b:',b )
    yield "{}: {}".format(i + 1, a)
    a, b = b, a + b
for item in fib(10):
  print(item)

# Yield - yield is a keyword that is used like return, except the function will return a generator.
# When to use yield instead of return in Python? - https://is.gd/JsKwnM
# What does the “yield” keyword do? - https://is.gd/jOvX6E

# Iterables
print("\n List")
mylist = [1, 2, 3]
for val in mylist:
  print(val)
print("\n for .. in")
print("Squares")
mylist = [x * x for x in range(4)]
for val in mylist:
  print(val)

# Generators
print("\n Generators")
mygenerator = (x * x for x in range(4))
for val in mygenerator:
  print(val)

# Yield - yield is a keyword that is used like return, except the function will return a generator.
print("\n Yield")
def createGenerator(num):
  myRange = range(num)
  for i in myRange:
    yield i * i

mygenerator = createGenerator(4)  # create a generator
print(mygenerator)  # mygenerator is an object!
for val in mygenerator:
  print(val)
