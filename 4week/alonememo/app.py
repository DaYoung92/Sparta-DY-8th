from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    memos = list(db.alonememo.find({}, {'_id': False}))

    return jsonify({'result':'success', 'articles':memos})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
		# 2. meta tag를 스크래핑하기
		# 3. mongoDB에 데이터 넣기
        url_receive = request.form['url_give']
        comment_receive = request.form['comment_give']

        	# meta tag를 스크래핑 하는 부분
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)

        response = requests.get(url_receive)
        soup = BeautifulSoup(response.text, 'html.parser') 
        # og 태그 : url 공유할 때 자동으로 뜨는 미리보기 형식. title, img, desc가 있다.

        title_tag = soup.select_one('meta[property="og:title"]')
        desc_tag = soup.select_one('meta[property="og:description"]')
        img_tag = soup.select_one('meta[property="og:image"]')

        title = title_tag['content'] #title_tag에 저장된 메타 태그의 'content' 속성값을 긁어온다.
        desc = desc_tag['content']
        img = img_tag['content']
        
        
        db.alonememo.insert_one({
            'title' : title,
            'description': desc,
            'image': img,
            'url' : url_receive,
            'comment' : comment_receive
            })
            
        return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)