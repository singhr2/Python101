#ReadingWritingJSONData.py
# Reference : Python's json module
# String data related functions (suffix s is for String ?): json.dumps() and json.loads()
#File related functions : json.dump() and json.load() to encode and decode JSON data

import json

company_info = {
    'name' : 'Etisalat',   'shares' : 100,  'price' : 542.23,
    'address' : { 'po box':'7878', 'location':'AUH', 'country':'UAE' }
}

# convert to JSON
json_str = json.dumps(company_info)
print(type(json_str)) #<class 'str'>

# read back
data = json.loads(json_str)
print(type(data)) #<class 'dict'>
print('data :', data)

#  ------ File related ----------
my_data_as_dict = {}
print('1 :', my_data_as_dict)  #{} <- empty dict

#referring specific key in dict
my_data_as_dict['references'] = []  # empty list
print('2a :', my_data_as_dict) # {'references': []}
print('2b :', my_data_as_dict['references']) # []
print('2c :', type(my_data_as_dict['references'])) # <class 'list'>

my_data_as_dict['references'].append({
    'name': 'Ranbir',
    'from': 'HP'
})
print('3 :', my_data_as_dict) # {'references': [{'name': 'Ranbir', 'from': 'HP'}]}

my_data_as_dict['references'].append({
    'name': 'Anshi',
    'from': 'MH'
})
print('4 :', my_data_as_dict) # {'references': [{'name': 'Ranbir', 'from': 'HP'}, {'name': 'Anshi', 'from': 'MH'}]}


#with open('reference_json_dump.txt', 'w') as outfile:
#    json.dump(my_data_as_dict, outfile)
json.dump(my_data_as_dict, open('reference_json_dump.txt', 'w'))

#loaded_data =json.load(open('reference_json_dump.txt'))
#json_dump_file_pointer = open('reference_json_dump.txt', 'r')
#json.load(json_dump_file_pointer)
#print('type(loaded_data) :', type(loaded_data))

''' [OK]
with open('reference_json_dump.txt') as json_file:
    data = json.load(json_file)
    print(data) # {'references': [{'name': 'Ranbir', 'from': 'HP'}, {'name': 'Anshi', 'from': 'MH'}]}
    print(type(data)) #<class 'dict'>
    for p in data['references']:
        print('name: ' + p['name'])
        print('from: ' + p['from'])
        print('')
'''
loaded_data = json.load(open('reference_json_dump.txt', 'r'))
print('loaded_data :', loaded_data) #{'references': [{'name': 'Ranbir', 'from': 'HP'}, {'name': 'Anshi', 'from': 'MH'}]}
print('type(loaded_data) :',type(loaded_data)) # <class 'dict'>
for rec in loaded_data['references'] :
    print('name: ' + rec['name'] + ', from: ' + rec['from'])
