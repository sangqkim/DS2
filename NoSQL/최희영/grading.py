from pymongo import MongoClient
import sys

client= MongoClient()
db = client.ds2
grades = db.grades

def pagination(page):
    result = grades.find({},{'_id':0, 'grades':1, 'sid':1}).sort([('sid',1)]).skip(10*(page-1)).limit(10)

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def letter():
    for i in range(100):
        each = grades.find_one({'sid': i, 'grades.type':'quiz'},{'grades.$':1, '_id':0})
        quiz_score = each['grades'][0]['score']
        each = grades.find_one({'sid': i, 'grades.type': 'homework'}, {'grades.$': 1, '_id': 0})
        hw_score = each['grades'][0]['score']
        each = grades.find_one({'sid': i, 'grades.type': 'exam'}, {'grades.$': 1, '_id': 0})
        exam_score = each['grades'][0]['score']

        total_score = quiz_score*0.2 + hw_score*0.3 + exam_score*0.5

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

        grades.update_one({'sid':i}, {'$set':{'total':total_score, 'letter':grade}})

    result = grades.find({}, {'letter':1, 'sid':1, 'total':1, '_id':0}).sort([('total',-1)])
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')


def perfect():
    relative = db.relative

    lst = []
    for i in range(100):
        flag = False
        each = grades.find_one({'sid': i, 'grades.type': 'quiz'}, {'grades.$': 1, '_id': 0})
        quiz_score = each['grades'][0]['score']
        each = grades.find_one({'sid': i, 'grades.type': 'homework'}, {'grades.$': 1, '_id': 0})
        hw_score = each['grades'][0]['score']
        each = grades.find_one({'sid': i, 'grades.type': 'exam'}, {'grades.$': 1, '_id': 0})
        exam_score = each['grades'][0]['score']

        total = quiz_score * 0.2 + hw_score * 0.3 + exam_score * 0.5

        each2 = grades.find_one({'sid': i}, {'_id': 0})

        if exam_score == 100:
            flag = True
        try:
            if each2['note']:
                flag = True

        except:
            pass

        if flag:
            if total > 90:
                total = 100
            else:
                total += 10

        lst.append(total)
        relative.insert_one({'sid': i, 'total': total})

    val_min = min(lst)
    val_max = max(lst)
    for i in range(100):
        each = relative.find_one({'sid': i})
        total = each['total']
        score = (total - val_min) / (val_max - val_min) * 100
        if score >= 80:
            grade = 'A'
        elif score >= 50:
            grade = 'B'
        elif score >= 20:
            grade = 'C'
        elif score >= 10:
            grade = 'D'
        else:
            grade = 'F'
        relative.update_one({'sid': i}, {'$set': {'letter': grade}})

    result = relative.find({}, {'letter': 1, 'sid': 1, '_id': 0}).sort([('sid', 1)])
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2
    grades = db.grades

    num = int(sys.argv[1])

    try:
        if num == 1:
            page = int(sys.argv[2])
            pagination(page)
        elif num == 2:
            letter()
        elif num == 3:
            perfect()
    except:
        print("ERROR")
    client.close()
