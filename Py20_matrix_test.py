#   Py20_matrix_test.py
#   To run: pytest

# Testing Python Applications with Pytest - https://bit.ly/3jhgS49

from Py20_matrix import Matrix
import pytest

# Empty Matrix []
def test_mx_multiple_1():
  A = Matrix('A', [])
  assert A == []

# Matrix [1, 2, 3]
def test_mx_multiple_2():
  A = Matrix('A', [[1], [2], [3]])
  assert A == [[1], [2], [3]]

# Matrix [1, 2, 3]
def test_mx_multiple_3():
  A = Matrix('A', [1, 2, 3])
  assert A == [[1, 2, 3]]

# Wrong Matrix ['1', 2, 3] - ERROR
def test_mx_multiple_4():
  with pytest.raises(ValueError):
    A = Matrix('A', [['1'], [2], [3]])

# Wrong Matrix  #2, #3, #2  - ERROR
def test_mx_multiple_5():
  with pytest.raises(ValueError):
    A = Matrix('A', [[1, 2], [1, 2, 3], [1, 2]])

# Case 1 - multiplication - OK
def test_mx_multiple_6():
  A = Matrix('A', [[1, 2], [5, 3], [6, 7]])
  B = Matrix('B', [[5], [1]])
  C = Matrix('C', [[7], [28], [37]])
  assert A * B == C

# Case 2 - multiplication - OK
def test_mx_multiple_7():
  A = Matrix('A', [[12, 7, 3], [4, 5, 6], [7, 8, 9]])
  B = Matrix('B', [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]])
  C = Matrix('C', [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]])
  assert A * B == C

# Matrixes width vs. height check - ERROR
def test_mx_multiple_8():
  A = Matrix('A', [[1, 2], [5, 3], [6, 7]])
  B = Matrix('B', [[5], [1], [1]])
  with pytest.raises(ValueError):
    C = A * B

''' pytest - Decorator
@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ddl', LikeState.liked),
])
@pytest.mark.skip(reason="regexes not supported yet")
@pytest.mark.xfail
@pytest.fixture
'''

@pytest.mark.parametrize("test_input, expected", [
    (Matrix('A', [1, 2, 3]), [[1, 2, 3]]),
    (Matrix('B', [4, 5, 6]), [[4, 5, 6]]),
    (Matrix('C', [7, 8, 9]), [[7, 8, 9]]),
])
def test_mx_more_para(test_input, expected):
  a = Matrix('', test_input)
  print(a)
  assert Matrix('', test_input) == expected

@pytest.mark.skip(reason="string input not supported yet")
def test_mx_string():
  assert Matrix('A', [1, 2, 3]) == [[1, 2, 3]]

@pytest.mark.xfail
def test_mx_wrong_matrix():
  assert Matrix('A', [[1, 2], [1, 2, 3], [1, 2]])

@pytest.mark.xfail
def test_divide_by_zero():
  assert 1 / 0 == 1

# @pytest.fixture - defined in conftest.py
def test_print(capture_stdout):
  print("hello")
  assert capture_stdout["stdout"] == "hello\n"

# Cases
test_mx_multiple_1()
test_mx_multiple_2()
test_mx_multiple_3()
test_mx_multiple_4()
test_mx_multiple_5()
test_mx_multiple_6()
test_mx_multiple_7()
test_mx_multiple_8()
