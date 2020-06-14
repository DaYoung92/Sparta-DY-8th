from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order_create():
    # pass #파이썬 문법: 이게 뜨면 무시하고 지나가라는 뜻
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    db.candle.insert_one({
        'name':name_receive,
        'count':count_receive,
        'address':address_receive,
        'phone':phone_receive
    })

    return jsonify({'result':'success'})

@app.route('/order', methods=['GET'])
def order_retreive():
    orders = list(db.candle.find({},{'_id':False}))

    return jsonify({
        'result':'success',
        'orders': orders
    })

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


