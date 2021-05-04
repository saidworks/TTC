# #uses standard library documentation
# import os
# import datetime
# access = os.path.getatime('/../../Tutorials')
# print(datetime.timedelta(seconds=access))
# #import package
# from MyFirstPackage import ModuleA
# string=input("enter a word").lower()
# letter=input("enter the letter you want to know its frequency").lower()
# ModuleA.count_string(string,letter)
#
# from MyFirstPackage.includes import ModuleB

#list of functions in a package
import numpy
# import matplotlib
#
# print(dir(matplotlib))
# help(matplotlib.LooseVersion())
from random import choice
board = [[[choice(['a','b','c','d']) for i in range(5)] for j in range(5)] for k in range(5)]
print(board)
for i in range(5):
    for j in range(5):
        board[i][j] = choice(['a','b','c','d'])
print(board)

import turtle
Said = turtle.Turtle()
Said.pendown()
for i in range(100):
    Said.forward(2*i)
    Said.left(90)
input()