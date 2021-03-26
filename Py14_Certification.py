# Artin test Python - void
# https://www.codementor.io/@sheena/essential-python-interview-questions-du107ozr6
# https://www.testdome.com/tests/python-online-test/45
# Certification ID: https://app.testdome.com/cert/47a14b40dc6d43d4b6b9db7b355411ef

# 1
'''
Implement a group_by_owners function that:
Accepts a dictionary containing the file owner
name for each file name.
Returns a dictionary containing a list of file
names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy','Code.py': 'Stan', 'Output.txt': 'Randy'} 
the group_by_owners function should return 
{'Randy':['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
'''
def group_by_owners(files):
  dct = {}
  for k in files.keys():
    nm = files[k]
    if nm in dct:
      dct[nm].append(k)
    else:
      dct[nm] = [k]
  return dct
if __name__ == "__main__":
  files = {
      'Input.txt': 'Randy',
      'Code.py': 'Stan',
      'Output.txt': 'Randy'
  }
  print(group_by_owners(files))

# 2
'''
Implement the IceCreamMachine's scoops method so
that it returns all combinations of one ingredient
and one topping. If there are no ingredients or
toppings, the method should return an empty list.
For example, 
IceCreamMachine(["vanilla", "chocolate"],["chocolate sauce"]).scoops() 
should return [['vanilla','chocolate sauce'], ['chocolate', 'chocolate sauce']].
'''
class IceCreamMachine:
  def __init__(self, ingredients, toppings):
    self.ingredients = ingredients
    self.toppings = toppings

  def scoops(self):
    vr = []
    for a in self.ingredients:
      for b in self.toppings:
        vr.append([a, b])
    return vr

if __name__ == "__main__":
  machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
  print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
