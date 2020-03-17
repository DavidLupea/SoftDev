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

@app.route("/name_to_mass")
def name_to_mass():
    return render_template("form.html", ans = findMass(request.args["input"]))

@app.route("/name_to_time")
def name_to_time():
    return render_template("form.html", ans = findYear(request.args["input"]))

@app.route("/name_to_class")
def name_to_class():
    return render_template("form.html", ans = findClass(request.args["input"]))

@app.route("/name_to_location")
def name_to_location():
    return render_template("form.html", ans = findLocation(request.args["input"]))

@app.route("/id_to_mass")
def id_to_mass():
    return render_template("form.html", ans = findMassbyID(request.args["input"]))

@app.route("/id_to_time")
def id_to_time():
    return render_template("form.html", ans = findYearbyID(request.args["input"]))

@app.route("/id_to_class")
def id_to_class():
    return render_template("form.html", ans = findClassbyID(request.args["input"]))

@app.route("/id_to_location")
def id_to_location():
    return render_template("form.html", ans = findLocationbyID(request.args["input"]))


def findMass(name):
    results = collection.find({"name" : name})
    for result in results:
        return result["mass"]
def findLocation(name):
    results = collection.find({"name" : name})
    for result in results:
        ans = result["reclat"] + " " + result["reclong"]
        return ans
def findClass(name):
    results = collection.find({"name" : name})
    for result in results:
        return result["recclass"]
def findTime(name):
    results = collection.find({"name" : name})
    for result in results:
        return result["year"]
def findMassbyID(id):
    results = collection.find({"id" : id})
    for result in results:
        return result["mass"]
def findLocationbyID(id):
    results = collection.find({"id": id})
    for result in results:
        ans = result["reclat"] + " " + result["reclong"]
        return ans
def findClassbyID(id):
    results = collection.find({"id" : id})
    for result in results:
        return result["recclass"]
def findTimebyID(id):
    results = collection.find({"id" : id})
    for result in results:
        return result["year"]


if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
