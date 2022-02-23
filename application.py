#ENGO 651 Lab 2
#Andrew Symes
#UCID 30033743

#imports, More than is needed but ok
import os
import re
import requests
import json
from flask import Flask, session
from flask import render_template, request
from flask import request
from flask_session import Session
import pandas as pd
#install sodapy
from sodapy import Socrata

app = Flask(__name__)

#Homepage, and only page
@app.route("/", methods = ["GET", "POST"])
def index():
    #Code modified from Socrata tutorial available at https://dev.socrata.com/blog/2014/11/04/data-visualization-with-python.html
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    #Data information provided through https://dev.socrata.com/foundry/data.calgary.ca/c2es-76ed
    client = Socrata("data.calgary.ca", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(data.calgary.ca,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    if request.method == "GET":
        selection = "False"

    if request.method == "POST":
        selection = request.form.get("selection")


    return render_template("Mappingpage.html", selection= selection)

#the above code transforming the query to geoJSON was adapted from the code providded at
#https://notebook.community/captainsafia/nteract/applications/desktop/example-notebooks/pandas-to-geojson


@app.route("/newenv", methods = ["GET", "POST"])
def newenv():
    if request.method == "GET":
        selection = "Yes"
        return render_template("test.html",selection=selection)

    if request.method == "POST":
        selection = request.form.get("selection")
        return render_template("test.html",selection=selection)







#https://notebook.community/captainsafia/nteract/applications/desktop/example-notebooks/pandas-to-geojson

print("hello")
