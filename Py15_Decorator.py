# Decorators
# Try THIS Simple Python Decorator (It's Super Useful) - https://youtu.be/4WQba4KwmRs
# Decorators in Python - https://www.geeksforgeeks.org/decorators-in-python/
import inspect

data_list = []

def register_fce(func):
  data_list.append(func)
  return func

@register_fce
def fce1():
  return ' main: ' + __name__ + '  fce: ' + inspect.currentframe().f_code.co_name + '  str: fce1'

@register_fce
def fce2():
  return ' main: ' + __name__ + '  fce: ' + inspect.currentframe().f_code.co_name + '  str: fce2'

@register_fce
def fce3():
  return ' main: ' + __name__ + '  fce: ' + inspect.currentframe().f_code.co_name + '  str: fce3'

if __name__ == "__main__":
  for i in data_list:
    print(i())
