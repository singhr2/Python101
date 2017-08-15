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
	


words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

for c in 'spam':
	print(c.upper())
	
x = 4
print('before while loop')
while x > 0:
	print('spam!' * x)
	x -= 1
print('after while loop')




