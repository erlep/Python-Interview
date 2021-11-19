# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# % CoreyMSchafer/code_snippets - https://is.gd/qP1inR
# Python Data Types - https://www.w3schools.com/python/python_datatypes.asp

# 0 Numbers
a = 5
b = 3
print('a = 5: ', a)
print('b = 3: ', b)
# deleni
c = a / b
print('c = a / b → ', c)

# celociselne deleni
c = a // b
print('c = a // b → ', c)

# zbytek
c = a % b
print('c = a % b → ', c)
# mocnina
c = a ** b
print('c = a ** b → ', c)

c = abs(-3.2)
print('c=abs(-3.2) → ', c)
c = round(3.123456, 5)
print('c=round(3.123456, 5) → ', c)
c = pow(4, 3)
print('c=pow(4, 3) → ', c)

# Format Number - print(f"
print('\n Format Number')
num1 = 10_000_000_000.123
num2 = 100_000_000.123
total = num1 + num2
print(f"{total:,}")

# PyFormat Using % and .format() for great good! - https://pyformat.info/
# Formatted Output - https://is.gd/NQH5Bu
print('\n Format number pi')
pi = 3.141592653589793
# old
print('%f' % (pi))
print('%.3f' % (pi))
# new
print('{:f}'.format(pi))
print('{:.3f}'.format(pi))

print(f"Number pi:{pi:,}")
formatted_float = "Number pi: {:.3f}".format(pi)
print(formatted_float, type(formatted_float))

print("OkDone.")

