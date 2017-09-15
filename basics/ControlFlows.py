# ControlFlows.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('ControlFlows.py').read())

## REFERENCE:
# http://www.openbookproject.net/books/bpp4awd/ch04.html

'''
* Parentheses are optional	: if (x < y)  ~ if x < y
* End-of-line ~ end of statement
* End of indentation ~  end of block
'''

a = 1;
b = 2;
print(a + b)  # Three statements on one line

# you can make a single statement span across multiple lines. To make this work, you simply have to enclose
# part of your statement in a bracketed pair—parentheses (()), square brackets ([]), or curly braces ({}).
X = (a +
     b)
print('X is :', X)

# The if else statement
food = 'veg'
if food == 'spam':
    print('Ummmm, my favorite!')
else:
    print("No, I won't have it. I want spam!")

# ??? pass (Empty placeholder)
if True:  # This is always true
    pass  # so this is always executed, but it does nothing
else:
    pass

# e.g. 3
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

# Nested conditionals
print('\n number comparison')
num_1 = int(input("Please enter 1st number: "))
num_2 = int(input("Please enter 2nd number: "))
if num_1 < num_2:
    print(num_2, 'is greater than', num_1)
else:
    if num_2 < num_1:
        print(num_1, 'is greater than', num_2)
    else:
        print('Both numbers are same')

'''
every Python tool that scans an object from left to right uses the iteration protocol.

'''

# for LOOP_VARIABLE in SEQUENCE:
#    STATEMENTS

for friend in ['Shreya', 'Anshi']:
    invitation = "Hi " + friend + ".  Please come to my party on Saturday!"
    print(invitation)

# printing table
for x in range(13):  # Generate numbers 0 to 12
    print(x, '\t', 2 ** x)

# e.g.
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
for x in [1, 2, 3, 4, 5]:  # This is what a list comprehension does
    squares.append(x ** 2)  # Both run the iteration protocol internally
print('squares (approach-1) :', squares);

''' This is equivalent to below code '''
squares = []
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print('squares (approach-2) :', squares);

## BREAK
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:  # if the number is odd
        break  # immediately exit the loop
    print(i)
print("done")

while True:
    reply = input('Enter text, type stop to exit:')
    if reply == 'stop': break
    print(reply.upper())
print('Bye, i\'ll stop now as you typed stop')

# CONTINUE
for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1:  # if the number is odd
        continue  # don't process it
    print(i)
print("done")


# with/as : Context managers (3.X, 2.6+)
#The advantage of using a with statement is that it is guaranteed to close the file no matter how the nested block exits.
#This allows common try…except…finally usage patterns to be encapsulated for convenient reuse.
'''
with open('output.txt', 'w') as f:
    f.write('Hi there!')
'''
with ['spam'] as iterator:
    print(iterator)


# Comprehensions
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('M :', M)

col2 = [row[1] for row in M]
print('col2 :', col2)

print('after adding 1 to send element in each row :', [row[1] + 1 for row in M])

print('Filter out odd items :', [row[1] for row in M if row[1] % 2 == 0])
