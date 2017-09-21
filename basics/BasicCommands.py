# BasicCommands.py


# To check Python version (at command prompt)
#1) At command prompt, type python
#python
#2) At command prompt, type python -V (capital V)
# python -V
# -or-
# python --version
#3) in code
import sys
print(sys.version) # Human readable -> 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)]
print(sys.version_info) # sys.version_info(major=3, minor=6, micro=2, releaselevel='final', serial=0)

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


