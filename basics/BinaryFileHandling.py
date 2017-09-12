# BinaryFileHandling.py
fileToRead = open('SampleTextFile.txt', 'rb')
data = fileToRead.read()
print(data)
fileToRead.close

print('Is file open ? ', fileToRead.closed)

if not fileToRead.closed :
        print(fileToRead.name + ' is open in ' + fileToRead.mode)


# read the same file in text mode
fileToRead = open('SampleTextFile.txt', 'r+')
data = fileToRead.read() # For readin one line , use readline() 
print(data)
