from flask import Flask, render_template
import pyrebase
import json
import helpers

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

weights = db.child("sources").get().val()

@app.route("/", methods=['POST'])
def home():
    return render_template("home.html", score = 0)

@app.route("/<link>/result", methods=['GET'])
def result_modal(link):
    title, score = helpers.evaluate(link, weights)
    return render_template("home.html", score = score)
