import sys
import re
from pymongo import MongoClient


def problem_1(pokedex):
    wind_weak = []
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']

    # TODO:
    cur = pokedex.find({'name': {'$in': wind_pokemon}})
    weak = set()
    for i in cur:
        for dd in i['weaknesses']:
            weak.add(dd)
    weak = list(weak)
    strong = pokedex.find({'type': {'$in': weak}, 'spawn_time': {'$gte': '20:00', '$lte': '24:00'}},{'id':1, 'name':1, 'spawn_time':1, 'type':1, '_id':0}).sort([('name', 1)])

    for item in strong:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')


def problem_2(pokedex):
    # TODO:
    # Problem B
    final_pokemons = ...

    for pokemon in final_pokemons:
        candy, count = "", 0
        
        # TODO:

        print(pokemon['name'], end=' => ')
        print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))


def main(problem_type):
    client = MongoClient('127.0.0.1')
    db = client.ds2
    pokedex = db.pokedex
    problem_1(pokedex)
    # if problem_type == 1:
    #     problem_1(pokedex)
    # elif problem_type == 2:
    #     problem_2(pokedex)

    client.close()


if __name__ == '__main__':
    # main(int(sys.argv[1]))
    main(1)
