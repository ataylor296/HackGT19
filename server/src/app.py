from flask import Flask, render_template, request
import pyrebase
import json
import helpers
import os

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

weights = db.child("sources").get().val()

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/result", methods=['GET','POST'])
def modal():
    if request.method == 'POST':
        data = request.form['url']
        title, score = helpers.evaluate(data, weights)
        #print(title, score)
        return render_template("modal.html", title = title, url = data, score = score)
    return render_template("modal.html", title = "", url = "", score = 0)

app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
