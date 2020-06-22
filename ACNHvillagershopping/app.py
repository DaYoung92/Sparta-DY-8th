from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port= 27017)
db = client.acnhDB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/search', methods=['GET'])
def villager_search():
    name_receive = request.args.get('name_give')

    villager = db.Villagers.find_one({'name':name_receive},{'_id':False})
    

    return jsonify({
        'result':'success',
        'villager':villager
    })

@app.route('/api/sellTableSet', methods=['GET'])
def sellTableSet():
    all_sells = list(db.SellArticle.find({},{'password':False, 'note':False}))
    
    results = []
    for sell in all_sells:
        object_id = sell['_id']
        sell.update({
            '_id': str(object_id)
        })
        results.append(sell)

    return jsonify({
        'result':'success',
        'sellArticles':results
    })

@app.route('/api/buyTableSet', methods=['GET'])
def buyTableSet():
    all_buys = list(db.BuyArticle.find({},{'password':False, 'note':False}))

    results = []
    for buy in all_buys:
        object_id = buy['_id']
        buy.update({
            '_id': str(object_id)
        })
        results.append(buy)
    
    return jsonify({
        'result':'success',
        'buyArticles':results
    })
    

@app.route('/api/SellArticleNew', methods=['POST'])
def sellArticleNew():
    name_receive = request.form['name_give']
    price_receive = request.form['price_give']
    pricetype_receive = request.form['pricetype_give']
    address_receive = request.form['address_give']
    password_receive = request.form['password_give']
    note_receive = request.form['note_give']
    time_receive = request.form['time_now']

    db.SellArticle.insert_one({
        'name':name_receive,
        'price':price_receive,
        'pricetype':pricetype_receive,
        'address':address_receive,
        'password':password_receive,
        'note':note_receive,
        'time':time_receive
    })

    return jsonify({'result':'success'})


@app.route('/api/BuyArticleNew', methods=['POST'])
def buyArticleNew():
    name_receive = request.form['name_give']
    price_receive = request.form['price_give']
    pricetype_receive = request.form['pricetype_give']
    address_receive = request.form['address_give']
    password_receive = request.form['password_give']
    note_receive = request.form['note_give']
    time_receive = request.form['time_now']

    db.BuyArticle.insert_one({
        'name':name_receive,
        'price':price_receive,
        'pricetype':pricetype_receive,
        'address':address_receive,
        'password':password_receive,
        'note':note_receive,
        'time':time_receive
    })

    return jsonify({'result':'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)