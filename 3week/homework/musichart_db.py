import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
musics = soup.select('table.list-wrap > tbody > tr.list')

# musics (tr들) 의 반복문을 돌리기
for music in musics:
    rank_number = music.select_one('td.number')
    if rank_number is not None:
        rank_raw = music.select_one('td.number').text
        rank = rank_raw[0:2]
        name = music.select_one('td.info > a.title.ellipsis').text.strip()
        musician = music.select_one('td.info > a.artist.ellipsis').text
        db.musics.insert_one({
            'rank':rank,
            'name':name,
            'musician':musician
        })
