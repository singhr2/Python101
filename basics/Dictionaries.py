# Dictionaries.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\StringDemo.py
# > python
# > exec(open('Dictionaries.py').read())

# known as mappings, unordered collections;
# collections of other objects, but they store objects by key instead of by relative position
# only mapping type in Python’s core objects set, are also mutable: like lists

# dictionaries are not sequences, they don’t maintain any dependable left-to-right order.
# left-to-right order of dictionary keys is scrambled.
# Mappings are not positionally ordered

'''
see also CollectionType.py
Internally, dictionaries are implemented as hash tables (data structures that support very fast retrieval).
Like lists, dictionaries store object references (not copies, unless you ask for them explicitly).
'''

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print('type(D) :', type(D))

# Fetch value of key 'food'
print('D[\'food\'] :', D['food'])

# Add 1 to 'quantity' value
print('<before> D :', D)
D['quantity'] += 1
print('<after> D :', D)


###
# To check what is dict()
another_dict=dict()
print(another_dict.items())
print(another_dict.values())

####
# Starting with empty dictionary
Developer1 = {}
Developer1['name'] = 'Ranbir'
Developer1['job family'] = 'Java'
print('\nDeveloper1 :', Developer1) #  {'name': 'Ranbir', 'job family': 'Java'}


####
# Two-item (name, age) dictionary
twoItemDict = {'name': 'Bob', 'age': 40}
print('twoItemDict :', twoItemDict) #{'name': 'Bob', 'age': 40}

dictUsingEquals = dict(name='Key01', code='E001')
print('dictUsingEquals :', dictUsingEquals) # {'name': 'Key01', 'code': 'E001'}



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
		'roles' : ['Developer', 'Designer', 'Architect'], # nested list
		'experience': 18,
		'address' :{
					'home': {'houseNo': '123', 'zipcode': 123123},
					'office':{'location':'icc','xtn':98989}
					}

	}

print('\n nestedEmpRecord :', nestedEmpRecord)
print('Name :', nestedEmpRecord['name'])
print('First Name :', nestedEmpRecord['name']['fName'])
print('Roles :', nestedEmpRecord['roles'])
print('2nd Roles :', nestedEmpRecord['roles'][1])
print('skillFamily :', nestedEmpRecord['skillFamily'])
print('Total addresses :', len(nestedEmpRecord['address']))
print('office addresses :', nestedEmpRecord['address']['office'])
print('home addresses :', nestedEmpRecord['address']['home'])
print('home zipcode :', nestedEmpRecord['address']['home']['zipcode'])


#Test for membership (key present test)
print('address present ? ', 'address' in nestedEmpRecord) #True
print('zipcode present ? ', 'zipcode' in nestedEmpRecord) #False
print('zipcode present ? ', 'zipcode' in nestedEmpRecord['address']) #False
print('zipcode present ? ', 'zipcode' in nestedEmpRecord['address']['home']) #True


print('Keys :', nestedEmpRecord.keys()) # dict_keys(['skillFamily', 'name', 'roles', 'experience', 'address'])

print('values :', nestedEmpRecord.values()) #dict_values(['java', {'lName': 'Singh', 'fName': 'Ranbir'}, ['Developer', 'Designer', 'Architect'], 18, {'home': {'houseNo': '123', 'zipcode': 123123}, 'office': {'location': 'icc', 'xtn': 98989}}])

#dict_items([('skillFamily', 'java'), ('name', {'lName': 'Singh', 'fName': 'Ranbir'}),
# ('roles', ['Developer', 'Designer', 'Architect']), ('experience', 18),
#('address', {'home': {'houseNo': '123', 'zipcode': 123123}, 'office': {'location': 'icc', 'xtn': 98989}})])
print('items :', nestedEmpRecord.items()) # all key+value tuples,


# If trying to use a variable that is not defined, error message is
# NameError: name 'copyOfNestedEmpRecordAddress' is not defined

# copy
copyOfNestedEmpRecordAddress=nestedEmpRecord['address'].copy()
print('copyOfNestedEmpRecordAddress :', copyOfNestedEmpRecordAddress)

# update
dummyDict={'keyX':'valueX', 'keyY':'valueY'}
dummyDict.update(copyOfNestedEmpRecordAddress)
# {'keyX': 'valueX', 'keyY': 'valueY', 'home': {'houseNo': '123', 'zipcode': 123123}, 'office': {'location': 'icc', 'xtn': 98989}}
print('dummyDict after update :', dummyDict)
copiedDict = dummyDict.copy()
# {'keyX': 'valueX', 'keyY': 'valueY', 'home': {'houseNo': '123', 'zipcode': 123123}, 'office': {'location': 'icc', 'xtn': 98989}}
print('copiedDict :', copiedDict)


# get : to get default value if nothing matches.
print('dummyDict.get(\'nonExistentKey\', \'000\') :', dummyDict.get('nonExistentKey', '000')) # 000
print('dummyDict.get(\'nonExistentKey\') :', dummyDict.get('nonExistentKey')) # None
if dummyDict.get('c') != None: print('present', dummyDict['c']) # nothing printed
if dummyDict.get('c') == None: print('not present') # not present

# -------  pop(key, default?),  popitem() -------
print('dummyDict :', dummyDict)

#KeyError: 'dummyKey'
#print('>>  dummyDict.pop(\'dummyKey\') :', dummyDict.pop('dummyKey'))
#KeyError: 'houseNo'
#print('>>  dummyDict.pop(\'houseNo\') :', dummyDict.pop('houseNo'))
print('>>  dummyDict.pop(\'keyX\') :', dummyDict.pop('keyX')) #valueX
print('>>  dummyDict :', dummyDict) #  {'keyY': 'valueY', 'home': {'houseNo': '123', 'zipcode': 123123}, 'office': {'location': 'icc', 'xtn': 98989}}
print('>>  dummyDict.popitem(\'home\') :', dummyDict.pop('home')) # {'keyY': 'valueY', 'office': {'location': 'icc', 'xtn': 98989}}
print('>>  dummyDict :', dummyDict) #
print('\n ---- >>>>')

#
dummyDict2={False:'OK', 1:'one', 2:'two'}
print('dummyDict2 :', dummyDict2) # {False: 'OK', 1: 'one', 2: 'two'}
dummyDict2={True:'1', 1:'OK', 2:'two'}

# ?? True == 1
print('dummyDict2 :', dummyDict2) #{True: 'OK', 2: 'two'}

# remove all items
D1={'key1':'value1', 'key2':'value2'}
print('D1 has ', D1.__sizeof__()) #120 ??
print('D1 has ', len(D1), ' items') # 2
D1.clear()
print('After clear(), D1 has ', len(D1), ' items') # 0

#Add another roles
nestedEmpRecord['roles'].append('Consultant') # Add one more job desc
print('nestedEmpRecord(after adding job) :', nestedEmpRecord)

#Numeric operator on values
print('experience :', nestedEmpRecord['experience'], ' Years')

nestedEmpRecord['experience']+=82
print('experience +82:', nestedEmpRecord['experience'], ' Years')
print('\n nestedEmpRecord :', nestedEmpRecord)


# Listing down objects created so far
print('\n dir() :', dir())


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


if not 'garbage' in nestedEmpRecord :
	print(' >>> there is no key in dictionar with key as garbage')

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
