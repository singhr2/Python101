#ReadingWritingCsvFile.py

import csv

#The csv module’s reader and writer objects read and write sequences.
#Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.
# csv.reader(csvfile, dialect='excel', **fmtparams)¶
# csv.writer(csvfile, dialect='excel', **fmtparams)¶

#csvFileReader = csv.reader(open('xSampleCsvFile.csv', newline=''), delimiter=' ', quotechar='|')
#spamWriter = csv.writer(open('xSampleCsvFile.csv', 'w', newline=''), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

#dataToWrite=[[1,'steve',9999]]
dataToWrite=[[1,'steve',9999],[2,'bill',9090]]
targetFileName='xSampleCsvFile2.csv'

fileToWrite=open(targetFileName, 'w')
spamWriter = csv.writer(fileToWrite)
#spamWriter = csv.writer(open('xSampleCsvFile2.csv', 'w'), delimiter=',')
spamWriter.writerows(dataToWrite)
fileToWrite.close()

for row in csv.reader(open(targetFileName, newline='\n'), delimiter=','):
   print(row)
