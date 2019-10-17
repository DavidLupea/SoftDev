# Team StraitOuttaSoftDev
# David Lupea, Devin Lin
# 2019-10-05

import os
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

creds = {"username": "steve", "password": "jobs"}

@app.route('/')  # Landing/Login
def index():
    if (session.get("username") == creds['username']) and (session.get("password") == creds['password']):   #checks if user is still logged in
        return redirect('/auth')
    return render_template('landing.html')

@app.route("/auth")
def authentication():
    # print(request.args)
    session['username'] = request.args['username']
    session['password'] = request.args['password']
    if 'username' in session:
        if session["username"] == creds['username'] and session.get("password") == creds['password']:   #Load logged in page with user's information
            return render_template("response.html", info=session, method_type=request.method)
        if session.get('password') != creds['password'] and session.get('username') != creds['username']:
            flash('Wrong Username and Password')
            return redirect(url_for('index'))
        if session.get('password') != creds['password']:
            flash('Wrong Password')
            return redirect(url_for('index'))
        if session.get('username') != creds['username']:
            flash('Wrong Username')
            return redirect(url_for('index'))

@app.route('/logout')  #Clears username's session
def logout():
    session.pop('username', None)
    return render_template("landing.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
