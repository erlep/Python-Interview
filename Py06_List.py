# -*- coding: utf-8 -*-
# % Preparing for a Python Interview: 10 Things You Should Know  https://youtu.be/DEwgZNC-KyE

# 6 List how to use

# my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = list(range(1, 12))
print("my_list: ", my_list, " - type: ", type(my_list))

# Give me each number in the list squared
squares = [num * num for num in my_list]
print("squares: ", squares, " - type: ", type(squares))
