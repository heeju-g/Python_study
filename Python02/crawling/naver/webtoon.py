# -*- coding:utf-8 -*-

#pip install requests
from bs4 import BeautifulSoup
import requests
import json


url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=thu'

resp = requests.get(url)
#print(resp.text) 얘는 문자열
#soup를 써서 객체화된 형태로 해서 원하는 거 가져올 수 있도록
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

#제목[별점]형태로 출력
img_list = soup.find('ul',class_='img_list')
webtoons = img_list.select('dl')
lst = list()
for webtoon in webtoons:
    title = webtoon.find('a')['title']
    #title = webtoon.find('dt').text 
    star = webtoon.find('strong').text
    #print('{} [{}]'.format(title,star))
    tmp = {}
    tmp['title']=title
    tmp['star']=star 
    lst.append(tmp)
#print(lst)
#딕셔너리 형태에서 json형태로 바꾸기
res = {}
res['webtoons']=lst 
res_json = json.dumps(res,ensure_ascii=False)
#print(res_json)
with open('webtoons.json','w',encoding='utf-8') as f:
    f.write(res_json)
    
