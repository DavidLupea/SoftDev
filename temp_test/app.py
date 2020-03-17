from flask import Flask, render_template, request
from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient('localhost', 27017);
try:
    client.drop_database('frootNinjas')
except:
    pass

db = client.frootNinjas
collection = db.meteors

if (collection.count() == 0):
    f = open("meteor.json", "r")
    data = f.readlines()
    for line in data:
        collection.insert_one(loads(line))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/auth")
def authenticate():
    return render_template("result.html", ans = "test1234")


if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
