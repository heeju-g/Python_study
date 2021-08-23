# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do'

resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

inner_value = soup.find_all(class_='inner_value')

result = '국내발생 : {} 해외유입 : {} 소계 : {}'.format(inner_value[1].text,inner_value[2].text,inner_value[0].text.split(' ')[1])
print(result)