# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 4 Common problems

# Delitelnost
for num in range(1, 21):
  # print (num)
  if num % 5 == 0 and num % 3 == 0:
    print(num, '- delitelne 5 a 3')
  elif num % 3 == 0:
    print(num, '- delitelne 3')
  elif num % 5 == 0:
    print(num, '- delitelne 5 ')
  else:
    print(num, '- jine num')

# Fibonacci Sequence - https://en.wikipedia.org/wiki/Fibonacci_number
a, b = 0, 1
for i in range(20):
  print(i, ': ', a)
  a, b = b, a+b
