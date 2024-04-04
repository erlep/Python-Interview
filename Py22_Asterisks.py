# * - Asterisk = Unpack Operator
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
def join_text(*strings, sep: str) -> str:
  return sep.join(strings)
print(join_text('A', 'B', 'C', 'D', sep='-'))
print(join_text('X', 'Y', 'Z', sep='='))
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

# asterisks as forsing to use keywords arguments - https://youtu.be/7fSHTqM8gHs?si=8yRpaQShuGPlIz0G
def MyFce(file: str, *, quality: str, privacy: str) -> None:
  # pass
  # ...
  # raise NotImplementedError()
  print(f'{file=} {quality=}  {privacy=}')
MyFce('qq.tx', quality='qlt', privacy='privacy')
# MyFce('qq.tx', 'qlt', 'privacy')
