import bson
from pymongo import MongoClient

client = MongoClient('localhost', 27017);
db = client.friutyNinjas
collection = db.askReddit

if (collection.count() == 0):
    f = open("rickMorty.json", "r")
    data = f.readlines()
    for line in data:
        collection.insert_one(loads(line))
    print(collection)
