import sys
import re
from pymongo import MongoClient
from pprint import pprint
import os

# client.drop_database(name_or_database='ds2') # 기존에 있는 ds2 database 없애기
# db.drop_collection(name_or_collection='pokedex')
# os.system('mongoimport -d ds2 -c pokedex dataset/pokedex.json') # 파이썬에서 shell을 통해 mongoimport 하기
# client.list_database_names() # database list 보기
# db.list_collection_names() # database에 있는 collection list 보기

client = MongoClient('127.0.0.1')
db = client.ds2
pokedex = db.pokedex
    

def problem_1(pokedex):
    wind_weak = []
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']

    # TODO:
    # Problem A
    
    # 약점 찾기
    # 오바람이 가지고 있는 3가지 포켓몬의 약점 찾기
    weaknesses = pokedex.find({'name': {'$in': wind_pokemon}}, 
                             {'id':1, 'name':1, 'spawn_time':1, 'type':1, 'weaknesses':1, '_id':0}).sort([('name', 1)])
    for item in weaknesses:
        wind_weak.append(item['weaknesses']) #   
    temp = wind_weak[0]
    for i in range(1, len(wind_weak)):
        temp = set(temp)&set(wind_weak[i]) # 공통 약점
    wind_weak = list(temp)
    
    
    strong = pokedex.find({'weaknesses': {'$in': wind_weak},  # 공통 약점
                                          'spawn_time': {'$gte': '20:00', '$lte': '24:00'}}, # 출몰 시간
    {'id':1, 'name':1, 'spawn_time':1, 'type':1, '_id':0}).sort([('name', 1)])

    for item in strong:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')


def problem_2(pokedex):
    # TODO:
    # Problem B
    final_pokemons = pokedex.find({'next_evolution': {'$exists': False}, 
                                   'candy_count': {'$exists': False}, 
                                   'candy':{'$ne': 'None'}},
        {'_id':0, 'id':1, 'name':1, 'prev_evolution':1, 'candy':1}).sort([('id', 1)])

    for pokemon in final_pokemons:
        candy, count = "", 0
        
        # TODO:
        n_prev = len(pokemon['prev_evolution'])
        for i in range(n_prev):
            pokemon_num = pokemon['prev_evolution'][i]['num']
            prev_pokemon = pokedex.find({'num': pokemon_num}, {'_id':0, 'candy_count':1})        
            for i in prev_pokemon:
                count = count+i['candy_count']

        print(pokemon['name'], end=' => ')
        print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))





def main(problem_type):
    client = MongoClient('127.0.0.1')
    db = client.ds2
    pokedex = db.pokedex

    if problem_type == 1:
        problem_1(pokedex)
    elif problem_type == 2:
        problem_2(pokedex)

    client.close()


if __name__ == '__main__':
    main(int(sys.argv[1]))

problem_1(pokedex)
problem_2(pokedex)



