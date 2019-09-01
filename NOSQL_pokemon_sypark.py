import sys
import re 
from pymongo import MongoClient 
from pprint import pprint 
import os

def problem_1(pokedex): 
    wind_weak = [] 
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']
    
    # TODO:
    #pprint(list(pokedex.find({'name':{'$in':wind_pokemon}})))
    wind_p = pokedex.find({'name':{'$in':wind_pokemon}})
    for find_p in wind_p:
        if wind_weak == [] : wind_weak = find_p['weaknesses']
        else : wind_weak = list(set(wind_weak)&set(find_p['weaknesses']))
    #print(wind_weak)

    # Problem A
    strong = pokedex.find({'type':{'$in':wind_weak}, 'spawn_time':{'$regex' : '^2'}}, 
                          {'_id':0, 'id':1, 'name':1, 'spawn_time':1, 'type':1}).sort([('name',1)])
    #print(strong)
    for item in strong:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def problem_2(pokedex):
    # TODO:
    # Problem B
    final_pokemons = pokedex.find({'next_evolution':{'$exists':0}}).sort([('id',1)])
    #pprint(list(final_pokemons))
    # TODO:
    for pokemon in final_pokemons:
        candy, count = "", 0
        #print(pokemon['prev_evolution'])
        candy = pokemon['candy']
        pre_poke_cnt = pokedex.find({'next_evolution.name':pokemon['name']}).count()
        #print(pre_poke_cnt)
        if pre_poke_cnt != 0 :
            pre_poke = pokedex.find({'next_evolution.name':pokemon['name']})  
            for poke in pre_poke:
                candy = poke['candy']
                count += int(poke['candy_count'])
            print(pokemon['name'], end=' => ')
            print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))

def main(problem_type): 
    client = MongoClient('127.0.0.1') 
    db = client.ds2 
    db.pokedex.drop() 
    os.system('mongoimport -d ds2 -c pokedex assignment-dataset/dataset/pokedex.json') 
    pokedex = db.pokedex

    if problem_type == 1:
        problem_1(pokedex)
    elif problem_type == 2:
        problem_2(pokedex)

    client.close()

if __name__ == "__main__":
    main(int(sys.argv[1]))
