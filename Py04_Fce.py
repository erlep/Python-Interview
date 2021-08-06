# -*- coding: utf-8 -*-
# Start a sample Python test without creating an account - https://blog.pyplane.com/tests

# funkce c
def c(a, b=None):
  if b is None:
    return 'jenom a: ' + str(a)
  else:
    return 'a: ' + str(a) + ' je tam take b: ' + str(b)
# Vysledek
print('c(1)', c(1))
print('c(1, 2)', c(1, 2))
print()

# 06:  Buy Laptup in Best Buy
def what_to_buy(item, *args, **kwargs):
  print("item:", item)
  print("args:", args)
  print("kwargs:", kwargs)
  if 'store' in kwargs:
    return f"Buy {item} in {kwargs['store']}"
  else:
    return f"Buy {item} in any store"
  return item

# Vysledek
output = what_to_buy('Laptup', "argument", store="Best Buy")
print("output: ", output)
print()

#############################################################
# Default parametry, volitelne parametry
def fct(x, y, z, *args, a=3, b=5, c='', **kwargs):

  if 'P' in args:
    return 'Je tam P. Parametr pokus: ' + str(kwargs['pokus']) + '  ' + x + y + z + c + str(a) + c + str(b)
  elif 'pokus' in kwargs:
    return 'Parametr pokus: ' + str(kwargs['pokus']) + '  ' + x + y + z + c + str(a) + c + str(b)
  else:
    return x + y + z + c + str(a) + c + str(b)

vysl = fct('x', 'y', 'z', 'P', pokus='MujPokus', b=22, a=11, c='-')
print('vysl:', vysl)
