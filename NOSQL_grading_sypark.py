from pymongo import MongoClient
from pprint import pprint
import sys
import os

#!mongoimport -d ds2 -c grades assignment-dataset/dataset/grades.json

def pagination():
    # TODO:
    # problem A
    # result = db.grades.find({'sid':{'$gte':10}},{'_id':0, 'note':0}).sort([('sid',1)]).limit(10)
    result = db.grades.find({},{'_id':0, 'note':0}).sort([('sid',1)]).limit(10).skip(10)

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def letter():
    # TODO:
    # problem B
    all_l = db.grades.find() #list
    for sid_d in all_l:
        tot = 0
        for map_d in sid_d['grades']:
            #print(map_d)
            #print(t_l['score'])
            if map_d['type'] == 'quiz' : tot += 0.2*int(map_d['score'])
            if map_d['type'] == 'homework' : tot += 0.3*int(map_d['score'])
            if map_d['type'] == 'exam' : tot += 0.5*int(map_d['score'])
        
        if tot >= 90 : let = 'A'
        elif tot >= 80 : let = 'B'
        elif tot >= 70 : let = 'C'
        elif tot >= 60 : let = 'D'
        else : let = 'F'
        #print(let)
        #print(tot)
        db.grades.update_one({'sid':sid_d['sid']}, {'$set' : {'letter':let, 'total':tot}})
    #for item in result:
    
    result = db.grades.find({},{'_id':0, 'letter':1,'sid':1, 'total':1}).sort([('total', -1)])
    #pprint(result)
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def perfect():
    # TODO:
    # problem C

    all_l = db.grades.find() #list
    for sid_d in all_l:
        tot = 0
        for map_d in sid_d['grades']:
            if map_d['type'] == 'quiz' : tot += 0.2*map_d['score']
            if map_d['type'] == 'homework' : tot += 0.3*map_d['score']
            if map_d['type'] == 'exam' : tot += 0.5*map_d['score']
        db.grades.update_one({'sid':sid_d['sid']}, {'$set' : {'total':tot}})
    
    #pprint(list(db.grades.find()))
    db.grades.update_many({'$or': [{'note':{'$exists':1}}, {'grades.type':'exam', 'grades.score':100}]},{'$inc':{'total':10}})
    db.grades.update_many({'total':{'$gt':100}}, {'$set' : {'total':100}})
    #pprint(list(db.grades.find()))
    db.relative.drop()
    db.create_collection('relative')
    all_let = db.grades.find() #list
    
    tot_min = 100
    tot_max = 0
    for sid_d in all_let:
        if sid_d['total'] < tot_min :tot_min = sid_d['total']
        if sid_d['total'] > tot_max :tot_max = sid_d['total']
    
    #print(tot_min, tot_max)
    all_let = db.grades.find() #list
    for sid_d in all_let:
        x = (sid_d['total']-tot_min)/(tot_max-tot_min)*100
        #print(x)
        if x >= 80 : let = 'A'
        elif x >= 50: let = 'B'
        elif x >= 20 : let = 'C'
        elif x >= 10 : let = 'D'
        else : let = 'F'
        db.relative.insert_one({'sid':sid_d['sid'], 'total':sid_d['total'], 'letter':let})
    
    result = db.relative.find({},{'_id':0, 'letter':1,'sid':1}).sort([('sid', 1)])
    
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2
    db.grades.drop()
    os.system('mongoimport -d ds2 -c grades assignment-dataset/dataset/grades.json')
    raw_input = sys.argv[1]

    if raw_input == '1': pagination()
    elif raw_input == '2' : letter()
    elif raw_input == '3': perfect()
