from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    if request.method == "GET":
        return '''
    --==WELCOME TO PROMETHEUS==--
    '''