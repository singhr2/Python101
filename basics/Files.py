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
  b) binary (such as an image or audio file), which deals in raw bytes and does no data translation
     binary files are useful for processing media, accessing data created by C programs, and so on.
     Python’s struct module can both create and unpack packed binary data—raw bytes
     that record values that are not Python objects—to be written to a file in binary mode.
'''


print('opening file in \'w\' (write) mode')
f = open('xDummyFile.txt', 'w')  # 'w' = write-mode
f.write('This is 1st line without line break ')
f.write('This is 2nd line with line break \n')
f.write('This is last line')

f.close()

print('opening file in \'r\' (read) mode')
f = open('xDummyFile.txt', 'r') # 'r' = read-mode
fileContents = f.read()
print('fileContents :', fileContents)

print('splitting file contents ')
print(fileContents.split())

# printing content using for loop
for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)

print('\n ----- printing content using for loop')
for line in open('xDummyFile.txt'):
    # print(type(line))  # <class 'str'>
    print(line, end='')
print('\n *** Done printing content using for loop.')


#To access files containing non-ASCII Unicode text, we simply pass in an translation (a.k.a. encoding) name
#if the text in the file doesn’t match the default encoding for our platform.
print('\n')
file = open('xDummyFile.txt', 'r', encoding='utf-8')
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

fileToRead = open('SampleTextFile.txt', 'r')
print('\n >>> reading 6 chars [', fileToRead.read(6), ']')
print() #Read up to next N characters (or bytes) into a string

# open file objects have a method called readline, which reads one line of text from a file at a time—
# each time we call the readline method, we advance to the next line
print('>>> Reading next line (including \\n newline) into a string')
aString = fileToRead.readline()
print(aString)

# This will read from where previous command has left.
print('\n >>> read() - Read entire file into a single string')
print(fileToRead.read())  # Read entire file into a single string

#Change file position to offset N for next operation
fileToRead.seek(0)

print('\n >>> readlines() - ', fileToRead.readlines())  # Read entire file into list of line strings (with \n)


#Flush output buffer to disk without closing
#someFileName.flush()

#Manual close (done for you when file is collected)
fileToRead.close()

#  readline Not working
print('>>>>>  <<<<<<<')
fileToRead2 = open('xSampleTextFile.txt', 'w+')
fileToRead2.write('A,B,C')  # writelines()
fileToRead2.write('\n2,3,4')
fileToRead2.flush()
line_read = fileToRead2.readline()
print('line_read ?:', line_read) # read 1 line only

fileToRead2.close()
# readline() didn't worked, so close and open again
fileToRead2 = open('xSampleTextFile.txt', 'r')
line_read = fileToRead2.readline()
print('line_read >> :', line_read) # read 1 line only
print('line.rstrip() :', line_read.rstrip())
print('line.split(\',\') :', line_read.split(','))



# __next__ in 3.X
# it returns the next line from a file each time it is called. 
# The only noticeable difference is that __next__ raises a built-in StopIteration exception at end-of-file instead of returning an empty string (as done by readline)
#
print('\n -------\n printing file contents using __next__()\n -------')
'''
f = open('xSampleTextFile.txt')
while f.__next__() != '' :
	f.__next__()
'''

#RECOMMENDED : use 'File iterators' to read by lines
#best approach is to not read it at all—instead, allow the for loop to automatically call __next__ to advance to the next line on each iteration. 
#The file object’s iterator will do the work of automatically loading lines as you go.
for line in open('xSampleTextFile.txt'):
    print(line)

# old way of doing this
print('\n -------\n printing file contents using while loop \n -------')
f = open('xSampleTextFile.txt')
while True:
	line = f.readline()
	if not line: break  # line will equal False if zero-length
	print(line, end='')

'''
	Python 3.X also provides a built-in function, next,
	that automatically calls an object’s __next__ method. 
	i.e. next(file) built-in calls file.__next__() in 3.X
	
	Given an iterator object X, the call next(X) is the same as X.__next__() on 3.X
'''
# next() 

print('\n -------\n printing file contents using next(f) built-in function\n -------')
# will return StopIteration exception if trying to call after eof
f = open('xSampleTextFile.txt')
print(next(f), end='') # The next(f) built-in calls f.__next__() in 3.X
print(next(f), end='') # next(f) => [3.X: f.__next__()], [2.X: f.next()]

