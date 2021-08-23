# -*- coding:utf-8 -*-

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import flask_cors


app = Flask(__name__)
flask_cors.CORS(app)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/crawling')
def result_json():
    # https://movie.naver.com/movie/running/current.nhn
    # 제목, 별점을 {'title':제목, 'star':별점} 형태로 크롤링하여
    # {'movies':[{},{},{},,,]}형태로 json 객체를 만들어 리턴
    url = 'https://movie.naver.com/movie/running/current.nhn'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    movies = soup.find_all('dl', class_ = 'lst_dsc')
    
    movielist = list()
    
    for movie in movies:
        ''' title = movie.find('a').text 
        star = movie.find('span',class_='num').text 
        tmp = {}
        tmp['title']=title
        tmp['star']=star 
        movielist.append(tmp)
     
    res = {}
    res['movies']=movielist 
    res_json = json.dumps(res,ensure_ascii=False)
    return res_json
    '''
        res = dict()
        res['title']= movie.find('a').text 
        res['star']= movie.find('span',class_='num').text
        movielist.append(res)
    result_dict = {'movies':movielist}
    result_json = json.dumps(result_dict, ensure_ascii=False)
    return result_json

if __name__ == '__main__':
    app.run(host='localhost',port='8686')
    
    