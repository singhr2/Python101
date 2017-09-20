# BasicCommands.py
"""
triple double-quote string should be used for doc string
"""

'''
triple single-quote string = comment ?
'''

'''
print()
    > it provides a simple interface to the sys.stdout object
    > print is function in Python 3.X
    > print was Statement in Python 2.X
'''


#print 'Hello Ranbir (python 2.x)'
print("Hello Ranbir (python 3)")

# This is equivalent to
import sys
sys.stdout.write("Hello Ranbir (python 3) using sys.stdout \n")  # hello world

#print error messages to the standard error stream
sys.stderr.write(('Bad!' * 8) + '\n')


