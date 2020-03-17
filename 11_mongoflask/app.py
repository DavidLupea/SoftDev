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
def hello_world():
    return render_template("/form.html")

@app.route("/auth")
def auth():
    print(request.args)
    return render_template("/result.html", ans = dummyfunc())

def dummyfunc():
    return("This has worked abcd123")

if __name__ == "__main__":
    app.debug = True
    app.run()

def findMass(name):
    results = collection.find({"name" : name})
    for result in results:
        print(result["mass"])
def findLocation(name):
    results = collection.find({"name" : name})
    for result in results:
        ans = result["reclat"] + " " + result["reclong"]
        print(ans)
def findClass(name):
    results = collection.find({"name" : name})
    for result in results:
        print(result["recclass"])
def findYear(name):
    results = collection.find({"name" : name})
    for result in results:
        print(result["year"])
def findMassbyID(id):
    id = str(id)
    results = collection.find({"id" : id})
    for result in results:
        print(result["mass"])
def findLocationbyID(id):
    id = str(id)
    results = collection.find({"id": id})
    for result in results:
        ans = result["reclat"] + " " + result["reclong"]
        print(ans)
def findClassbyID(id):
    id = str(id)
    results = collection.find({"id" : id})
    for result in results:
        print(result["recclass"])
def findYearbyID(id):
    id = str(id)
    results = collection.find({"id" : id})
    for result in results:
        print(result["year"])

if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
