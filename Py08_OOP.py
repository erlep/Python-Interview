# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 8 - OOP - w3s https://www.w3schools.com/python/python_classes.asp
class Person:
  ''' class Person '''
  def __init__(self, name='', age=''):
    ''' konstruktor '''
    self.name = name
    self.age = age
    self.msg = 'Person: '+"Name is " + self.name + \
        ". He is " + str(self.age) + " years old."
  def print(self):
    ''' funkce print '''
    print(self.msg)
person = Person("John", 36)
person.print()

class Student(Person):
  ''' class Student(Person) '''
  def __init__(self, name='', age='', school=''):
    # Person.__init__(self, name, age)
    super().__init__(name, age)
    self.school = school
    self.msg = 'Student: '+self.msg + " Student of " + self.school + "."
student = Student("Mike", 22, "VUT")
student.print()

class Absolvent(Student):
  ''' class Absolvent(Student) '''
  def __init__(self, name='', age='', school='', prace=''):
    # Person.__init__(self, name, age)
    super().__init__(name, age, school)
    self.prace = prace
    self.msg = 'Absolvent: '+self.msg + " Ted pracuje v " + self.prace + "."
absolvent = Absolvent("Kazbunda", 44, "VUT", 'ABB')
absolvent.print()

# Difference between type() and isinstance() - https://bit.ly/3yN3ZV7
print('isinstance(Person(), Person))  : ', isinstance(Person(), Person))  # returns True
print('type(Person()) == Person       : ', type(Person()) == Person)  # returns True
print('isinstance(Student(), Person)  : ', isinstance(Student(), Person))  # returns True
print('type(Student()) == Person      : ', type(Student()) == Person)  # returns False
print()

# Multiple Inheritance - https://bit.ly/3lQg5YX
class Parent1:
  x = 'x'
class Parent2:
  y = 'y'
class Parent3:
  z = 'z'
class Kid(Parent1, Parent2, Parent3):
  k = 'k'

k = Kid()
print('k.x:', k.x, '  k.y:', k.y, '  k.z:', k.z, '  k.k:', k.k)
print()

# dir() - vypis vlastnosti objektu
# eval() - obsah promenne jako nazev
# Using a string variable as a variable name - https://bit.ly/3nf3lfj
for d in dir(absolvent):
  # eval
  t = eval('absolvent.' + d)
  print('att:', d, '  val:', t)
print("OkDone.")
