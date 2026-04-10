from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Azure App Running!"

app.run(host="0.0.0.0", port=8000)
