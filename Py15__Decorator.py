# Most Used Python Decorators - https://bit.ly/3XCKDjr
# 10 Fabulous Python Decorators - https://bit.ly/3NE30jm
# Decorators in Python - https://bit.ly/3rc8ieq

# @staticmethod: This decorator is used to define a static method in a class. It does not require an instance of the class to be called and can be accessed using the class name.
# @classmethod: This decorator is used to define a class method in a class. It takes the class itself as the first argument instead of an instance of the class.
# @property: This decorator is used to define a getter method for a class attribute. It allows you to access the attribute as if it were a regular attribute, but in reality it executes the getter method.
# @abstractmethod: This decorator is used to define an abstract method in an abstract base class. It is used to enforce a specific behavior in the derived classes.
# @wraps: This decorator is used to wrap a function or method and preserve its metadata such as its name, docstring and signature.
# @lru_cache: This decorator is used to cache the result of a function call with a limited size cache. It can significantly improve the performance of functions that are called frequently with the same arguments.

# ==============================================================================
# calculate function execution time
import functools
import time

def timer(func):
  'Time Measure Decorator'
  # Decorators should copy metadata to the new function
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    value = func(*args, **kwargs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
    return value
  return wrapper

@timer
def doubled_and_add(num):
  res = sum([i*2 for i in range(num)])
  print("Result : {}".format(res))

doubled_and_add(100000)
doubled_and_add(1000000)
doubled_and_add(10000000)
print()

# ==============================================================================
# pocitani volani funkce - Stateful Decorators
def count_calls(func):
  'Count Calls Decorator. Number of calls in <fce>.num_calls '
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    wrapper.num_calls += 1  # type: ignore
    print(f"Call {wrapper.num_calls} of {func.__name__!r}")  # type: ignore
    return func(*args, **kwargs)
  wrapper.num_calls = 0  # type: ignore
  return wrapper

@count_calls
def say():
  print("Hello!")

say()
say()
say()
say()
print('Pocet volani say()', say.num_calls)
