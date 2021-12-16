# Decorators

# Decorators in Python - https://www.geeksforgeeks.org/decorators-in-python/

# importing libraries
import math
import time

###############################################################################
# toto je jen uvod, dekoratory nize
###############################################################################
# Treating the functions as objects.
# Python program to illustrate functions can be treated as objects
def shout1(text):
  return text.upper()
print(shout1('Hello'))
yell = shout1
print(yell('Hi'))
print('')

# Passing the function as argument
# Python program to illustrate functions can be passed as arguments to other functions
def shout(text):
  return text.upper()
def whisper(text):
  return text.lower()
def greet(func):
  # storing the function in a variable
  greeting = func("""Hi, I am created by a function passed as an argument.""")
  print(greeting)
greet(shout)
greet(whisper)
print('')

# Returning functions from another functions.
# Python program to illustrate functions Functions can return another function
def create_adder(x):
  def adder(y):
    return x+y
  return adder
add_15 = create_adder(15)
print(add_15(10))
print('OutPut: 25 \n')

###############################################################################
# toto je jen uvod, dekoratory nize
###############################################################################
# Decorator can modify the behavior:
# defining a decorator
def hello_decorator1(func):
  # inner1 is a Wrapper function in which the argument is called
  # inner function can access the outer local functions like in this case "func"
  def inner1():
    print("Hello, this is before function execution")
    # calling the actual function now inside the wrapper function.
    func()
    print("This is after function execution")
  return inner1

# defining a function, to be called inside wrapper
def function_to_be_used():
  print("This is inside the function !!")

# passing 'function_to_be_used' inside the decorator to control its behavior
function_to_be_used = hello_decorator1(function_to_be_used)

# calling the function
function_to_be_used()


###############################################################################
# the execution time of a function using a decorator.
###############################################################################
print('\n  decorator calculate_time')
# decorator to calculate duration # taken by any function.
def calculate_time(func):
  # added arguments inside the inner1,
  # if function takes any arguments,
  # can be added like this.
  def inner1(*args, **kwargs):
    # storing time before function execution
    begin = time.time()
    func(*args, **kwargs)
    # storing time after function execution
    end = time.time()
    print("Total time taken in : ", func.__name__, end - begin)
  return inner1

# this can be added to any function present, in this case to calculate a factorial
@calculate_time
def factorial(num):
  # sleep 2 seconds because it takes very less time
  # so that you can see the actual difference
  time.sleep(2)
  print(math.factorial(num))

# calling the function.
factorial(10)

###############################################################################
# What if a function returns something or an argument is passed to the function?
###############################################################################
print('\n  decorator hello_decorator')
def hello_decorator(func):
  def inner1(*args, **kwargs):
    print("before Execution")
    # getting the returned value
    returned_value = func(*args, **kwargs)
    print("after Execution")
    # returning the value to the original frame
    return returned_value
  return inner1

# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
  print("Inside the function")
  return a + b

a, b = 1, 2
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


###############################################################################
# Chaining Decorators
###############################################################################
print('\n  Chaining Decorators')
# code for testing decorator chaining
def decor1(func):
  def inner():
    x = func()
    return x * x
  return inner
def decor2(func):
  def inner():
    x = func()
    return 2 * x
  return inner

@decor1
@decor2
def num():
  return 10

print(num())
print('OutPut: 400 \n')


