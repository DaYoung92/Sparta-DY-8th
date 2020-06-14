from flask import Flask, render_template, jsonify, request #flask 기능 불러오기
# render_template HTML 파일을 불러온다
#jsonify 파이썬의 딕셔너리를 json 형태로 바꿔준다
#request 클라이언트가 서버에게 보내는 데이터를 쉽게 처리해준다

app = Flask(__name__)

# python decorator(데코레이터 = 문법 종류임) : 함수에 추가적인 기능을 넣어주는 함수
@app.route('/') #router 기능을 함수에 장착한다 : route는 사용자가 접속할 수 있는 url을 생성함. 여기서는 'localhost/'(로컬호스트 메인페이지)라는 주소를 할당한다는 뜻임. /mypage 라고 쓰면 'localhost/mypage'r라는 주소가 생김
def home():
        # return "Hello World!"
        return render_template('index.html') #연동할 html 파일명을 입력한다 (반드시 templates 폴더 안에 있어야 함)

@app.route('/mypage')
def mypage():
    return "This is My Page"

# API
# url, header, body
# get : header까지.수신
# post: 전부다. 송신

@app.route('/test/get/data', methods=['GET'])
def get_data():
    username_receive = request.args.get('username')
    password_receive = request.args.get('password')
    data = {
        'test': 123,
        'test1': True,
        'test2': '스파르타'
    }

    if password_receive == '1234' :
        data['test1'] = False

    return  jsonify(data)


@app.route('/test/post/data', methods=['POST'])
def post_data():
    username_receive = request.form['username']
    password_receive = request.form['password']

    print(username_receive, password_receive)

    data = {
        'success' : True
    }
    return jsonify(data)

# __name__:해당 파이썬 파일이 실행되는 위치
if __name__ == '__main__': #="해당 파이썬 파일이 실행되었을 때"
    app.run('0.0.0.0', debug=True, port=5000) #="app을 실행시킨다 (app은 위의 Flask 변수)"
    # '0.0.0.0' : 모든 ip의 접근을 허용한다
    # debug =True : debug 모드.  테스트 중이라는 뜻으로, 어디 부분이 에러가 나는지 일일이 다 표시한다.
    # port: 접속 경로 포트. 'localhost:5000'이라고 치면 접속이 된다는 뜻이다.
    # 이 문구는 항상 맨 끝에 위치해야 한다. 안 그럼 에러난다

