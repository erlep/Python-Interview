# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 8 - OOP - w3s https://www.w3schools.com/python/python_classes.asp
class Person:
  ''' class Person '''
  def __init__(self, name='', age=''):
    ''' konstruktor '''
    self.name = name
    self.age = age
    self.msg = "Name is " + self.name + \
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
    self.msg = self.msg + " Student of " + self.school + "."
student = Student("Mike", 22, "VUT")
student.print()


class Absolvent(Student):
  ''' class Absolvent(Student) '''
  def __init__(self, name='', age='', school='', prace=''):
    # Person.__init__(self, name, age)
    super().__init__(name, age, school)
    self.prace = prace
    self.msg = self.msg + " Ted pracuje v " + self.prace + "."
absolvent = Absolvent("Kazbunda", 44, "VUT", 'ABB')
absolvent.print()

# Difference between type() and isinstance() - https://bit.ly/3yN3ZV7
print('isinstance(Person(), Person))  : ', isinstance(Person(), Person))  # returns True
print('type(Person()) == Person       : ', type(Person()) == Person)  # returns True
print('isinstance(Student(), Person)  : ', isinstance(Student(), Person))  # returns True
print('type(Student()) == Person      : ', type(Student()) == Person)  # returns False

print("OkDone.")
