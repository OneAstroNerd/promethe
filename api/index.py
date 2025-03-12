from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # if request.method != "GET":
    #     return '''
    # --==WELCOME TO PROMETHEUS==--
    # '''
    
    if request.method == "GET":
        return "you sent a get request"
    elif request.method == "POST":
        return "you sent a pst request"