from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "\nWELCOME TO PROMETHEUS\n"

@app.route('/gate', metods=["POST"])
def authenticator():
    pass