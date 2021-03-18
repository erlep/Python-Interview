# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 8 - OOP - w3s https://www.w3schools.com/python/python_classes.asp
class Person:
  ''' class Person '''
  def __init__(self, name, age):
    ''' konstruktor '''
    self.name = name
    self.age = age
    self.msg = "Name is " + self.name + \
        ". He is " + str(self.age) + " years old."
  def print(self):
    ''' funkce print '''
    print(self.msg)
p1 = Person("John", 36)
p1.print()

class Student(Person):
  ''' class Student(Person) '''
  def __init__(self, name, age, school):
    # Person.__init__(self, name, age)
    super().__init__(name, age)
    self.school = school
    self.msg = self.msg + " Student of " + self.school + "."
p2 = Student("Mike", 22, "VUT")
p2.print()

print("OkDone.")
