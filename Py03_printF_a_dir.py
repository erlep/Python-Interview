# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

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
