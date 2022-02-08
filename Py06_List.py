# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# Python 3 Cheat Sheet https://perso.limsi.fr/pointal/python:memento

# List how to use
# --------------------

# prirozena cisla  1,2 az 11
my_list = list(range(1, 12))
print("my_list: ", my_list, " - type: ", type(my_list))
# Give me each number in the list squared
squares = [num ** 2 for num in my_list if num % 2]
print("mocniny lichych: ", squares, " - type: ", type(squares))
# Posun o +-1 suda / licha
oJednu = [x + 1 if x % 2 else x-1 for x in my_list]
print("oJednu: ", oJednu, " - type: ", type(oJednu))
# Jsou vsechny cisla suda
suda = all([num % 2 == 0 for num in oJednu])
print("Jsou vsechny cisla oJednu suda: ", suda)
# Je nejake cislo sude
suda = any([num % 2 == 0 for num in oJednu])
print("Je nejake cislo sude oJednu suda: ", suda)


# Vrat jen cisla
# -------------------------------------------------------
my_list = [1, 2, 3, "text", 7, 10]
# lepsi nez filter je radek niz
# filtered = list(filter(lambda x: isinstance(x, int), my_list))
filtered = [x for x in my_list if isinstance(x, int)]
print("\nmy_list:     ", my_list)
print("jen typ int - filtered: ", filtered)
# unpacking of sequence in item and list
a, *b = filtered
print('a, *b = filtered:', filtered)
print('a:', a)
print('b:', b)
*a, b = filtered
print('*a, b = filtered:', filtered)
print('a:', a)
print('b:', b)

# Projde list co je >15, da do seznamu a nahradi cislem 15
# Algo: limit values greater than 15, memorizing of lost values.
lst = [11, 18, 9, 12, 23, 4, 17]
print('source:', lst)
lost = []
for idx, val in enumerate(lst):
  if val > 15:
    lost.append(val)
    lst[idx] = 15
# Vysledek
print("modif: ", lst, "-lost(>15):", lost)


# Najde v listu nejmensi schazejici cele cislo < 100 000
# -------------------------------------------------------
def NajdiN(aList):
  print('A: ', aList)

  # prebrani jen cisel 1 az 1e5
  AA = [num for num in aList if num > 0 and num <= 100_000]
  print('AA: ', AA)

  # Deduplikace - List na Set
  AA = set(AA)
  print('AA: ', AA)

  # smycka pres 0-N, kdyz je nejake vynechane je to vysledek
  for i in range(1, len(AA)+2):
    # obsahuje i
    if (i not in AA):
      return (i)


# Vrati chybejici cisla v rade realnych cisel po to nejvetsi z listu
# -------------------------------------------------------
def SeznamN(aList):
  print('A: ', aList)

  # prebrani jen cisel 1 az 1e5
  AA = [num for num in aList if num > 0 and num <= 100_000]
  print('AA: ', AA)

  # kdyz je AA prazdne
  if len(AA) == 0:
    return (1)

  # List na Set - deduplikace
  AA = set(AA)
  print('AA: ', AA)

  # nej cislo - tj. posledni
  maxN = list(AA)[-1]
  print('maxN: ', maxN)

  # seznam
  seznam = range(1, maxN)

  # seznam cisel co chyby
  ret = [n for n in seznam if n not in AA]

  # vrati list
  return (ret)

A = []
A = [1]
A = [1, 2, 3]
A = [-2, 0, -3]
A = [-4, 1, 3, 6, 4, 1, 2, 2000000, -5, -8, 2123456]
A = [-4, -5, -8, 2123456, 1, 4, 2, 3, 6, 8, 4, 4, 8, 8]
A = [2, 2, 6, 5, 3, 0, 2, 11, 0, 2, -4, -5, -8, 1, 8, -9, -4, -7, -1, -8]

print('\n  NajdiN a SeznamN')
print('NajdiN:', NajdiN(A))
print('SeznamN:', SeznamN(A))

print('\n  vyhod nejmensi integer (pro stejne cisla to prvni)')
def remove_smallest(arr):
  # prvni hodnota
  minValue = arr[0]
  # najdi min hodnotu
  for num in arr:
    if num < minValue:
      minValue = num
  # shallow copy
  newArr = arr[:]
  # smaz min hodnotu
  newArr.remove(minValue)
  print(arr, ' => ', newArr)
  return newArr

a = remove_smallest([5, 3, 2, 1, 4])
a = remove_smallest([1, 2, 3, 4, 5, 1])
a = remove_smallest([2, 2, 1, 2, 1])
a = remove_smallest([2])
