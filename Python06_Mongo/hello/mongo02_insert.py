# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
db = client.test
collection = db.score

#res01 = collection.insert_one({'name':'재민','kor':56, 'eng':87, 'math':100})
#print(res01.inserted_id)
'''
res = collection.insert_many(
        [
            {'name':'홍길동','midterm':{'kor':'80','eng':'100','math':'50'},'final':{'kor':'50','eng':'90','math':'70'}},
            {'name':'이순신','midterm':{'kor':'90','eng':'80','math':'50'},'final':{'kor':'80','eng':'95','math':'85'}},
            {'name':'김선달','midterm':{'kor':'60','eng':'70','math':'70'},'final':{'kor':'85','eng':'100','math':'50'}},
            {'name':'강호동','midterm':{'kor':'60','eng':'40','math':'90'},'final':{'kor':'55','eng':'40','math':'40'}},
            {'name':'유재석','midterm':{'kor':'80','eng':'60','math':'100'},'final':{'kor':'100','eng':'70','math':'80'}},
           
        ]
    )
'''
#print(res.inserted_ids)

for doc in collection.find():
    print(doc)