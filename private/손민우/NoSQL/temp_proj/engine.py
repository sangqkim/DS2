from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client.ds2
enron = db.emails

# raw_input = sys.argv[1]
raw_input = "Social / not: Network / sort: date"
# raw_input = "from: robyn@layfam.com"
# raw_input = "to: cindy.olson@enron.com, greg.whalley@enron.com / Please / not: Attached, previously"
# fill in the blank
enron.create_index([('subject',TEXT), ('text', TEXT)], weights = {'subject':2, 'text':1})
s = raw_input.split('/')
lnot, lfrom, lto, lsearch, lsort = [], [], [], [], []

for i in s:
    cmd = i.replace(" ", "").split(':')
    if cmd[0] == 'not':
        lnot.extend(cmd[1].split(','))
    elif cmd[0] == 'from':
        lfrom.append(cmd[1])
    elif cmd[0] == 'to':
        lto.extend(cmd[1].split(','))
    elif cmd[0] == 'sort':
        lsort.append(cmd[1])
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
    sender = {'$match': {'sender': lfrom[0]}}
    query.append(sender)
if lsort:
    if lsort[0] == 'score':
        sort = {'$sort': {'score': {'$meta': 'textScore'}}}
    elif lsort[0] == 'date':
        sort = {'$sort': {'date': -1}}
    query.append(sort)

result = enron.aggregate(query)
print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))
