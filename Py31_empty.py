#!/usr/bin/env python3

a = 1
print(type(a))

a = 1.123456789101223
print(type(a))

a = 0x123
print(type(a))


a = '1.1'
print(type(a))

m = [1, 2.2, 3, 4, 5, 6, 7, 8.81234567890001]

# vsechny stejny typ
print(all((type(t) == int) or (type(t) == float) for t in m))

a = [1, 2, 3]
print(a)

b = [a]
print(b)

# Naming with Underscores in Python - https://bit.ly/3GabuKD
_ = 'promenna podtrzitko'
print('_', _)

# Using a string variable as a variable name - https://bit.ly/3nf3lfj
aa = "zzz"
exec(aa + " = 'something else'")
print(aa)

foo = "bar"
exec(foo + " = 'something else'")
print(bar)

# How to use string value as a variable name in Python? - https://bit.ly/3E80GLo
candy = ['a', 'b', 'c']
fruit = ['d', 'e', 'f']
snack = ['g', 'h', 'i']
name = 'fruit'
na = 'fru'
me = 'it'
# globals()  nebo pro lokalni  locals()
for e in globals()[name]:
  print(e)
# eval
print(eval(name))
print(eval(na+me))
