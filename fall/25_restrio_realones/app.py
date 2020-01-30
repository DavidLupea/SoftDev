#David Lupea and Jionghao Wu
#SoftDev1 pd2
#K24 -- A RESTful Journey Skyward
#2019-11-13

from flask import Flask
from flask import render_template
from urllib.request import urlopen
import json
import random

app = Flask(__name__)   #create instance of class Flask

@app.route("/")
def root():
    page_1 = urlopen("http://ip-api.com/json/98.113.21.243")
    response_1 = page_1.read()
    data_1 = json.loads(response_1)

    page_2 = urlopen("https://collectionapi.metmuseum.org/public/collection/v1/search?q=farms")
    response_2 = page_2.read()
    data_2 = json.loads(response_2)

    rand = random.randint(0,data_2['total'])
    rand_entry = data_2['objectIDs'][rand]

    page_3 = urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(rand_entry))
    response_3 = page_3.read()
    data_3 = json.loads(response_3)

    img_1 = data_3["primaryImageSmall"]
    # artist = data_3["constituents"][0]['name']

    page_4 = urlopen("http://quotes.rest/qod.json")
    response_4 = page_4.read()
    data_4 = json.loads(response_4)
    data_4 = data_4["contents"]
    data_4 = data_4["quotes"]
    data_4 = data_4[0]

    return render_template("index.html",vals = data_1, img = img_1, quote = data_4['quote'],author = data_4['author'])



if __name__ == "__main__":
    app.debug = True
    app.run()
