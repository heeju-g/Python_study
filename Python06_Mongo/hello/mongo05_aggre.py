# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost',27017)
test = client.test
score = test.score



#math 점수가 20보다 큰 document들의 math평균을 구해서 {'_id':'math','average':평균}출력
aggre = score.aggregate(
        [
            {'$match':{'math':{'$gt':20}}},
            {'$group':{'_id':'math','average':{'$avg':'$math'}}}
        
        ]
    )
print(aggre)
print(list(aggre)[1])
