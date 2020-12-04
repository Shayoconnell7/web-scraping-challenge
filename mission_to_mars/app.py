# 1. import Flask
from flask import Flask, render_template, redirect
import scrape_mars 
import pymongo

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection

# db = client.mars_info
# info_dict = db.info_dict

@app.route("/scrape")
def scraper():
    mars_info = client.db.mars_info
    mars_scrape = scrape_mars.scrape()
    
    mars_info.replace_one({}, mars_scrape, upsert=True)
    
    return redirect("/")

@app.route("/")
def home():

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars_data=mars_info)


if __name__ == "__main__":
    app.run(debug=True)
