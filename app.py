from flask import Flask, render_template, request
import pyrebase
import json
import helpers

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

weights = db.child("sources").get().val()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/result", methods=['GET','POST'])
def home_modal():
    if request.method == 'POST':
        data = request.form['url']
        title, score = helpers.evaluate(data, weights)
        #print(title, score)
        return render_template("home_modal.html", title = title, url = data, score = score)
    return render_template("home_modal.html", title = "", url = "", score = 0)

app.run()
