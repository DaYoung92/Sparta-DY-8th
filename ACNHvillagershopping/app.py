from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import datetime

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

    new_date = datetime.datetime.now().timestamp() * 1000
    calday = 24*60*60*1000
    pre_date = int(new_date - calday)

    print(new_date)
    print(new_date - calday)

    db.SellArticle.delete_many({'time':{'$lt':pre_date}})

    all_sells = list(db.SellArticle.find({},{'password':False, 'note':False}))
    
    results = []
    for sell in all_sells:
        object_id = sell['_id']
        # print(object_id)
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
    new_date = datetime.datetime.now().timestamp() * 1000
    calday = 24*60*60*1000
    pre_date = int(new_date - calday)

    db.BuyArticle.delete_many({"$or":[{'time':{"$gt":new_date}},{'time':{"$lt":pre_date}}]})

    all_buys = list(db.BuyArticle.find({},{'password':False, 'note':False}))

    results = []
    for buy in all_buys:
        object_id = buy['_id']
        buy.update({
            '_id': str(object_id)
        })
        results.append(buy)

    # print(results)
    
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

@app.route('/api/SellOneView', methods=['GET'])
def SellArticleOneView():
    id_receive = request.args.get('id')

    o_id = ObjectId(id_receive)
    # print(o_id)
    all_article = db.SellArticle.find({"_id": o_id},{"password":False})
    
    article_data = []
    
    for article in all_article:
        object_id = article['_id']
        # print(object_id)
        article.update({
            '_id': str(object_id)
        })
        article_data.append(article)
        
    print(article_data)
    
    return jsonify({
        'result' : 'success',
        'article' : article_data
    })

@app.route('/api/BuyOneView', methods=['GET'])
def BuyArticleOneView():
    id_receive = request.args.get('id')
    
    o_id = ObjectId(id_receive)
    # print(o_id)
    all_article = db.BuyArticle.find({"_id": o_id},{"password":False})

    article_data = []
    
    for article in all_article:
        object_id = article['_id']
        # print(object_id)
        article.update({
            '_id': str(object_id)
        })
        article_data.append(article)
        
    print(article_data)
    
    return jsonify({
        'result' : 'success',
        'article' : article_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)