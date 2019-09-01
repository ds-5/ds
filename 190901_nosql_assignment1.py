def pagination():
    # TODO:
    result = db.grades.find({}, {'_id':0}).skip(10).limit(10).sort('sid')
    # problem A

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

pagination()

def letter():
    # TODO:
    score_weight = {'quiz':0.2, 'homework':0.3, 'exam':0.5}
    for doc in collection.find():
        total = 0
        for data in doc['grades']:
            total += score_weight[data['type']] * data['score']
        letter = 'F'
        if total >= 90:
            letter = 'A'
        elif total >= 80:
            letter = 'B'
        elif total >= 70:
            letter = 'C'
        elif total >= 60:
            letter = 'D'
        collection.update_many({'sid':doc['sid']},
                               {'$set':{'letter': letter, 'total':total}},
                               upsert=True)
        
    result = collection.find({}, {'letter':1, 'sid':1, 'total':1, '_id':0}).sort('total',-1)
    
    # problem B

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

letter()

def perfect():
    # TODO:       
    for doc in collection.find():
        # score + 10
        if 'note' in doc or {'type':'exam', 'score':100} in doc['grades']:
            total = min(100, doc['total']+10)
            collection.update({'sid':doc['sid']}, {'$set':{'total':total}})

    total_min = collection.find_one(sort=[('total',1)])['total']
    total_max = collection.find_one(sort=[('total',-1)])['total']
    
    for doc in collection.find():
        percent = (doc['total'] - total_min) / (total_max - total_min) * 100
        letter = 'F'
        if percent >= 80:
            letter = 'A'
        elif percent >= 50:
            letter = 'B'
        elif percent >= 20:
            letter = 'C'
        elif percent >= 10:
            letter = 'D'
        doc['letter'] = letter
        del doc['grades']
        db.relative.insert_one(doc)
       
    result = db.relative.find({}, {'sid':1, 'letter':1, '_id':0}).sort('sid')
    # problem C
    
    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')
perfect()