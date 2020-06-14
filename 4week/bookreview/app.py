from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # 클라이언트에서 받아온 값을 MongoDB 에 저장
    db.bookreview.insert_one({
        'title' : title_receive,
        'author': author_receive,
        'review': review_receive
    })
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    # MongoDB에서 _id 제외한 모든 데이터를 조회한다
    reviews = list(db.bookreview.find({},{'_id': False}))
    # Dictionary에 데이터를 담아서 올림
    data = {
        'result': 'success',
        'reviews': reviews,

    }
    return jsonify(data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)