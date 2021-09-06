#!/usr/bin/env python3
#########################################
#  Calculates Matrix multiplication.
#########################################
# “how to take matrix input in python” Code Answer’s - https://bit.ly/3lnhMOT
# testpy https://bit.ly/3jhgS49
# Python Program to Multiply Two Matrices - https://bit.ly/3A3DJqj
# Python Iterators - https://bit.ly/3zTc4Za
# dual iterator in one python object - https://bit.ly/3ldKDW4
# Python __eq__ - https://bit.ly/3lrWGPL
'''
Description
-----------
    Matrix A
width: 2
height: 3
    Matrix B
width: 1
height: 2
    Matrix A values:
1 2
5 3
6 7
    Matrix B values:
5
1
    Result:
7
28
37
'''
# Matrix class
class Matrix(object):
  # constructor - name, matrix (list of lists)
  def __init__(self, name, mx=None):
    self.name = ''
    self.width, self.height = 0, 0
    self.mx_rows = []
    if mx is None:
      # rucni zadani
      self.name = name
      self.width, self.height = self.wh()
    # Lepsi je pouzit isinstance misto type()
    # elif type(mx) == Matrix:
    elif isinstance(mx, Matrix):
      # mx je Matrix
      self.name = name
      self.mx_rows = mx.mx_rows
    else:
      # mx je list
      self.name = name
      self.mx_rows = mx
    # Check
    if not(self.check()):
      s = '!!! Wrong Matrix! !!!'
      self.name = s
      print(s)
      raise ValueError(s)

  # definice pro '=='
  def __eq__(self, other):
    if isinstance(other, Matrix):
      # Matrix
      return self.mx_rows == other.mx_rows
    elif isinstance(other, list):
      # list
      return self.mx_rows == other
    return False

  # Radky
  def rows(self):
    return self.mx_rows
  # Sloupce
  def columns(self):
    return zip(*self.mx_rows)
  # Iterator - dual iterator in one python object - https://bit.ly/3ldKDW4
  def iter_rows(self):
    for row in self.rows():
      yield row
  # Iterator
  def iter_columns(self):
    for column in self.columns():
      yield column
  # Iterace pres radky
  __iter__ = iter_rows

  # Matrix check
  def check(self):
    # matice [] kontola: Je OK?
    if self.mx_rows == []:
      return True
    # Nastaveni w,h
    self.height = len(self.mx_rows)
    try:
      self.width = len(self.mx_rows[0])
    except:
      # sirka matice = 0, pripad  [1, 2, 3]
      self.mx_rows = [self.mx_rows]
      self.height = len(self.mx_rows)
      self.width = len(self.mx_rows[0])

    # Kontrola na stejny pocet radku a sloupcu
    for i in self.rows():
      # vsechny prvky matice stejny typ: int OR float
      if not(all((type(t) == int) or (type(t) == float) for t in i)):
        return False
      # kontrola: width
      if len(i) != self.width:
        self.width = -1
        return False
    # kontrola: height
    for i in self.columns():
      if len(i) != self.height:
        self.height = -1
        return False
    return True

  # * - multiplication = Matrix multiplication
  def __mul__(self, x):
    ''' Function: Matrix Multiplication
        Parameter: name - Matrixes A, B
        Return: A x B
    '''
    A = (self)
    B = (x)
    if (A.width != B.height):
      s = '!!! Wrong Matrixes width != height !!!   A.w:' + str(A.width) + ' != B.h:' + str(B.height)
      print(s)
      # return Matrix(s, [])
      raise ValueError(s)
    # Nasobeni
    s = '__mul__'
    try:
      C = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    except:
      s = 'Matrix Multiplication Calculation error!'
      C = []
      raise ValueError(s)
    C = Matrix(s, C)
    return C

  # Overloading __str__() to use print(Matrix):
  def __str__(self):
    if self.name == "none":
      st = "Matrix width: {0}".format(self.width)
    else:
      st = "Matrix Name: {0}, width: {1}, height: {2}".format(self.name, self.width, self.height)
    for i in self.mx_rows:
      st += '\n' + str(i)
    st += '\n'
    return st

  # Enter Value
  def value(self, Hlaska):
    try:
      val = int(input(Hlaska))
    except:
      s = 'Wrong value enter error!'
      exit("Moje Error message")
      raise ValueError(s)
    return val

  # Matrix input Width & Heighs
  def wh(self):
    print('Matrix ', self.name)
    self.width = self.value('width: ')
    self.height = self.value('height: ')
    print()
    return self.width, self.height

  # Matrix input string rows - int separated by space
  def input(self):
    print('Matrix ', self.name, ' values:')
    M = []
    for i in range(self.height):
      try:
        M.append([int(j) for j in input().split()])
      except:
        s = 'Matrix Multiplication value enter error!'
        raise ValueError(s)
    # Check
    self.__init__(self.name, M)
    print()
    return M

#  Calculates Matrix multiplication.
if __name__ == '__main__':
  # # Matrixes A,  B - manual entry
  # A = Matrix('A')
  # B = Matrix('B')
  # A.input()
  # B.input()
  # Matrixes A,  B - code entry
  A = Matrix('A', [[1, 2], [5, 3], [6, 7]])
  B = Matrix('B', [[5], [1]])
  print(A)
  print(B)

  # Result Matrix A x B
  print('Result:')
  C = Matrix('C', A * B)
  print(C)

  # Compare Matrix vs Matrix
  D = Matrix('D', [[7], [28], [37]])
  print(D)
  print('C == D ', C == D)
  print()

  # Compare List vs Matrix
  E = [[7], [28], [37]]
  print('List: ', E)
  print('C == E ', C == E)
  print()

  # Compare List vs Matrix
  F = [[1], [2], [3]]
  print('List: ', F)
  print('C == F ', C == F)
  print()

  # Simple multiplication
  G = A * B
  print(G)

  # Matice - Vektor
  V = Matrix('V', [1, 2, 3])
  print(V)
