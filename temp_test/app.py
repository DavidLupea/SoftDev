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
    return render_template("form.html", ans = request.args["input"])

@app.route("/name_to_year")
def name_to_year():
    return render_template("form.html", ans = "test1234")

@app.route("/name_to_class")
def name_to_class():
    return render_template("form.html", ans = "test1234")

@app.route("/name_to_location")
def name_to_location():
    return render_template("form.html", ans = "test1234")

@app.route("/id_to_mass")
def id_to_mass():
    return render_template("form.html", ans = "test1234")

@app.route("/id_to_year")
def id_to_year():
    return render_template("form.html", ans = "test1234")

@app.route("/id_to_class")
def id_to_class():
    return render_template("form.html", ans = "test1234")

@app.route("/id_to_location")
def id_to_location():
    return render_template("form.html", ans = "test1234")


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
def findYear(name):
    results = collection.find({"name" : name})
    for result in results:
        return result["year"]
def findMassbyID(id):
    id = str(id)
    results = collection.find({"id" : id})
    for result in results:
        return result["mass"]
def findLocationbyID(id):
    id = str(id)
    results = collection.find({"id": id})
    for result in results:
        ans = result["reclat"] + " " + result["reclong"]
        return ans
def findClassbyID(id):
    id = str(id)
    results = collection.find({"id" : id})
    for result in results:
        return result["recclass"]
def findYearbyID(id):
    id = str(id)
    results = collection.find({"id" : id})
    for result in results:
        return result["year"]




if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
