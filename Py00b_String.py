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
mystringliteral6 = "this is a string with \047quotes\047"

print(mystringliteral1)
print(mystringliteral2)
print(mystringliteral3)
print(mystringliteral4)
print(mystringliteral5)
print(mystringliteral6)

# Python  String
s = 'Hi\nHello'
print(s)
# Python Raw String
raw_s = r'Hi\nHello'
print(raw_s)

# Python String format() Method - https://www.w3schools.com/python/ref_string_format.asp
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print('''txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36): ''')
print('       ',txt1)
print('''txt2 = "My name is {0}, I'm {1}".format("John",36): ''')
print('       ',txt2)
print('''txt3 = "My name is {}, I'm {}".format("John",36): ''')
print('       ',txt3)

print("OkDone.")
