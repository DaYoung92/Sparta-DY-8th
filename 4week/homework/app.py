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
@app.route('/purchase', methods=['POST'])
def write_purchases():
    name_receive = request.form['name_give']
    qty_receive = request.form['qty_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']


    # 클라이언트에서 받아온 값을 MongoDB 에 저장
    db.tentpurchase.insert_one({
        'name' : name_receive,
        'qty': qty_receive,
        'address': address_receive,
        'phone' : phone_receive
    })
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/purchase', methods=['GET'])
def read_purchases():
    # MongoDB에서 _id 제외한 모든 데이터를 조회한다
    purchases = list(db.tentpurchase.find({},{'_id': False}))
    # Dictionary에 데이터를 담아서 올림
    data = {
        'result': 'success',
        'purchases': purchases

    }
    return jsonify(data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)