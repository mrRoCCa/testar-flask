from flask import Flask
app = Flask(__name__)

@app.route("/start/")
def hello():
    return "Hello World!"
    