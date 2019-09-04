from pymongo import MongoClient
import sys

def pagination(col):
    # problem A
    result = col.find({},{'_id':0, 'grades':1, 'sid':1}).sort([('sid', 1)]).skip(10).limit(10)
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def letter(col):
    # problem B
    for i in range(100):
        each = col.find_one({'sid': i, 'grades.type':'quiz'},{'grades.$':1, '_id':0})
        quiz_score = each['grades'][0]['score']
        quiz_score *= 0.2
        each = col.find_one({'sid': i, 'grades.type': 'homework'}, {'grades.$': 1, '_id': 0})
        hw_score = each['grades'][0]['score']
        hw_score *= 0.3
        each = col.find_one({'sid': i, 'grades.type': 'exam'}, {'grades.$': 1, '_id': 0})
        exam_score = each['grades'][0]['score']
        exam_score *= 0.5

        total_score = quiz_score + hw_score + exam_score
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

        col.update_one({'sid':i}, {'$set':{'total':total_score, 'letter':grade}})

    result = col.find({}, {'letter':1, 'sid':1, 'total':1, '_id':0}).sort([('total',-1)])
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def perfect(col, db):

    # problem C
    check = db.list_collection_names()
    if 'relative' in check:
        db.drop_collection('relative')
    col2 = db.relative
    lst = []
    for i in range(100):
        flag = False
        each = col.find_one({'sid': i, 'grades.type': 'quiz'}, {'grades.$': 1, '_id': 0, 'note':1})
        quiz_score = each['grades'][0]['score']
        r_quiz_score = quiz_score * 0.2
        each = col.find_one({'sid': i, 'grades.type': 'homework'}, {'grades.$': 1, '_id': 0, 'note':1})
        hw_score = each['grades'][0]['score']
        r_hw_score = hw_score * 0.3
        each = col.find_one({'sid': i, 'grades.type': 'exam'}, {'grades.$': 1, '_id': 0, 'note':1})
        exam_score = each['grades'][0]['score']
        r_exam_score = exam_score * 0.5

        total = r_quiz_score + r_hw_score + r_exam_score
        if exam_score == 100:
            flag = True
        try:
            if each['note']:
                flag = True
        except:
            pass

        if flag:
            if total > 90:
                total = 100
            else:
                total += 10
        lst.append(total)
        col2.insert_one({'sid': i, 'total': total})

    val_min = min(lst)
    val_max = max(lst)
    for i in range(100):
        each = col2.find_one({'sid':i})
        total = each['total']
        score = (total - val_min)/(val_max - val_min) * 100
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
        col2.update({'sid':i}, {'$set':{'letter':grade}})
    result = col2.find({},{'letter':1, 'sid':1, '_id':0}).sort([('sid', 1)])
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2

    # raw_input = sys.argv[1]
    # TODO:
    col = db.grades
    # letter(col)
    perfect(col, db)
    # if raw_input == 'A':
    #     pagination(col)
    # elif raw_input == 'B':
    #     letter(col)
    # elif raw_input == 'C':
    #     perfect(col)
    client.close()
