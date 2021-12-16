#  # Fibonacci Sequence - https://en.wikipedia.org/wiki/Fibonacci_number
# Fibonacci Generator
a, b = 0, 1
for i in range(20):
  #  print('i+1:', i+1, '  a:', a)
  print(a)
  a, b = b, a+b
