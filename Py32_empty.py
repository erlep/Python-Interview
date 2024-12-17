#!/usr/bin/env python
# Setting Up VSCode For Python: A Complete Guide - https://www.datacamp.com/tutorial/setting-up-vscode-python
# VSCode Python: Add Parameter Names
def my_function(param1, param2, param3):
  pass


a = 1
b = 2
c = 3
# Když začneš psát volání funkce, IntelliSense ti nabídne parametry
# my_function(param1=, param2=, param3=)

my_function(param1=a, param2=b, param3=c)

my_function(a, b, c)
