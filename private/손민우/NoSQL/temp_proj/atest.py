from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client.ds2
col = db.enron
result = col.find()

to_array=[]
from_array=[]
not_array=[]
sort_array=[]
none_array=[]

raw_input = sys.argv[1]
raw_input = raw_input.replace(' ','')

input = raw_input.split('/')
for i in range(len(input)):
    keyword = input[i].split(':')
    if keyword[0] == 'to':
        to_array = keyword[1].split(',')
    elif keyword[0] == 'from':
        from_array = keyword[1]
    elif keyword[0] == 'not':
        not_array = keyword[1].split(',')
    elif keyword[0] == 'sort':
        sort_array = keyword[1]
    else:
        none_array = keyword[0].split(',')

col.drop_indexes()
col.create_index( [('subject', TEXT), ('text', TEXT)], weights = {'subject':2, 'text':1} )

condition = ''
for i in range(len(none_array)):
    condition = condition + ' ' + str(none_array[i])

for j in range(len(not_array)):
    condition = condition + ' -' + str(not_array[j])

kw = {'$match' : {'$text' : {'$search' :condition, '$caseSensitive': False}}}
to = {'$match' : {'to' : {'$in' : to_array} } }
sender = {'$match' : {'sender' : from_array}}
sort_1 = {'$sort' : { 'score' : {'$meta' : 'textScore'}}}
sort_2 = {'$sort' : {'date':-1}}

query = []

if len(none_array) > 0:
    query.append(kw)
if len(from_array) > 0:
    query.append(sender)
if len(to_array) > 0:
    query.append(to)
if len(none_array) > 0:
    query.append(sort_1)
if len(sort_array) > 0:
    query.append(sort_2)

result = col.aggregate(query)

print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))
client.close()

