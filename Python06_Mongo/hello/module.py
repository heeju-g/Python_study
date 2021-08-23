# -*- coding:utf-8 -*-

#pip install pymongo

from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017')
client = MongoClient('localhost',27017)
client = MongoClient('192.168.10.3',27017)

db = client.test
#db = client['test']
collection = db.score
#collection = db['score']

result = collection.find()
#print(result)
for res in result:
    print(res)