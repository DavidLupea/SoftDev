#David Lupea
#SoftDev1 pd2
#K24 -- A RESTful Journey Skyward
#2019-11-13

from flask import Flask
from flask import render_template
from urllib.request import urlopen
import json

app = Flask(__name__)   #create instance of class Flask

@app.route("/")
def root():
    u = urlopen("https://api.nasa.gov/planetary/apod?api_key=guzL1fAp3pwbQ3bozJgEJTo6C5uJRxh8a5oQqEMN")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",pic = data['url'],capt = data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
