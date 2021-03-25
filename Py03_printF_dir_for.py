# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# https://www.codementor.io/@sheena/essential-python-interview-questions-du107ozr6

# 3 use Python

## dir = ls -lr
import glob
import os

os.chdir(r"..\JobsCzScraper")
for file in glob.glob("*.py"):
  print(file)

# Format Number
print('\Format Number')
num1 = 10_000_000_000.123
num2 = 100_000_000.123
total = num1 + num2
print(f"{total:,}")
print("OkDone.")

# ----------------------------------------------------
def print_directory_contents(sPath):
  """
  This function takes the name of a directory 
  and prints out the paths files within that 
  directory as well as any files contained in 
  contained directories. 

  This function is similar to os.walk. Please don't
  use os.walk in your answer. We are interested in your 
  ability to work with nested structures. 
  """
  print('sPath: ', sPath)
  for sChild in os.listdir(sPath):
    sChildPath = os.path.join(sPath, sChild)
    if os.path.isdir(sChildPath):
      print_directory_contents(sChildPath)
    # else:
    #   print(sChildPath)

# print_directory_contents(r'.\..')
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
