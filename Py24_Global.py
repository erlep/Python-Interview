#!/usr/bin/env python3
# Global - https://www.w3schools.com/python/python_variables_global.asp
# Alternatives to Using Globals in Python - https://bit.ly/3u9jWVC

INIT = False
def gRun():
  global INIT
  print('g: Will Run')
  if INIT:
    print('g: Already initiated')
  if not INIT:
    init()
def init():
  global INIT
  INIT = True
  print('g: Will Init')
gRun()
gRun()
print()
# OUTPUT:
# Will Run
# Will Init
# Will Run
# Already initiated

# What Should We Use Instead?
# Create class
class Init:
  def __init__(self, init_: bool):
    self.init = init_
# Create Instance of the class
init_ = Init(False)
def oRun():
  print('o: Will Run')
  if init_.init:
    print('o: Already initiated')
  if not init_.init:
    init()
def init():
  init_.init = True
  print('o: Will Init')
oRun()
oRun()
