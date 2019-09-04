from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client.ds2
enron = db.emails

raw_input = sys.argv[1]
# fill in the blank

s = raw_input.split('/')
lnot, lto, lsearch, lsort, lfrom = [], [], [], '', ''

for i in s:
    cmd = i.replace(" ", "").split(':')
    if cmd[0] == 'not':
        lnot.extend(cmd[1].split(','))
    elif cmd[0] == 'from':
        lfrom = cmd[1]
    elif cmd[0] == 'to':
        lto.extend(cmd[1].split(','))
    elif cmd[0] == 'sort':
        lsort = cmd[1]
    else:
        lsearch.extend(cmd[0].split(','))

query = []
if lnot or lsearch:
    text = ''
    for i in lsearch:
        text = text + ' ' + str(i)
    for i in lnot:
        text = text + ' -' + str(i)
    search = {'$match': {'$text': {'$search': text, '$caseSensitive': False, '$language': 'en'}}}
    query.append(search)
if lto:
    to = {'$match': {'to': {'$in': lto}}}
    query.append(to)
if lfrom:
    sender = {'$match': {'sender': lfrom}}
    query.append(sender)
if lsort:
    if lsort == 'score':
        sort = {'$sort': {'score': {'$meta': 'textScore'}}}
    elif lsort == 'date':
        sort = {'$sort': {'date': -1}}
    else:
        print('You can sort by only date or score')
        raise(AssertionError)
    query.append(sort)

enron.create_index([('subject',TEXT), ('text', TEXT)], weights = {'subject':2, 'text':1})
result = enron.aggregate(query)

print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))
