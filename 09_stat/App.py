from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/my_foist_template")
def template():
    coll = [0, 1, 1, 2, 3, 5, 8]
    

if __name__ == "__main__":
    app.debug = True
    app.run()
