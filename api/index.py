from flask import Flask, request

app = Flask(__name__)

users = {
    "astro": "astro1388",
    "bemami": "bioc"
}

@app.route("/")
def home():
    return "\nWELCOME TO PROMETHEUS\n"

@app.route('/gate')
def authenticator():
    id = request.args.get("id")
    passkey = request.args.get("passkey")

    if id in users.keys and passkey == users[id]:
        return "USER FOUND"
