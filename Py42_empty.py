#!/usr/bin/env python

# Inheriting form two classes in python with super. can you call parent init methods with super()? - https://bit.ly/49N8EcJ

class Person():
  def __init__(self, name):
    self._name = name

  def get_name(self):
    return self._name

class Child(Person):
  def __init__(self, name, father_name, mother_name):
    super().__init__(name)
    self._father = Person(father_name)
    self._mother = Person(mother_name)

  def get_father_name(self):
    return self._father.get_name()

  def get_mother_name(self):
    return self._mother.get_name()


child = Child('Peter', 'Joseph', 'Mary')
print(child.get_name(), child.get_father_name(), child.get_mother_name())

# Prints:
# Peter Joseph Mary
