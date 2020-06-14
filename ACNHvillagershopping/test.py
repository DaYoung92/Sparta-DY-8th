from pymongo import MongoClient #pymongo 패키지에서  MongoClient 기능 가져오긔

client = MongoClient('localhost', 27017) #포트 번호를 선언한다
db = client.acnhDB #데이터베이스 하나 생성. 이름은 dbsparta

all_villagers = list(db.Villagers.find()) #사람이 읽을 수 있게 python list로 변환
print(all_villagers)