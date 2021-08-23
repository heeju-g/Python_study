# -*- coding:utf-8 -*-
from pymongo import MongoClient

client= MongoClient('mongodb://localhost:27017')
test = client['test']
score = test['score']

res01 = score.update_one(
        {'name':'조세호'},
        {'$set':{'mat':13}}
    )
print(res01.matched_count)
print(res01.modified_count)

print('------------')

res02 = score.update_many(
        {'eng':{'$lte':70}},
        {'$set':{'eng':0}}
    )
print(res02.matched_count)
print(res02.modified_count)








