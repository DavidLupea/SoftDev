from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient('localhost', 27017);
db = client.K09
collection = db.restaurants

if (collection.count() == 0):
    f = open("primer-dataset.json", "r")
    data = f.readlines()
    for line in data:
        collection.insert_one(loads(line))

def findBorough(borough):
    result = collection.find({"borough" : borough})
    print("\nAll restaurants in the borough " + borough + "\n")
    for place in result:
        print(place["name"])

#findBorough("Brooklyn")

def findZip(zipCode):
    result = collection.find({"address.zipcode" : zipCode})
    print("\nAll restaurants with the zip code " +zipCode + "\n")
    for place in result:
        print(place["name"])

#findZip("10462")

def findZipGrade(zipCode, grade):
    result = collection.find({"address.zipcode" : zipCode, "grades.grade" : grade})
    print("\nAll restaurants with the zip code " + zipCode + " and grade " + grade + "\n")
    for place in result:
        print(place["name"])

#findZipGrade("10462", "A")

def findZipScore(zipCode, score): 
    result = collection.find({"address.zipcode" : zipCode, "grades.score" : {"$lt" : score}})
    print("\nAll restaurants with the zip code " + zipCode + " and score below " + str(score) + "\n")
    for place in result:
        print(place["name"])

#findZipScore("10462", 1)
