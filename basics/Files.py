# Files.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('Files.py').read())
# or
# > python Files.py

'''
! Must have exactly one of create/read/write/append mode and at most one plus
> 'r' (read) : default processing mode
> 'w' : write
> 'a' : 'a' to open for appending text to the end (e.g., for adding to logfiles).
> 'rb': Python 3.X bytes files (bytes strings)
> Adding a + opens the file for both input and output (i.e., you can both read and
write to the same file object,

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

fileToRead = open('_Git Commands.txt', 'r')
print('\n >>> reading 6 chars [', fileToRead.read(6), ']')
print() #Read up to next N characters (or bytes) into a string

print('>>> Reading next line (including \\n newline) into a string')
aString = fileToRead.readline()
print(aString)

# This will read from where previous command has left.
print('\n >>> read() - Read entire file into a single string')
print(fileToRead.read())  # Read entire file into a single string

#Change file position to offset N for next operation
fileToRead.seek(0)

print('\n >>> readlines() - ', fileToRead.readlines())  # Read entire file into list of line strings (with \n)


#use line File iterators read line by line
for line in open('cls.py'):
    print(line)

#Flush output buffer to disk without closing
#someFileName.flush()

#Manual close (done for you when file is collected)
fileToRead.close()

#  + Not working
fileToRead2 = open('SampleTextFile.txt', 'w+')
fileToRead2.writelines('-----')
fileToRead2.flush()
print(fileToRead2.readlines())
