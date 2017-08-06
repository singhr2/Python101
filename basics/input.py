
#In Python 3, raw_input() function is deprecated.
## Further, the received data is always treated as string.
ageStr: str = input('Enter your age :')
print('Entered age :', ageStr)

ageInt = int(ageStr)
print('ageInt :', ageInt)

print( type(ageInt) )

