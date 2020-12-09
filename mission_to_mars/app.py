# 1. import Flask
from flask import Flask, render_template, redirect 
import scrape_mars 
from flask_pymongo import PyMongo

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

#create homepage 
@app.route("/")
def home():
    #find scraped data
    mars = mongo.db.mars.find_one()
    #pass scraped data into html file
    return render_template("index.html", mars=mars)

#create /scrape page
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    #call function to scrape data
    mars_scrape = scrape_mars.scrape()

    #update mongo database with most recent scrape
    mars.update({}, mars_scrape, upsert=True)

    #return to homepage
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)