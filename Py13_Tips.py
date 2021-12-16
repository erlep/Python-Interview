# -*- coding: utf-8 -*-
# Start a sample Python test without creating an account - https://blog.pyplane.com/tests

# 01:  [2, 4, 6, 8, 25]
my_numhers = [1, 2, 3, 4, 5]
my_list = [x**2 if x == 5 else x*2 for x in my_numhers]
print("01: ", my_list)

# 02:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("02: ", my_list[::-1])

# 04: >> Hello fron the otherside <<
my_string = "    Hello fron the otherside     "
stripped = my_string.strip()
print("04: >>", stripped, "<<")


# 05:  [1, 2, 3, 7, 10]
my_list = [1, 2, 3, "text", 7, 10]
filtered = list(filter(lambda x: isinstance(x, int), my_list))
print("05: ", filtered)

# 06:  Buy Laptup in Best Buy
def what_to_buy(item, *args, **kwargs):
  print("item:", item)
  print("args:", args)
  print("kwargs:", kwargs)
  if 'store' in kwargs:
    return f"Buy {item} in {kwargs['store' ]}"
  else:
    return f"Buy {item} in any store"
  return item
output = what_to_buy('Laptup', "argument", store="Best Buy")
print("06: ", output)

# 07:  False
output = all([num % 2 == 0 for num in [2, 4, 6, 8, 10, 11]])
print("07: ", output)


# 08:  Please enter two integers or floats
def divide_numhere(num1, nun2):
  try:
    result = num1 / nun2
  except TypeError:
    return "Please enter two integers or floats"
  except ZeroDivisionError:
    return "Can't divide by zero"
  return result
output = divide_numhere(5, '10')
print("08: ", output)

# 09 - What is the __str__ method in Python? -https://is.gd/gBjMZ0
class MyClass:
  x = 0
  y = ""

  def __init__(self, anyNumber, anyString):
    self.x = anyNumber
    self.y = anyString

myObject = MyClass(12345, "Hello")
print(myObject.__str__())
print(myObject.__repr__())
print(myObject)

# 10
words = ['book', 'car', 'plane', 'chair', 'floor']
'''
Desired output:
book/ car/plane/chair/floor
'''
output = '/'.join(words)
print("10: ", output)
