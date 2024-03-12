# __init__, __enter__, __exit__ of object in Python

# Souběžné a paralelně běžící úlohy naprogramované v Pythonu – knihovna Trio - https://bit.ly/3kXZVNi
# https://github.com/tisnik/most-popular-python-libs

class Context():
  def __init__(self):
    print("Context: init")

  def __enter__(self):
    print("Context: enter")
    return "foo"

  def __exit__(self, exit_type, value, traceback):
    print("Context: exit", exit_type, value, traceback)


print("Before with block")

with Context() as c:
  print("Inside with block")
  print(c)

print("After with block")
