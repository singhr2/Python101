# Exceptions104.py


#
#
# example : with/as statement
#
# SYNTAX: 
#     with expression [as variable]:
#          with-block
#


'''
where is the code that is actually being called when the variable goes out of scope? 
The short answer is, "wherever the context manager is defined." 
You see, there are a number of ways to create a context manager. 
The simplest is to define a class that contains two special methods: __enter__() and __exit__(). 

__enter__() returns the resource to be managed (like a file object in the case of open()). 
__exit__() does any cleanup work and returns nothing.


Context managers allow you to allocate and release resources precisely when you want to. 
The most widely used example of context managers is the with statement. 

A common use case of context managers is locking and unlocking resources and closing opened files

'''

with open('SampleTextFile.txt', 'w') as opened_file:
    opened_file.write('Hi there!\n')
    opened_file.write('Bye Bye!!\n')


#The above code opens the file, writes some data to it and then closes it. 
# If an error occurs while writing the data to the file, it tries to close it. 
# The above code is equivalent to:

'''
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
'''


#
#
#Implementing Context Manager as a Class
# Ref: http://book.pythontips.com/en/latest/context_managers.html
#
#

'''
At the very least a context manager has an __enter__ and __exit__ methods defined. 
'''


class MyFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with MyFile('SampleTextFile.txt', 'r') as opened_file:
    lines = opened_file.readlines()

# print using list comprehension
[print(x) for x in lines]