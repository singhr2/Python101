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