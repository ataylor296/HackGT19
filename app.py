from flask import Flask
import pyrebase
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

# db = firebase.database()
# db.child("users").child("Tarek")
# data = {"name": "Mortimer 'Tarek' Ullah"}
# db.child("users").push(data)
# db.child("users").child("Hossain")
# dat = {"name" : "shuvo" , "score" : 600}
# db.push(dat)