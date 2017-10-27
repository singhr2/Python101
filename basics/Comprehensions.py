#Comprehensions.py

'''
> List comprehensions apply an arbitrary expression to items in an iterable, rather than applying a function.
  
  Syntax: [ expression for target in iterable ]

* Note: list comprehensions construct list results, remember that they can iterate over any sequence or other iterable type (see eg below)

'''

#Say we need to obtain a list of all the integers in a sequence and then square them:

a_list = [1, '4', 9, 'a', 0, 4]
squared_ints = [ e**2 for e in a_list if isinstance(e, int) ]
print (squared_ints) # [ 1, 81, 0, 16 ]


#----------------------------------------------------
# we wish to collect the ASCII codes of all characters in an entire string

# [Option-1] : 
input_string = 'spam'
res = []
for x in input_string :
    res.append(ord(x)) # Manual results collection
print(res) # [115, 112, 97, 109]


# [Optin-02] : Using map
res2 = list(map(ord, input_string)) # Apply function to sequence (or other)
print(res2) # [115, 112, 97, 109]


# [Option-03] : using list comprehension
# map maps a function over an iterable, 
# list comprehensions map an expression over a sequence or other iterable
res3 = [ord(x) for x in input_string] # Apply expression to sequence (or other)
print(res3) # [115, 112, 97, 109]


# picking up even numbers from 0 to 4 (using modulus operator %)
#option-1 : List comprehension
list1 = [x for x in range(5) if x % 2 == 0]
print(list1) # [0, 2, 4]

#option-2 : lambda
list2 =list(filter((lambda x: x % 2 == 0), range(5)))
print(list2) # [0, 2, 4]


# using multiple iterables
[x + y for x in 'spam' for y in 'SPAM']
[x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]

