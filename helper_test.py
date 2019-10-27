from flask import Flask
import pyrebase
import json
import helpers

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

weights = db.child("sources").get().val()

test_news = ["https://www.nydailynews.com/news/politics/ny-trump-first-pitch-washington-nationals-world-series-20191026-o5rnjkq3trhfnpenpvah4fadtm-story.html?fbclid=IwAR1Bz7xj629rTFw8p5AaKLYSrG6SvLaAZwBNC4vTdMJ0vCyVDzawh7rCnG0",
            "https://www.cnn.com/2019/10/26/politics/company-government-contract-donald-trump-brother-robert-trump/index.html",
            "https://abcnews.go.com/Politics/state-department-official-expected-part-impeachment-probe/story?id=66532626&cid=clicksource_4380645_null_hero_hed",
            "https://www.usnews.com/news/elections/articles/2019-10-25/the-state-of-the-presidential-race-100-days-until-the-iowa-caucus",
            "https://www.npr.org/2019/10/26/773706177/pentagon-awards-10-billion-contract-to-microsoft-over-front-runner-amazon",
            "https://www.nytimes.com/2019/10/26/us/tennessee-treehouse-fire.html",
            "https://www.huffpost.com/entry/al-franken-comeback-politicon_n_5db2300be4b0a89374020d55?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuaHVmZnBvc3QuY29tL25ld3Mv&guce_referrer_sig=AQAAAK1EbjNMIbjvCJBNwOo5wC5hxouNhFg7KktUGaVrm_Qbkmi3iri2a7zDnQNG0ra9g_nGJ9jLrKljUlj5FqDZ-FL11ENuKe14fDZvkekFXJbeBU7TvwYfeWxNivPrt7wApwGqSTwlOjRmq7s1SQ16mj05pPdVdW7ZJTRQSOKGZ5Gs",
            "https://fox2now.com/2019/10/26/belleville-apartment-fire-caused-by-unattended-candle/"]

for s in test_news:
    title, score = helpers.evaluate(s, weights)
    if title:
        print("Title: ", title)
    else:
        print("Title: Unknown")
    print(score)