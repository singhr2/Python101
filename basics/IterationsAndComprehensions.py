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


# The built-in function iter() 
#	takes an iterable object and returns an iterator.
#
# Each time we call the next method on the iterator gives us the next element. If there are no more elements, it raises a StopIteration.
iterator1 = iter(input_numbers)
print('Type of iterator :', type(iterator1))
print('Next item :', next(iterator1))
print('Next item :', next(iterator1))
print('Next item :', next(iterator1))
print('Next item :', next(iterator1))
# StopIteration as no more element to iterate
#print('Next item :', next(iterator1))


#
# The enumerate() method 
#		> syntax: enumerate(iterable, start=0)
#					start (optional) - enumerate() starts counting from this number.	
#
#		> The enumerate() method adds counter to an iterable and returns it(the enumerate object).
#			The returned object is a enumerate object.

# eg1
grocery = ['bread', 'milk', 'butter']

'''
(0, 'bread')
(1, 'milk')
(2, 'butter')
'''
for item in enumerate(grocery):
  print(item)

'''
0 bread  
1 milk   
2 butter 
'''
print('\n')
for count, item in enumerate(grocery):
  print(count, item)

'''
100 bread    
101 milk     
102 butter   
'''
print('\n')

# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)
 
 

# List Comprehension
# List comprehensions are written in square brackets because they are ultimately a way to construct a new list.

print('-----')
L1 = [11, 12, 13, 14, 15]
for n in L1:
    print (n)

# alternate approach
# list comprehension expression
L2 = [x + 10 for x in L1]
print('L2 :', L2)  # L2 : [21, 22, 23, 24, 25]

'''
21
22
23
24
25
'''
for x in L2:
	print(x)

## Convert to uppercase
X2 =['This', 'is', 'a', 'sample', 'input']
for n2 in X2:
	print(n2.upper())

