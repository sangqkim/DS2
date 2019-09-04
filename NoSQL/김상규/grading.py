from pymongo import MongoClient
import sys
from pprint import pprint
#import os

#client.drop_database(name_or_database='ds2') # 기존에 있는 ds2 database 없애기
# db.drop_collection(name_or_collection='grades')
# os.system('mongoimport -d ds2 -c grades dataset/grades.json') # 파이썬에서 shell을 통해 mongoimport 하기
# client.list_database_names() # database list 보기
# db.list_collection_names() # database에 있는 collection list 보기


def pagination():
    # TODO:
    result = db.grades.find({'grades': {'$exists': True}}, {'grades':1, 'sid':1, '_id':0}).sort([('sid',1)]).limit(10).skip(10)
    # problem A

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def letter():
    # TODO:
    # problem B
    result = db.grades.find({'grades': {'$exists': True}}, {'grades':1, 'sid':1, '_id':0})
    for item in result:
        for i in range(len(item['grades'])):
            if item['grades'][i]['type'] == 'quiz':
                quiz_score = item['grades'][i]['score']*0.2
            elif item['grades'][i]['type'] == 'homework':
                homework_score = item['grades'][i]['score']*0.3
            elif item['grades'][i]['type'] == 'exam':
                exam_score = item['grades'][i]['score']*0.5
        total_score = quiz_score+homework_score+exam_score
        if total_score >= 90:
            grade = 'A'
        elif total_score >= 80:
            grade = 'B'
        elif total_score >= 70:
            grade = 'C'
        elif total_score >= 60:
            grade = 'D'
        else:
            grade = 'F'        
        db.grades.update_one({'sid': item['sid']}, {'$set': {'total': total_score, 'letter': grade}})
             
    result = db.grades.find({}, {'sid':1, 'total':1, 'letter':1, '_id':0}).sort([('total',-1)])

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

#def perfect():
#    # TODO:
#    # problem C
#
#    for item in result:
#        print('{ ', end='')
#        for (k, v) in sorted(item.items()):
#            print('{}:{}'.format(k, v), end=', ')
#        print('\b\b }')

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2

    raw_input = sys.argv[1]

    # TODO:

    client.close()

pagination()

letter()

#perfect()

