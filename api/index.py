from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
--==WELCOME TO PROMETHEUS==--
'''


@app.route('/login')
def about():
    return 'About'