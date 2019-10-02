#David Lupea
#SoftDev1 pd2
#demo -- My First Flask App
#2019-09-18

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/test")
def cooldude():
    print(__name__)
    return "Wow it worked!!"

@app.route("/milkbeforecereal")
def milkbeforecereal():
    print(__name__)
    return "Milk comes before cereal!"

if __name__ == "__main__":
    app.debug = True
    app.run()
