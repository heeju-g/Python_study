# -*- coding:utf-8 -*-

# pip instal beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
#print(resp)
soup = BeautifulSoup(resp,'html.parser')
#응답받은 데이터(doc)
#print(soup)

#movies = soup.find_all('dl', class_ = 'lst_dsc')
#print(movies)

#movies 안에 있는 제목과 별점을 파싱해서 
# 제목[별점]으로 반복해서 출력하자
movies = soup.find_all('dl', class_ = 'lst_dsc')
for movie in movies:
    #print(movie)
    title = movie.find('a').text 
    star = movie.find('span',class_='num').text 
    print('{}[{}]'.format(title,star))
    
    
    
    
    
    
    
    