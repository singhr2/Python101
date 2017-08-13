# Dictionaries.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\StringDemo.py
# > python
# > exec(open('Dictionaries.py').read())

# known as mappings.
# collections of other objects, but they store objects by key instead of by relative position
# only mapping type in Python’s core objects set, are also mutable: like lists

# dictionaries are not sequences, they don’t maintain any dependable left-to-right order.
# left-to-right order of dictionary keys is scrambled. 
# Mappings are not positionally ordered


D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print('type(D) :', type(D))

# Fetch value of key 'food'
print('D[\'food\'] :', D['food'])

# Add 1 to 'quantity' value
print('<before> D :', D)
D['quantity'] += 1
print('<after> D :', D)


####
# Starting with empty dictionary
Developer1 = {}
Developer1['name'] = 'Ranbir'
Developer1['job family'] = 'Java'
print('\nDeveloper1 :', Developer1) #  {'name': 'Ranbir', 'job family': 'Java'}


####
# Create using keyword arguments
Developer2 = dict(name='Anshi', job='student', age=6) 
print('\nDeveloper2 :', Developer2) # {'name': 'Anshi', 'job': 'student', 'age': 6}

## Create using zipping
Developer3 = dict(zip(['name', 'job', 'age'], ['Shreya', 'student', 11]))
print('\nDeveloper3 :', Developer3) #  {'name': 'Shreya', 'job': 'student', 'age': 11}


## Python’s object nesting
nestedEmpRecord = {
		'skillFamily': 'java', #
		'name': { 'lName': 'Singh', 'fName': 'Ranbir'},   # nested dict
		'roles' : ['Developer', 'Designer', 'Architect'] # nested list
	}	

print('\n nestedEmpRecord :', nestedEmpRecord)
print('Name :', nestedEmpRecord['name'])
print('First Name :', nestedEmpRecord['name']['fName'])
print('Roles :', nestedEmpRecord['roles'])
print('2nd Roles :', nestedEmpRecord['roles'][1])
print('skillFamily :', nestedEmpRecord['skillFamily'])

#Add another roles
nestedEmpRecord['roles'].append('Consultant') # Add one more job desc
print('nestedEmpRecord(after adding job) :', nestedEmpRecord)

# fetching a nonexistent key will throw an error
# UNCOMMENT below line to get #KeyError: 'garbage'
# print('nestedEmpRecord :', nestedEmpRecord['garbage']) 

# dictionary in membership expression
# Check if key exists
print( 'garbage in nestedEmpRecord :', 'garbage' in nestedEmpRecord)
print( 'skillFamily in nestedEmpRecord :', 'skillFamily' in nestedEmpRecord)

#if not 'garbage' in nestedEmpRecord :
searchedKey = 'name'
if searchedKey in nestedEmpRecord :
	print( 'key found in dictionary with value as ', searchedKey)
else :
	print(searchedKey, ' keys exists')

print('Total records :', len( nestedEmpRecord))
if len( nestedEmpRecord) == 0 :
	print( 'empty')
elif len( nestedEmpRecord) == 1 :
	print( 'only 1 record')
else :
	print( len( nestedEmpRecord), ' record(s) found')

# Alternate options to check for existing keys
#a) Using key (but with a default)
keyValue= nestedEmpRecord.get('garbage', -999)
print('\n nestedEmpRecord[\'garbage\'] :', keyValue)

#b) if/else expression form
# Get the value if 'garbage' exists as key in dict, else return -999
keyValue= nestedEmpRecord['garbage'] if 'garbage' in nestedEmpRecord else '-999'
if keyValue == '-999' :
	print('retured default value, key doesn\'t exists')
else :
	print('key exists, value :', nestedEmpRecord['garbage'])


# ordering dictionaries using keys
# OPTION -1 : get keys, create list, sort and get values for sorted keys
print('nestedEmpRecord.keys() :', nestedEmpRecord.keys()) # dict_keys(['skillFamily', 'name', 'roles'])
#print(type(nestedEmpRecord.keys())) # <class 'dict_keys'>

keysList = list(nestedEmpRecord.keys()) 
print('\n UnSorted dict keys:', keysList) #  ['skillFamily', 'name', 'roles']
keysList.sort()
print('\n Sorted dict keys:', keysList) # ['name', 'roles', 'skillFamily']

for k in keysList:
	print(k, '=>', nestedEmpRecord[k])
	

# OPTION -2 : newer sorted built-in function
print('\n sorting dict keys using sorted built-in function')
print('nestedEmpRecord :', nestedEmpRecord)
for k in sorted(nestedEmpRecord):
	print(k, '=>', nestedEmpRecord[k])


