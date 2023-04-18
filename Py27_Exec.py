#!python3
#!/usr/bin/env python3


# Using a string variable as a variable name - https://bit.ly/3nf3lfj
aa = "zz"
exec(aa + " = 'something else'")
print('aa', aa)
print('zz', zz)

# How to use string value as a variable name in Python? - https://bit.ly/3E80GLo
candy = ['a', 'b', 'c']
fruit = ['d', 'e', 'f']
snack = ['g', 'h', 'i']
name = 'fruit'
na = 'fru'
me = 'it'

# globals()  nebo pro lokalni  locals()
for e in globals()[name]:
  print('e', e)

# eval
print('eval(name):  ', eval(name), ' type:', type(eval(name)))
print('eval(na+me) :', eval(na+me), ' type:', type(eval(na+me)))
