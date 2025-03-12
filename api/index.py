from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
--==WELCOME TO PROMETHEUS==--

prometheus is a minimal CLI messenger
    '''

@app.route('/about')
def about():
    return 'About'