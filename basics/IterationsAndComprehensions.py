# IterationsAndComprehensions.py

'''
> Python’s iteration protocol, a method call model used by the for loop,
> list comprehensions, which are a close cousin to the for loop that applies an expression to items in an iterable.
'''
input_numbers = [1,2,3,4]
print(type(input_numbers))  # <class 'list'>

# print uses end='' here to suppress adding a \n, because line strings already have one
# without this, our output would be double-spaced;

# for loop can work on any sequence type in Python, including lists, tuples, and strings
for n in input_numbers:
    print(n ** 2, end=' ')
print()

for x in (1, 2, 3, 4):
    print(x ** 3, end=' ')
print()

for x in 'spam':
    print(x * 2, end=' ')
print()