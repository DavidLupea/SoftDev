#David Lupea, Jionghao Wu
#SoftDev1 pd2
#K24 -- Getting More REST
#2019-11-14

from flask import Flask
from flask import render_template
from urllib.request import urlopen
import json

u = urlopen("http://ip-api.com/json/92.239.17.225")
response = u.read()
data = json.loads(response)
print(data)
