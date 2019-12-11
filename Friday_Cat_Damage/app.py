from flask import Flask, render_template, session, request, jsonify, redirect, url_for
import ast
import urllib
import json
import os
import databaseUtils
import converter
import math

app = Flask(__name__)

# HELPER FUNCTIONS


def getIP():
    link = "https://api6.ipify.org?format=json"
    u = urllib.request.urlopen(link)
    response = u.read()
    ip = json.loads(response)["ip"]
    return ip


def get_ip_data(ip):
    link = "http://ip-api.com/json/{}".format(ip)
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)
    return data

# LOGIN ROUTES
@app.route("/")
def root():
    databaseUtils.createUsers()
    if "username" in session:
        return redirect("/welcome")
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/processRegistration")
def processRegistration():
    # getting user ip
    ip = getIP()
    # getting user lat/lon
    data = get_ip_data(ip)

    user = request.args["username"]
    passw = request.args["password"]
    confirm = request.args["confirm"]
    check = True

    if user == "" or passw == "":
        return render_template("register.html", error="You must fill out all fields")
    elif passw != confirm:
        return render_template("register.html", error="Passwords do not match")
    else:
        check = databaseUtils.register(
            user, passw, ip, data["lon"], data["lat"])

    if check:
        session["username"] = user
        session["password"] = passw
        return redirect(url_for("welcome"))
    else:
        return render_template("register.html", error="Username already in use. Choose a different one")


@app.route("/auth")
def authenticate():
    if len(request.args) == 0:
        session.pop("username")
        return redirect("/")
    user = request.args["username"]
    passw = request.args["password"]
    ip = getIP()
    check = databaseUtils.validate(user, passw, ip)
    if check == 0:
        session["username"] = request.args["username"]
        return redirect(url_for("welcome"))
    elif check == 1:
        return render_template("login.html", error="Your username is unfortunately WRONG")
    elif check == 2:
        return render_template("login.html", error="Your password is unfortunately WRONG")
    elif check == 3:
        data = get_ip_data(ip)
        databaseUtils.updateIP(user, ip, data["lon"], data["lat"])
        session["username"] = request.args["username"]
        return redirect(url_for("welcome"))

# AFTER LOGIN ROUTES


@app.route("/welcome")
def welcome():
    return render_template("welcome.html", ip=getIP(), data=get_ip_data(getIP()))


@app.route("/log_key")
def get_key():
    session["key"] = request.args.get("mapquest_key")
    return render_template("welcome.html", ip=getIP(), data=get_ip_data(getIP()),
                           thanks="Your API key has been logged successfully")


@app.route("/traffic")
def traffic():
    userDict = databaseUtils.getUser(session["username"])
    ip = userDict["ip"]
    lat = userDict["lat"]
    lon = userDict["lon"]

    # link for traffic flow image
    link = "https://www.mapquestapi.com/staticmap/v5/map?center={}&zoom=12&traffic=flow|cons|inc&size=600,400@2x&key={}"
    # adding lat/lon and key to request
    lat_lon = str(lat) + "," + str(lon)
    # if user did not enter a key
    if 'key' not in session:
        return render_template("welcome.html", ip=ip, data=get_ip_data(ip),
                               error="You did not enter an API key!")
    else:
        key = session["key"]

    piclink = link.format(lat_lon, key)

    # link for traffic incident api request
    link = "https://www.mapquestapi.com/traffic/v2/incidents?&outFormat=json&boundingBox={}%2C{}%2C{}%2C{}&key={}"
    # creating box of lons + lats for api to search
    latOffset = 1.0 / 20.0
    latMax = lat + latOffset
    latMin = lat - latOffset

    lngOffset = latOffset * math.cos(lat * math.pi / 180.0)
    lngMax = lon + lngOffset
    lngMin = lon - lngOffset
    # adding box + key to request
    link = link.format(latMax, lngMax, latMin, lngMin, key)
    try:
        u = urllib.request.urlopen(link)
    except:
        return render_template("welcome.html", ip=ip, data=get_ip_data(ip),
                               error="Your API key was incorrect!")
    response = u.read()
    # returns a dict with a list called incidents
    incidents = json.loads(response)
    return render_template("traffic.html", incidents=incidents["incidents"], picRef=piclink)


@app.route("/weather")
def weather():
    # getting db info
    userDict = databaseUtils.getUser(session["username"])
    ip = userDict["ip"]
    lat = userDict["lat"]
    lon = userDict["lon"]

    # request to get where on earth id
    link = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(
        lat, lon)
    u = urllib.request.urlopen(link)
    response = u.read()
    location_data = json.loads(response)
    # where on earth id recieved from api
    woeid = str(location_data[0]["woeid"])

    # getting actual weather in that area
    link = "https://www.metaweather.com/api/location/{}".format(woeid)
    u = urllib.request.urlopen(link)
    response = u.read()
    weather_data = json.loads(response)["consolidated_weather"]

    # getting weather icons
    link = "https://www.metaweather.com/static/img/weather/png/64/{}.png"
    for day in weather_data:
        day["icon"] = link.format(day['weather_state_abbr'])

    return render_template("weather.html",
                           weather=weather_data)


@app.route("/business_form")
def business_form():
    return render_template("business_form.html",
                           sic_code_names=converter.return_sic_code_names())


@app.route("/business_list")
def business_list():
    # getting user info from db
    userDict = databaseUtils.getUser(session["username"])
    ip = userDict["ip"]
    lat = userDict["lat"]
    lon = userDict["lon"]

    # request for places of a certain type in the area
    link = "https://www.mapquestapi.com/search/v2/radius?origin={},{}&radius=2&maxMatches=100&ambiguities=ignore&hostedData=mqap.ntpois|group_sic_code=?|{}&declutter=true&outFormat=json&key={}"
    # sic_code is an id code for each type of business
    sic_code = converter.get_sic_code(request.args.get("industry"))
    # checks if user has enterred an api key
    if 'key' not in session:
        return render_template("welcome.html", ip=ip, data=get_ip_data(ip),
                               error="You did not enter an API key!")
    else:
        key = session["key"]
    # adding params to link request
    link = link.format(lat, lon, sic_code, key)
    try:
        # checking if api key works
        u = urllib.request.urlopen(link)
    except:
        return render_template("welcome.html", ip=ip, data=get_ip_data(ip),
                               error="Your API key was incorrect!")
    response = u.read()
    businesses = json.loads(response)
    # checking if there are businesses of the selected type in the area
    # if there are none, user is sent back
    if 'searchResults' not in businesses:
        return render_template("business_form.html",
                               sic_code_names=converter.return_sic_code_names(),
                               error="Sorry, there are no businesses of that type in your area. Please select another type.")
    else:
        businesses = businesses['searchResults']  # business list
        lat_lng = str(lat) + "," + str(lon) + "|marker-red" + \
            "||"  # for location marker
        i = 0

        # adding location markers to the map for each business
        for entry in businesses:
            i += 1  # becomes the number on the location marker
            lat_lng += str(entry["fields"]["lat"]) + "," + \
                str(entry["fields"]["lng"]) + "|marker-" + str(i) + "||"
        link = "https://www.mapquestapi.com/staticmap/v5/map?locations={}&size=600,400@2x&&declutter=true&key={}"
        key = session["key"]
        link = link.format(lat_lng, key)  # adding location and key to request
        return render_template("business_list.html",
                               json=businesses,
                               image=link)


@app.route("/directions")
def directions():
    userDict = databaseUtils.getUser(session["username"])
    ip = userDict["ip"]
    lat = userDict["lat"]
    lon = userDict["lon"]

    # destination
    place = ast.literal_eval(request.args['index'])

    link = "http://ip-api.com/json/{}".format(ip)
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)

    # mapquest directions link
    link = "https://www.mapquestapi.com/directions/v2/route?key={}&from={}&to={}&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"
    # user zip CODE
    start = str(lat) + "," + str(lon)
    # destination address
    dest = str(place["fields"]["lat"]) + "+," + str(place['fields']['lng'])
    # adding necessart info to link
    key = session["key"]
    link = link.format(key, start, dest)

    u = urllib.request.urlopen(link)
    response = u.read()
    # big dictionary with all necessary steps
    directions = json.loads(response)['route']

    link = "https://open.mapquestapi.com/staticmap/v5/map?start={}&end={}&size=600,400@2x&key={}".format(
        start, dest, key)

    return render_template("directions.html", place=place, directions=directions, pic=link, dest=place['fields']['name'])


@app.route("/inputAddress")
def inputAddress():
    userDict = databaseUtils.getUser(session["username"])
    ip = userDict["ip"]
    lat = userDict["lat"]
    lon = userDict["lon"]

    # destination
    place = ast.literal_eval(request.args['index'])

    link = "http://ip-api.com/json/{}".format(ip)
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)

    # mapquest directions link
    link = "https://www.mapquestapi.com/directions/v2/route?key={}&from={}&to={}&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"
    # user zip CODE
    start = request.args['address'].replace(" ", "+")
    # destination address
    dest = str(place["fields"]["lat"]) + "+," + str(place['fields']['lng'])
    # adding necessart info to link
    key = session["key"]
    link = link.format(key, start, dest)

    u = urllib.request.urlopen(link)
    response = u.read()
    # big dictionary with all necessary steps
    directions = json.loads(response)['route']

    link = "https://open.mapquestapi.com/staticmap/v5/map?start={}&end={}&size=600,400@2x&key={}".format(
        start, dest, key)

    return render_template("directions.html", place=place, directions=directions, pic=link, dest=place['fields']['name'])


if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
