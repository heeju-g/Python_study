# -*- coding:utf-8 -*-

import pickle

file = open('test02.txt','rb')
#print(file.read())
#이렇게 언피클링 해줘야 제대로 읽어온다
score = pickle.load(file)
print(score)
print(type(score))
file.close()