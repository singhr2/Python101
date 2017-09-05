# Files.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('Files.py').read())
# or
# > python Files.py

'''
> 'r' (read) is the default processing mode

> Files work in two modes:
  a) text, which represents content as str and implements Unicode encodings, and
  b) binary, which deals in raw bytes and does no data translation
     binary files are useful for processing media, accessing data created by C programs, and so on.
     Python’s struct module can both create and unpack packed binary data—raw bytes
     that record values that are not Python objects—to be written to a file in binary mode.

'''


print('opening file in \'w\' (write) mode')
f = open('DummyFile.txt', 'w')  # 'w' = write-mode
f.write('This is 1st line without line break ')
f.write('This is 2nd line with line break \n')
f.write('This is last line')

f.close()

print('opening file in \'r\' (read) mode')
f = open('DummyFile.txt', 'r') # 'r' = read-mode
fileContents = f.read()
print('fileContents :', fileContents)

print('splitting file contents ')
print(fileContents.split())

# printing content using for loop
for line in open('DummyFile.txt'): print(line)

#To access files containing non-ASCII Unicode text, we simply pass in an translation (a.k.a. encoding) name
#if the text in the file doesn’t match the default encoding for our platform.
print('\n')
file = open('DummyFile.txt', 'r', encoding='utf-8')
print(file.readlines())


'''
#The problem here is that \n is taken to stand for a newline character, and \t is replaced with a tab.
below line will produce following error=> OSError: [Errno 22] Invalid argument: 'C:\new\text.dat'
    myfile = open('C:\new\text.dat', 'w')

If the letter r (uppercase or lowercase) appears just before the opening quote of a string, it turns off the escape mechanism.
    myfile = open(r'C:\new\text.dat', 'w')
Or keep your backslashes by simply doubling them 
    myfile = open('C:\\new\\text.dat', 'w')
'''
