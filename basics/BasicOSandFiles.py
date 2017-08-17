'''
This files demos basic functions related to OS and Files
'''

import os

print('Current Directory :', os.getcwd())

import sys

print('OS :', sys.getwindowsversion())
print(sys.platform)

nextinput = input('Enter Your Year(YY) of Birth')
age = 117 - int(nextinput)
print('Your age is :', age)

# Printing multiple values
print(os.getcwd(), sys.getwindowsversion(), nextinput, age)
