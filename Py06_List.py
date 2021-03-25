# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# Python 3 Cheat Sheet https://perso.limsi.fr/pointal/python:memento

# 6 List how to use

# my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = list(range(1, 12))
print("my_list: ", my_list, " - type: ", type(my_list))

# Give me each number in the list squared
squares = [num * num for num in my_list]
print("squares: ", squares, " - type: ", type(squares))

# Algo: limit values greater than 15, memorizing of lost values.
lst = [11, 18, 9, 12, 23, 4, 17]
print('souce:', lst)
lost = []
for idx in range(len(lst)):
  val = lst[idx]
  if val > 15:
    lost.append(val)
    lst[idx] = 15

print("modif:", lst, "-lost(>15):", lost)
