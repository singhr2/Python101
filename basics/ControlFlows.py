# ControlFlows.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('ControlFlows.py').read())


x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')
	

'''
every Python tool that scans an object from left to right uses the iteration protocol.

'''


words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

for c in 'spam':
	print(c.upper())

## Another while loop example
x = 4
print('before while loop')
while x > 0:
	print('spam!' * x)
	x -= 1
print('after while loop')


##
# The list comprehension will often run faster than a for loop today on some types of code (perhaps even twice as fast)
# —a property that could matter in your programs for large data sets.


squares = []
for x in [1, 2, 3, 4, 5]: # This is what a list comprehension does
	squares.append(x ** 2) # Both run the iteration protocol internally
print('squares (approach-1) :', squares);

''' This is equivalent to below code '''
squares = []
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print('squares (approach-2) :', squares);


##


