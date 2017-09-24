# Files02.py

'''
>> xDummyFile.txt
This is 1st line without line break This is 2nd line with line break
This is last line
'''

print('\n ----- printing content using for loop')
for line in open('xDummyFile.txt'):
    # print(type(line))  # <class 'str'>
    # line[0] = 'T'
    print(line, end='')
print('\n *** Done printing content using for loop.')


# 2 : Print only if first character in line is T
print('print if line starts with t')
# OUTPUT : case sensitive, only 2nd line gets printed
lines = [line.rstrip() for line in open('xDummyFile.txt') if line[0] == 't']
print(lines)