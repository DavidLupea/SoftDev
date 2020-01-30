import sqlite3

FILENAME = "data.db"


def createUsers():
    db = sqlite3.connect(FILENAME)
    c = db.cursor()

    command = "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, ip TEXT, longitude REAL, latitude REAL)"
    c.execute(command)

    db.commit()
    db.close()


def addToUser(user, passw, ip, lon, lat):
    db = sqlite3.connect(FILENAME)
    c = db.cursor()

    command = 'INSERT INTO users VALUES ({}, {}, {}, {}, {})'
    command = command.format(user, passw, ip, lon, lat)
    c.execute(command)

    db.commit()
    db.close()


def updateIP(user, ip, lon, lat):
    db = sqlite3.connect(FILENAME)
    c = db.cursor()

    user = "\"" + user + "\""
    ip = "\"" + ip + "\""
    lon = "\"" + str(lon) + "\""
    lat = "\"" + str(lat) + "\""

    command = "UPDATE users SET ip = {}, longitude = {}, latitude = {} WHERE  username = {}"
    command = command.format(ip, lon, lat, user)
    c.execute(command)

    db.commit()
    db.close()


def getUser(user):
    db = sqlite3.connect(FILENAME)
    c = db.cursor()

    user = "\"" + user + "\""
    userDict = {}

    c.execute("SELECT * FROM users WHERE username = " + user)
    s = c.fetchall()
    if len(s) == 0:
        return {}
    else:
        s = s[0]
        userDict["user"] = s[0]
        userDict["pass"] = s[1]
        userDict["ip"] = s[2]
        userDict["lon"] = float(s[3])
        userDict["lat"] = float(s[4])

        db.commit()
        db.close()
        return userDict


def register(user, passw, ip, lon, lat):
    userDict = getUser(user)
    # if the username is already in the DB
    if 'user' in userDict:
        return False

    user = "\"" + user + "\""
    passw = "\"" + passw + "\""
    ip = "\"" + ip + "\""
    addToUser(user, passw, ip, lon, lat)
    return True


def validate(user, passw, ip):
    # 0 -> validated
    # 1 -> username wrong
    # 2 -> password wrong
    # 3 -> IP has changed

    userDict = getUser(user)
    if 'user' not in userDict:
        return 1
    if userDict["pass"] != passw:
        return 2
    if userDict["ip"] != ip:
        return 3
    return 0
