from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client.ds2
enron = db.emails

raw_input = sys.argv[1]

# TODO:
# fill in the blank
enron.create_index([('subject',TEXT), ('text', TEXT)], {'weights':{'subject':2, 'text':1}})
s = raw_input.split('/')
di = dict()
for i in s:
    if ':' in i:
        cmd, ss = i.strip().split(':')
        if cmd == 'not':
            di.update(enron.find({'subject':{'$nin':[ss]}}))
        elif cmd == 'from':
            di.update(enron.find({'sender':ss}))
        elif cmd == 'to':
            di.update(enron.find({'to':ss}))
        elif cmd == 'sort':
            sort = ss
    else:
        searcher = i
        enron.find({'subject':{'$in':[searcher]}})


print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))
