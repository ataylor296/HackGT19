from flask import Flask
import pyrebase
import json
import helpers

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

weights = db.child("sources").get().val()

@app.route("/")
def hello():
    return "Hello World!"


