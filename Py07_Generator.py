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
for i in mylist:
  print(i)
print("\n for .. in")
print("Squares")
mylist = [x * x for x in range(4)]
for i in mylist:
  print(i)

# Generators
print("\n Generators")
mygenerator = (x * x for x in range(4))
for i in mygenerator:
  print(i)

# Yield - yield is a keyword that is used like return, except the function will return a generator.
print("\n Yield")
def createGenerator(num):
  mylist = range(num)
  for i in mylist:
    yield i * i
mygenerator = createGenerator(4)  # create a generator
print(mygenerator)  # mygenerator is an object!
for i in mygenerator:
  print(i)
