# Team StraitOuttaSoftDev
# David Lupea, Devin Lin
# 2019-10-03

import os
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = os.urandom(32)

creds = {"user": "user", "password": "password"}

@app.route('/')  # Landing/Login
def index():
    if (session.get("user") == creds['user']) and (session.get("password") == creds['password']):   #Session info
        return redirect('/auth')
    return render_template('landing.html')

@app.route("/auth")
def authentication():
    if request.args['user']:
        session['user'] = request.args['user']
        session['password'] = request.args['pass']
    if 'user' in session:
        if session["user"] == creds['user'] and session.get("password") == creds['password']:   #Load logged in page with user's information
            return render_template("response.html", info=session, method_type=request.method)
        if session.get('password') != creds['password']:
            return render_template("landing.html", error = "Your password is WRONG")
        return render_template("landing.html", error = "Your username is WRONG")

@app.route('/logout')  #Clears user's session
def logout():
    session.pop('user', None)
    return render_template("landing.html")

app.debug = True
app.run()
