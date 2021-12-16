# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE
# % CoreyMSchafer/code_snippets - https://is.gd/qP1inR
# Python Data Types - https://www.w3schools.com/python/python_datatypes.asp

# 0 String
# Single quotes vs. double quotes in Python - no diff - https://is.gd/iRvt7e

mystringliteral1 = "this is a string with 'quotes'"
mystringliteral2 = 'this is a string with "quotes"'
mystringliteral3 = """this is a string with "quotes" and more 'quotes'"""
mystringliteral4 = '''this is a string with 'quotes' and more "quotes"'''
mystringliteral5 = 'this is a string with "quotes"'
mystringliteral6 = "this is a string with \042quotes\042"
mystringliteral7 = "this is a string with \047quotes\047"
print(mystringliteral1)
print(mystringliteral2)
print(mystringliteral3)
print(mystringliteral4)
print(mystringliteral5)
print(mystringliteral6)
print(mystringliteral7)

# Python  String
s = 'Hi\nHello'
print(s)
# Python Raw String
raw_s = r'Hi\nHello'
print(raw_s)
print()

# Python String format() Method - https://www.w3schools.com/python/ref_string_format.asp
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print('''txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36): ''')
print('       ', txt1)
print('''txt2 = "My name is {0}, I'm {1}".format("John",36): ''')
print('       ', txt2)
print('''txt3 = "My name is {}, I'm {}".format("John",36): ''')
print('       ', txt3)
print()


# Trim = .strip()
print('Trim string = .strip() ')
mezery = '    aa bb *** cc    '
print('>>mezery<<  ', '>>' + mezery + '<<')
print('>>mezery.strip()<<  ', '>>' + mezery.strip() + '<<')
while '**' in mezery:
  mezery = mezery.replace('**', '*')
print('>>mezery<<  ', '>>' + mezery + '<<')
print()

# join strings
words = ['book', 'car', 'plane', 'chair', 'floor']
'''
Desired output:
book/car/plane/chair/floor
'''
print("words: ", words)
output = '/'.join(words)
print("join output: ", output)

# Replace
carka = output.replace("/", ",")
print("carka: ", carka)

# Split
split = carka.split(",")
print("split: ", split)

# Display string multiple times - https://bit.ly/3H4aOqw
print('-' * 8)

# f-Strings - https://bit.ly/3H1a7yl
name = "Pepa " + \
    "Zdepa"
age = 99
print(f"Hello, {name}. You are {age}.")

# Format()
num_value = 123.45678
str_value = '{:.2f}'.format(num_value)
print(str_value)

# Check if variable is string - using isinstance() - https://bit.ly/3wPWGfS
test_string = "GFG"
print("The original string : " + str(test_string))
res = isinstance(test_string, str)
print("Is variable a string ? : " + str(res))

print("OkDone.")
