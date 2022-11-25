# Asterisks in Python: what they are and how to use them - https://bit.ly/3GbgL4Z
print('2*5', 2*5)
print('2**5', 2**5)
print()

# *list
numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers, sep='; ')
print()

# *list
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits)
print()

# The ** operator does something similar, but with keyword arguments
date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print('filename = "{year}-{month}-{day}.txt".format(**date_info)', filename)
print()

# This function accepts any number of arguments:
def MultiArgumentFce(*argumenty):
  print('  argumenty', argumenty, '  len(argumenty)', len(argumenty), '  type(argumenty)', type(argumenty))
  # for idx, val in enumerate(argumenty):
  #   print('idx', idx, 'val', val)
print("MultiArgumentFce()", MultiArgumentFce())
print("MultiArgumentFce(1)", MultiArgumentFce(1))
print("MultiArgumentFce('2','test')", MultiArgumentFce('2', 'test'))
print("MultiArgumentFce(3,'test','arguments')", MultiArgumentFce(3, 'test', 'arguments'))
print()

# * for unpacking
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
first, second, *remaining = fruits
print(remaining)  # ['watermelon', 'tomato']
first, *remaining = fruits
print(remaining)  # ['pear', 'watermelon', 'tomato']
first, *middle, last = fruits
print(middle)    # ['pear', 'watermelon']
((first_letter, *remaining), *other_fruits) = fruits
print(first_letter)  # l
print(remaining)  # ['e', 'm', 'o', 'n']
print()

# Double asterisks in dictionary literals
date_info = {'year': '2020', 'month': '01', 'day': '7'}
event_info = {**date_info, 'group': "Python Meetup"}
print(event_info)  # {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'}
print()
