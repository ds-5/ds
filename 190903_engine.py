from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client.ds2
enron = db.enron

raw_input = sys.argv[1]

############################### TODO:
enron.drop_indexes()
enron.create_index([("subject","text"), ("text","text")], weights={"subject":2, "text":1})

doc_search = {"$text":{"$search":"", '$caseSensitive':False, '$language':'en'}}
sort_key = ''
for keyword in raw_input.split('/'):
    keyword = ''.join(keyword.split(' '))
    i = keyword.find(':')
    if i<0: # search
        doc_search["$text"]["$search"] = '"' + '""'.join(keyword.split(',')) + '"' + doc_search["$text"]["$search"]
    elif i>=0 and keyword[:i] == 'not':
        doc_search["$text"]["$search"] += ' -' + ' -'.join(keyword[i+1:].split(','))
    elif i>=0 and keyword[:i] == 'from':
        doc_search["sender"] = keyword[i+1:]
    elif i>=0 and keyword[:i] == 'to':
        doc_search["to"] = {"$in":keyword[i+1:].split(',')} 
    elif i>=0 and keyword[:i] == "sort":
        sort_key = keyword[i+1:]

if not doc_search['$text']['$search']:
    del doc_search['$text']
    
if sort_key == 'score':
    result = enron.find(doc_search, {'score':{'$meta':'textScore'}}).sort([('score', {'$meta':'textScore'})])
elif sort_key == 'date':
    result = enron.find(doc_search).sort([('date',-1)])
else:
    result = enron.find(doc_search)

############################### END

print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))
