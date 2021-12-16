# -*- coding: utf-8 -*-
# Start a sample Python test without creating an account - https://blog.pyplane.com/tests

# Funkce se 2 paramery, b - nepovinne
def Fce(a, b=None):
  if b is None:
    return 'Fce: jenom a: ' + str(a)
  else:
    return 'Fce: a: ' + str(a) + ' je tam take b: ' + str(b)
# Vysledek
print('Fce(1):    ', Fce(1))
print('Fce(1, 2): ', Fce(1, 2))
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
def Fnc(a, b, c, d=4, e=5, f=6, *args, **kwargs):
  print("a:", a, "  b:", b, "  c:", c, "  d:", d, "  e:", e, "  f:", f,)
  print("args:", args)
  print("kwargs:", kwargs)
  return 'OkDone.'
print('def Fnc(a, b, c, d=4, e=5, f=6, *args, **kwargs):')
vysl = Fnc(1, 2, 3, 0, -1, -2, -3, -4, pokus='MujPokus', g=22, h=11, i='icko')
print("Fnc:(vysl = Fnc(1,2,3,0,-1,-2,-3,-4, pokus='MujPokus', g=22, h=11, i='icko')):", vysl)
print()
print('def Fnc(a, b, c, d=4, e=5, f=6, *args, **kwargs):')
vysl = Fnc(1, 2, 3, e=88, g=22, h=11)
print("Fnc:(vysl = Fnc(1,2,3,e=88, g=22, h=11))):", vysl)
print()

#############################################################
# -> syntax - Annotation for type of return value of function - https://bit.ly/3hWwKZF
# Function definitions - https://bit.ly/3hZyiCp
def float2int(x: float) -> int:
  return int(x)
# Pouziti funkce
i = float2int(3.14)
print('float2int(3.14):', i, '  type(i)', type(i))
# promenna typu funkce
MyFce = float2int
print('MyFce(3.14):', MyFce(3.14))
