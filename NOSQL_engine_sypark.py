from pymongo import MongoClient, TEXT
from pprint import pprint
import sys
import os

client = MongoClient()
db = client.ds2
db.emails.drop() 
os.system('mongoimport -d ds2 -c emails assignment-dataset/dataset/emails.json') 
enron = db.emails

raw_input = sys.argv[1]
#raw_input = "Social/ not: Network / sort: date " #1
#raw_input = "from: robyn@layfam.com" #2
#raw_input = "to : cindy.olson@enron.com, greg.whalley@enron.com / Please /not:Attached,previously" #3

# TODO:
raw_input = raw_input.replace(' ', '')
text_feild = raw_input.split('/')
sort_f = ''
sender = ''
to_f = []
search_f = []

for str_one in text_feild:
    if 'not:' in str_one: 
        for word in str_one.split(':')[1].split(',') : search_f.append(' -'+word)
    elif 'sort:' in str_one:
        if 'score' in str_one : sort_f= [('score',dict([('$meta','textScore')]))]
        elif 'date' in str_one : sort_f= str_one.split(':')[1]
    elif 'from:' in str_one: sender = [('sender', str_one.split(':')[1])]
    elif 'to:' in str_one: to_f = [('to', dict([('$in', str_one.split(':')[1].split(','))]))]
    else : 
        for word in str_one.split(','): search_f.append(word)

#print(sort_f, sender, to_f, search_f)
#to or from
if sender == '' :
    if to_f == [] : search_find = ''
    else : search_find = dict(to_f)
else :
    if to_f == [] : search_find = dict(sender)
    else : search_find = dict(sender + to_f)
#text_search
search_text = ''
if search_f != [] :
    search_text_tmp = "\\\'"
    for one_ts in search_f:
        search_text_tmp = search_text_tmp + one_ts +'\\\''
        if one_ts != search_f[-1] : search_text_tmp = search_text_tmp + ' \\\''
    search_text = dict([('$text', dict([('$search', search_text_tmp), ('$caseSensitive',False), ('$language','en')]))])
 #sort
search_sort = ''
if isinstance(sort_f, list) : search_sort = dict(sort_f)
else : search_sort = sort_f  
    
#print(search_find, search_text, search_sort)    

enron.create_index([('subject',TEXT), ('text',TEXT)], weights = {'subject':2, 'text':1})

search_full = ''
if search_find != '' : 
    if search_text != '' : search_full = {**search_find, **search_text}
    else : search_full = search_find
else : 
    if search_text != '' : search_full = search_text

#print(search_full)

if search_sort == '' : result = enron.find(search_full)
else :
    if isinstance(sort_f, list) : result = enron.find(search_full, search_sort).sort(sort_f)
    else : result = enron.find(search_full).sort([(sort_f,-1)])

print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))
