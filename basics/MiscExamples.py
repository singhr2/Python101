# MiscExamples.py


dir(dict) # dict is the name of the type

help(dict)


# Common Python expression statements
'''
Operation 			Interpretation
~~~~~~~~~~~~        ~~~~~~~~~~~~~~~~
spam(eggs, ham) 	Function calls
spam.ham(eggs) 		Method calls
'''

#!/usr/bin/env python3

'''
On Unix, when a program is invoked in the console, the file’s first two bytes are read.
* If these bytes are the ASCII characters #!, the shell assumes that the file is to be executed by an interpreter 
and that the file’s first line specifies which interpreter to use. 
This line is called the shebang (shell execute) line, and if present must be the first line in the file.
'''

'''
to redirect the output of this program to file,
	python eg01.py > eg01-output.txt
'''

import os # os Module 
print('Current Working Directory :', os.getcwd())

print('~~~~~~~~')

print("Hello", "World!")
print('hello world')
print(2 ** 4)
print('Spam!' * 8) # Repeats Spam! 8 times

print('~~~~~~~')
for x in 'ranbir':
	print(x)
	print('---')
print('Exited loop')

print('~~~~~~~~')
import sys
print('Platform:'+ sys.platform)
print('Platform:', sys.platform)


print('~~~~~~~')
name=input('enter your name:')
print('you have entered ->', name)