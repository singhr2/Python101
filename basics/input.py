#input.py
'''
In 3.X, 
	raw_input was renamed input, and 
	print is a built-in function instead of a statement
	Further, the received data is always treated as string.
'''
import sys

ageStr: str = input('Enter your age :')
print('Entered age :', ageStr)

if ageStr.isdigit():
	print('received numeric input')
else:
	print('received input is not numeric ')
	sys.exit(0) #Exit program if the input is not valid number

ageInt = int(ageStr)
print('ageInt :', ageInt)

print( type(ageInt) )

