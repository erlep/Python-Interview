# -*- coding: utf-8 -*-
# Start a sample Python test without creating an account - https://blog.pyplane.com/tests

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

# Vysledek
output = what_to_buy('Laptup', "argument", store="Best Buy")
print("output: ", output)


#############################################################
# Default parametry
def fct(x, y, z, *args, a=3, b=5, **kwargs):
  return x + y + z + str(a) + str(b)

vysl = fct('a', 'b', 'c', pokus='pokus')
print('vysl:', vysl)
