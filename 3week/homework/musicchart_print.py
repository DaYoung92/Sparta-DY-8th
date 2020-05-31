from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.dbsparta

all_musics = list(db.musics.find())

for music in all_musics:
    rank = music["rank"]
    name = music["name"]
    musician = music["musician"]
    print(rank, name, musician)