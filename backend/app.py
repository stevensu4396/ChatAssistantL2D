from flask import Flask,request
from flask_socketio import SocketIO, emit
import chatgpt_service as gpt
import voice_gen_service as voice

app = Flask(__name__, static_folder='../front', static_url_path='/web')
socket = SocketIO(app, cors_allowed_origins='*') #跨域问题
@app.route('/')
def index():
    question = request.args["question"]
    answer = gpt.chatgpt(question)
    return answer

@app.route("/record", methods=["POST"])
def record():
    data = request.files
    print("start...")
    print(type(data))
    print(data)
    file = data['upfile']
    print(file.filename)
    print(request.headers)
    # 文件写入磁盘
    file.save('./' + file.filename)
    print("end...")
    return voice.tts()

if __name__ == "__main__":
    app.run(host='0.0.0.0')