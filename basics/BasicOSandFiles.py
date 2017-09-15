'''
This files demos basic functions related to OS and Files
'''

import os

print('Current Directory :', os.getcwd())

import sys

# Is it python version ?
print('sys.version :', sys.version) # 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)]

print('OS :', sys.getwindowsversion()) #sys.getwindowsversion(major=6, minor=1, build=7601, platform=2, service_pack='Service Pack 1')
print('platform :', sys.platform)#win32

nextinput = input('Enter Your Year(YY) of Birth')
age = 117 - int(nextinput)
print('Your age is :', age)

# Printing multiple values
print(os.getcwd(), sys.getwindowsversion(), nextinput, age)
