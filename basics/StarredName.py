#StarredName.py

'''
single starred name, *X, can be used in the assignment target
in order to specify a more general matching against the sequence—
the starred name is assigned a list,
which collects all items in the sequence not assigned to other names.

More generally, wherever the starred name shows up,
it will be assigned a list that collects every unassigned name at that position:
'''

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d) #1 2 3 4

#ValueError: too many values to unpack (expected 2)
#a, b = seq

r, *s = seq
print(r) #1
print(s) #[2, 3, 4]


*y, z = seq
print(y) # [1, 2, 3]
print(z) # 4


u, *v, w = seq
print(u) # 1
print(v) # [2, 3]
print(w) # 4


a, *b = 'spam'
print(a) #s
print(b) #['p', 'a', 'm']

seq = [1, 2, 3, 4]
a, b, c, d, *e = seq
print(a, b, c, d, e) # 1 2 3 4 []

a, b, *e, c, d = seq
print(a, b, c, d, e) # 1 2 3 4 []

# SyntaxError: two starred expressions in assignment
#a, *b, c, *d = seq

a = b = c = 'spam'
print(a,b,c) #spam spam spam

#ValueError: too many values to unpack (expected 3)
#a , b , c = 'spam'
#print(a,b,c)

print('\nPrinting a1, *b1, c1')
(a1, *b1, c1) = [(1, 2, 3, 4), (5, 6, 7, 8)]
print(a1) # (1, 2, 3, 4)
print(b1) # []
print(c1) # (5, 6, 7, 8)


print('\nPrinting a2,b2, c2)')
a2, *b2, c2 = (1, 2, 3, 4)
print(a2) # 1
print(b2) # [2, 3]
print(c2) # 4

# Not understood
print('\n processing while loop...')
L = [1, 2, 3, 4]
while L:
    front, *L = L # Get first, rest without slicing
    print(front, L)

