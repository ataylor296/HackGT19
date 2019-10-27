import pyrebase
import json

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

import csv
with open('Reliable News Sources.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    all_sources = []
    for row in csv_reader:
        if row[0]:
            all_sources.append([row[0], int(row[1])])

for i in range(len(all_sources)):
    db.child("sources").child(all_sources[i][0]).update({"name": all_sources[i][0], "weight": all_sources[i][1]})