
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#mongo = pymongo(app, url="mongodb://localhost:27017/mars_app")
#mars_data = mongo.db.mars_data
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#################################################
# Flask Routes
#################################################

@app.route("/")

def home():
    """List all available api routes."""
    scraped_dict = mongo.db.scraped_dict.find_one()
    return render_template ("index.html", mars = scraped_dict)
      
@app.route("/scrape")
def scrape():
     scraped_dict = mongo.db.scraped_dict
     scraped_data = scrape_mars.scrape()
     scraped_dict.update({}, scraped_data, upsert=True)
     return redirect("/", code = 302)

if __name__ == '__main__':
    app.run(debug=True)
