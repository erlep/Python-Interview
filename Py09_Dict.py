# -*- coding: utf-8 -*-
# % Python How To - https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# Python Dictionaries - https://www.w3schools.com/python/python_dictionaries.asp
print(' How to Remove Duplicates From a Python List')

# How to Remove Duplicates From a Python List
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# Create a Function - How to Remove Duplicates From a Python List
def my_function(MyList):
  return list(dict.fromkeys(MyList))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist, '\n')

# Python Dictionaries - https://www.w3schools.com/python/python_dictionaries.asp
# Python Dictionary Methods - https://www.w3schools.com/python/python_dictionaries_methods.asp
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print('dict car: ', car)
print('len(car): ', len(car))
print('car["model"]', car["model"])

# keys
x = car.keys()
print('car.keys()', car.keys())
# add
car["color"] = "white"
print('car["color"] = "white" => after "year" new value "color" ', x)
print(x)  # after the change
# values
x = car.values()
print('car.values() ', car.values())
# items
x = car.items()
print('car.items() ', car.items())
# Check if Key Exists
if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Loop - items
print('\t for x in car.items():')
for x in car.items():
  print(x)
# Loop - items
print('\n\t for x in car.keys():')
for x in car.keys():
  print(x, ':', car[x])

# Check if a given key already exists in a dictionary - https://is.gd/kXr8Pu
d = {"key1": 10, "key2": 23}
if "key1" in d:
  print("this will execute")

if "nonexistent key" in d:
  print("this will not")

# Pristup k dict
print('d["key1"]:', d["key1"])

# Hodnoty dict: prevod na str, spojeni do retezce
values = ' '.join(str(v) for v in d.values())
print(values, type(values))
