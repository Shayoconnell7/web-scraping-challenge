# 1. import Flask
from flask import Flask, render_template
from scrape_mars import scrape
import pymongo

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection

db = client.mars_info
info_dict = db.info_dict

#homepage
@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    scraped_data = scrape
    info_dict.insert_one(scraped_data)
    
    print(info_dict)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", inventory=inventory)

#scrape_mars.scrape

# 4. Define what to do when a user hits the /scrape route
# @app.route("/scrape")
# def about():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
