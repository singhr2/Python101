# IterationsAndComprehensions.py

input_numbers = [1,2,3,4]
print(type(input_numbers))  # <class 'list'>

#print uses end='' here to suppress adding a \n, because line strings already have one 
# without this, our output would be double-spaced;
for n in input_numbers: print(n ** 2, end=' ')

