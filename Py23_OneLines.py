#!/usr/bin/env python3
# Top 10 Python One Liners - https://youtu.be/ZW-TWrEF6qc
import datetime

print('swap variables: ', end='')
a = 5
b = 10
a, b = b, a
print(a, b)

print('list: ', end='')
squares = [i*i for i in range(10) if i % 2 == 0]
print(squares)

print('1 line if: ', end='')
var = 42 if 3 > 2 else 99
print(var)

print('unpack list: ', end='')
data = [0, 1, 2, 3, 4, 5]
print(*data)

print('days left in year: ', end='')
# import datetime; print((datetime.date(2022, 12, 23)-datetime.date.today()).days)
print((datetime.date(2022, 12, 31)-datetime.date.today()).days)
# alias daysleft='python - c "import datetime;print((datetime.date(2022, 12, 23)-datetime.date.today()).days)"'

print('reverse list by slicing: ')
print(data)
data = data[::-1]
print(data)

print('Palindrome - stejne kdyz se cte pozpatku: ', end='')
a = 'level'
print(a)
print(a == a[::-1])

print('assign multiple variable: ', end='')
name, age, language = 'Jan', 31, "Python"
print(name, age, language)

print('number string to integer list: ', end='')
user_input = '1 2 3 4 5 6'
# my_list = list(map(int, user_input.split()))
my_list = [int(x) for x in user_input.split()]
print(my_list)


print('read file into list: ', end='')
lines = [line.strip() for line in open('Py23_OneLines.txt', 'r')]
print(lines)

print('http server: ', end='')
print('from cmd line: python -m http.server')
