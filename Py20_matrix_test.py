#   mx_mulV2_test.py
#   py.test

import pytest
from mx_mulV2 import Matrix
# def test_mx_multiple(A, B, C):
#   assert mx_multiple(A, B) == C


# Case 1
def test_mx_multiple_1():
  A = Matrix('A', [[1, 2], [5, 3], [6, 7]])
  B = Matrix('B', [[5], [1]])
  C = Matrix('C', [[7], [28], [37]])
  assert A * B == C

# Case 2
def test_mx_multiple_2():
  A = Matrix('A', [[12, 7, 3], [4, 5, 6], [7, 8, 9]])
  B = Matrix('B', [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]])
  C = Matrix('C', [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]])
  assert A * B == C

# Cases
test_mx_multiple_1()
test_mx_multiple_2()
