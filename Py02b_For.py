# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# Python For Loops - https://www.w3schools.com/python/python_for_loops.asp

#  "python.formatting.provider": "autopep8",
#  "python.formatting.autopep8Args": ["--indent-size=2"]

print("\t for in range() ====================")
for i in range(1, 12, 2):
  if i >= 9:
    break
  elif i == 3:
    # delej dalsi I
    continue
  elif i == 7:
    # zadny kod
    pass
  else:
    print(i)
else:
  print("loop exited normally")

print("\t for in  ====================")
fruits = ["apple", "banana", "cherry"]
print("fruits: ", fruits, " - type: ", type(fruits))
for x in fruits:
  print(x)

# How to loop with indexes in Python - https://is.gd/fCOXgn
print('\t use range(len(our_list)) ====================')
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
  print("President {}: {}".format(i + 1, presidents[i]))

print("\t 1 enumerate(,start) ====================")
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
  print("President {}: {}".format(num, name))

print("\t 1 enumerate - multiple ====================")
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
  ratio = ratios[i]
  print("{}% {}".format(ratio * 100, color))

print("\t 1 zip ====================")
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
  print("{}% {}".format(ratio * 100, color))

print("\t 1 line for ====================")
# ----------------------------------------------------
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]
'''
A0 = {'a':1,'b':2,...}
A1 = 0,1...,9
A2 = []
A3 = [(1, 2, 3, 4, 5)]
A4 = [(1, 2, 3, 4, 5)]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0,0],[1,1], [2,4]...,[9,81])
'''
print('A0:', A0)
print('A1:', A1)
print('A2:', A2)
print('A3:', A3)
print('A4:', A4)
print('A5:', A5)
print('A6:', A6)
# ----------------------------------------------------
print("\t format for ====================")
print('A1:', A1)
print('print( ["{0:0.2f}".format(i) for i in A1])')
print(["{0:0.2f}".format(i) for i in A1])
# --
print("\t 1 line for 2nd time ====================")
print('   i - print([ i for i in range(11)])')
print([i for i in range(11)])
print('   i + i - print([ i+i for i in range(11)])')
print([i+i for i in range(11)])
print('   i * i - print([i*i for i in range(11)])')
print([i*i for i in range(11)])
print('   [i,i+i,i*i] - print([[i,i+i,i*i] for i in range(11)])')
print([[i, i+i, i*i] for i in range(11)])
print('   {i: i*i}  - print({i: i*i for i in range(11)})')
print({i: i*i for i in range(11)})
# ----------------------------------------------------
print("\t Sum ====================")
print('Sum')
rng = range(1, 101, 1)
print('rng: ', rng)
print('print(sum(rng))')
print(sum(rng))

print("\t Sum - via for ====================")
print('Sum - via for')
suma = 0
for i in rng:
  suma = suma + i
print(suma)
# ----------------------------------------------------
print("OkDone.")
