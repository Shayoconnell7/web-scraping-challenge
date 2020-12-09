# # 1. import Flask
# from flask import Flask, render_template, redirect, jsonify
# import scrape_mars 
# import PyMongo
# import pandas as pd
# import requests
# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import datetime as dt

# # 2. Create an app, being sure to pass __name__
# app = Flask(__name__)


# # setup mongo connection
# # conn = "mongodb://localhost:27017"
# # client = pymongo.MongoClient(conn)

# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)
# # connect to mongo db and collection

# # db = client.mars_info
# # info_dict = db.info_dict

# @app.route("/scrape")
# def scraper():
#     mars_info = mongo.db.mars_info
#     mars_scrape = scrape_mars.scrape()
    
#     mars_info.replace_one({}, mars_scrape, upsert=True)
    
#     return redirect("/")

# @app.route("/")
# def home():

#     # render an index.html template and pass it the data you retrieved from the database
#     return render_template("index.html", mars_data=mars_info)


# if __name__ == "__main__":
#     app.run(debug=True)
# 1. import Flask
from flask import Flask, render_template, redirect 
import scrape_mars 
#import pymongo
from flask_pymongo import PyMongo
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_info"
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#mars_info = myclient["mars_info"]

@app.route("/")
def home():
    mars = mongo.db.mars.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_scrape = scrape_mars.scrape()

    mars.update({}, mars_scrape, upsert=True)

    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)