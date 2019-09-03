import sys
import re
from pymongo import MongoClient


def problem_1(pokedex):
    wind_weak = []
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']

    cur = pokedex.find({'name': {'$in': wind_pokemon}})
    for i in cur:
        wind_weak.append(set(i['weaknesses']))

    weak = list(wind_weak[0] & wind_weak[1] & wind_weak[2])
    strong = pokedex.find({'type': {'$in': weak}, 'spawn_time': {'$gte': '20:00', '$lte': '24:00'}},
                          {'id':1, 'name':1, 'spawn_time':1, 'type':1, '_id':0}).sort([('name', 1)])

    for item in strong:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')


def problem_2(pokedex):
    # Problem B
    final_pokemons = pokedex.find({'next_evolution':{'$exists':False}, 'prev_evolution':{'$exists':True}})\
        .sort([('id', 1)])

    for pokemon in final_pokemons:
        candy, count = "", 0
        for i in pokemon['prev_evolution']:
            find_num = i['num']
            each = pokedex.find_one({'num':find_num})
            candy = each['candy']
            count += each['candy_count']
        print(pokemon['name'], end=' => ')
        print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))


def main(problem_type):
    client = MongoClient('127.0.0.1')
    db = client.ds2
    pokedex = db.pokedex
    problem_1(pokedex)
    # problem_2(pokedex)
    # if problem_type == 1:
    #     problem_1(pokedex)
    # elif problem_type == 2:
    #     problem_2(pokedex)

    client.close()


if __name__ == '__main__':
    # main(int(sys.argv[1]))
    main(1)
