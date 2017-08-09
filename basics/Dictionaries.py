# Dictionaries.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\StringDemo.py
# > python
# > exec(open('Dictionaries.py').read())

# known as mappings.
# collections of other objects, but they store objects by key instead of by relative position
# only mapping type in Python’s core objects set, are also mutable: like lists

# left-to-right order of dictionary keys is scrambled. 
# Mappings are not positionally ordered


D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print('type(D) :', type(D))

# Fetch value of key 'food'
print('D[\'food\'] :', D['food'])

# Add 1 to 'quantity' value
print('<before> D :', D)
D['quantity'] += 1
print('<after> D :', D)


####
# Starting with empty dictionary
Developer1 = {}
Developer1['name'] = 'Ranbir'
Developer1['job family'] = 'Java'
print('\nDeveloper1 :', Developer1)


####
# Create using keyword arguments
Developer2 = dict(name='Anshi', job='student', age=6)
print('\nDeveloper2 :', Developer2)

## Create using zipping
Developer3 = dict(zip(['name', 'job', 'age'], ['Shreya', 'student', 11]))
print('\nDeveloper3 :', Developer3)


## Nesting