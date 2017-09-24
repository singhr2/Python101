# IterateUsingIterAndNext.py

'''
The iter() method returns an iterator for the given object.
iter(object[, sentinel])
    sentinel (Optional) - special value that is used to represent the end of a sequence

Reference: http://www.diveintopython3.net/special-method-names.html
'''

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# We write iter(seq), and Python calls seq.__iter__()
vowelsIter = iter(vowels)
vowelsIterReversed = reversed(vowels)

# We Write next(seq), and python calls seq.__next__()
# OUTPUT: aeiou
for i in vowelsIter:
    print(i, end='')

# Printing in reverse order
# OUTPUT: uoiea
print('\n Printing in reverse order')
for x in vowelsIterReversed:
    print(x, end='')

