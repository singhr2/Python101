#NameAttribute.py

'''
built-in attribute called __name__,

Python creates and assigns automatically as follows:
• If the file is being run as a top-level program file, 
   __name__ = "__main__" when it starts.
• If the file is being imported instead, 
	__name__ = module’s name as known by its clients.
'''
if __name__ == '__main__':
	print ('This program is being run by itself')
else:
	print ('I am being imported from another module')