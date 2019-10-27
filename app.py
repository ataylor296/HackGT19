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

print(helpers.get_weight("https://www.nydailynews.com/news/politics/ny-trump-first-pitch-washington-nationals-world-series-20191026-o5rnjkq3trhfnpenpvah4fadtm-story.html?fbclid=IwAR1Bz7xj629rTFw8p5AaKLYSrG6SvLaAZwBNC4vTdMJ0vCyVDzawh7rCnG0", weights))

@app.route("/")
def hello():
    return "Hello World!"


