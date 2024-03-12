#!/usr/bin/env python

# Python Inheritance Explained: Complete Guide - https://ioflood.com/blog/python-inheritance/

class Father:
  def skills(self):
    print('Programming and Cooking')

class Mother:
  def skills(self):
    print('Art and Teaching')

class Child(Father, Mother):
  pass

# Creating an instance of the Child class
child = Child()
child.skills()

# Output:
# 'Programming and Cooking'
