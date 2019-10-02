from flask import Flask, render_template, request

username = "user"
password = "admin"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("/landing.html")

@app.route("/auth")
def authenticate():
    return render_template()


if __name__ == "__main__":
    app.debug = True
    app.run()
