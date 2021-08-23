# -*- coding:utf-8 -*-
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def root():
    html = '''
    <h1>get/post</h1>
    <a href='/test'>get</a>
    <form action='/test' method='post'>
        <input type='submit' value='post'>
    </form>
    '''
    return html

@app.route('/test',methods=['GET','POST'])
def hello_test():
    if request.method == 'POST':
        return '<h1 style="color:blue">request post</h1>'
    else:
        return '<h1 style="color:red">request get</h1>'

if __name__ == '__main__':
    app.run()

