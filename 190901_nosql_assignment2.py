def problem_1(pokedex):
    wind_weak = []
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']

    # TODO:
    # wind_weak
    cursor = pokedex.find({'name':{'$in':wind_pokemon}})
    wind_weaknesses = set(cursor.next()['weaknesses'])
    for doc in cursor:
        wind_weaknesses &= set(doc['weaknesses'])
    wind_weak.extend(list(wind_weaknesses))
    
    # Problem A
    strong = pokedex.find({'type':{'$in':wind5_weaknesses},'spawn_time':{'$regex':'2\d:'}},
                             {'_id':0, 'id':1, 'name':1, 'spawn_time':1,'type':1}
                            ).sort([('name',1)])

    for item in strong:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')


def problem_2(pokedex):
    # TODO:
    # Problem B
    final_pokemons = pokedex.find({'next_evolution':{'$exists':0},
                                   'prev_evolution':{'$exists':1}
                                  }).sort([('id',1)])
    ######

    for pokemon in final_pokemons:
        candy, count = "", 0
        
        # TODO:
        for prev_pokemon in pokemon['prev_evolution']:
            prev_pokemon_info = pokedex.find_one({'num':prev_pokemon['num']})
            candy = prev_pokemon_info['candy']
            count += prev_pokemon_info['candy_count']
        ######

        print(pokemon['name'], end=' => ')
        print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))

problem_2(collection)