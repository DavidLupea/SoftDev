from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("/template.html")

@app.route("/auth")
def authenticate():
    return "hi"


if __name__ == "__main__":
    app.debug = True
    app.run()
