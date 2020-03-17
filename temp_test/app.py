from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(app)
    return render_template("/form.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "hi"


if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0')
