# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# https://www.codementor.io/@sheena/essential-python-interview-questions-du107ozr6

## dir = ls -lr
import glob
import os

# ----------------------------------------------------
print('\n\t for file in glob.glob("*.py"):')
os.chdir(r'..\JobsCzScraper')
for file in glob.glob("*.py"):
  print(file)
print()
# ----------------------------------------------------
print('\n\t def print_directory_contents(sPath):')
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
  # print('sPath: ', sPath)
  for sChild in os.listdir(sPath):
    sChildPath = os.path.join(sPath, sChild)
    if os.path.isdir(sChildPath):
      print_directory_contents(sChildPath)
    else:
      print(sChildPath)
print_directory_contents(r'..\JobsCzScraper')
# ----------------------------------------------------
