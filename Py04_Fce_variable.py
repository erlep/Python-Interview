# Python function
# Start a sample Python test without creating an account - https://blog.pyplane.com/tests

from operator import add, sub, mul, truediv as div
import inspect
#######################################
# yield for def
def frange(start,stop,step):
  while start < stop:
    yield start
    start += step
# for frange
for x in frange(0, 2, 0.25):
  print(x, end=' ')
print()
#######################################
ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
  }
op = '-'
x =5
y = 2
r = ops[op](x, y)
print('r',r, type(r).__mro__)
print()


def inf():
  # script name - https://bit.ly/3EZT65T
  print ('i This is:', inf.__name__,
          '\n  inspect ', inspect.currentframe().f_code.co_name ,
          '\n  trace   ',inspect.stack()[1][0].f_code.co_name + '/' + inspect.stack()[2][0].f_code.co_name )

def a_fce():
  print ('a This is:', a_fce.__name__)
  inf()

def b_fce():
  print ('b This is:', b_fce.__name__)
  inf()


a_fce()
b_fce()
c = a_fce
c()
c = b_fce
c()
print()

print(c())
print(c.__call__)
