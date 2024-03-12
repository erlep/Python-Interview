#!/usr/bin/env python

# How to instantiate a class given its parent class in Python? - https://bit.ly/3v7qqbF

class MetaAnimal(type):
  classes: dict = {}
  print(f'{classes=} ')

  def __new__(mcs, name, bases, dct):
    result = super().__new__(mcs, name, bases, dct)
    mcs.classes[name.lower()] = result
    # print(f'⚡{MetaAnimal.classes=} \n{type(MetaAnimal.classes)=}')
    return result

  @classmethod
  def get_animal(mcs, name):
    return mcs.classes.get(name)


class Animal(metaclass=MetaAnimal):
  def communicate(self):
    pass


class Dog(Animal):
  def communicate(self):
    self.bark()

  def bark(self):
    print('Woof')


class Cat(Animal):
  def communicate(self):
    self.meow()

  def meow(self):
    print('Meow')


MetaAnimal.get_animal('cat')().communicate()
MetaAnimal.get_animal('dog')().communicate()
