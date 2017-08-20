# Tuples.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('Files.py').read())


'''
# 'r' (read) is the default processing mode
'''
print('opening file in \'w\' (write) mode')
f = open('DummyFile.txt', 'w')
f.write('This is 1st line without line break ')
f.write('This is 2nd line with line break \n')
f.write('This is last line')

f.close()

print('opening file in \'r\' (read) mode')
f = open('DummyFile.txt', 'r')
fileContents = f.read()
print('fileContents :', fileContents)

print('splitting file contents ')
print(fileContents.split())

# printing content using for loop
for line in open('DummyFile.txt'): print(line)


# binary files are useful for processing media, accessing data created by
# C programs, and so on.
# Python’s struct module can both create and unpack
# packed binary data—raw bytes that record values that are not Python objects—to be
# written to a file in binary mode.

'''
To access files containing non-ASCII Unicode text, we simply pass in an encoding name
if the text in the file doesn’t match the default encoding for our platform.
'''
print('\n')
file = open('DummyFile.txt', 'r', encoding='utf-8')
print(file.readlines())