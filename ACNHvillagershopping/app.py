from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port= 27017)
db = client.acnhDB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def villager_search():
    name_receive = request.form['name_give']

    villager = list(
        db.Villagers.find_one({'name':name_receive},{'_id':False})
    )

    return jsonify({
        'result':'success',
        'villager':villager
    })
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)