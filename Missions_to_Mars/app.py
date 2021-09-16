from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

mongo = pymongo(app, url="mongodb://localhost:27017/mars_app")
mars_data = mongo.db.mars_data
#################################################
# Flask Routes
#################################################

@app.route("/")

def home():
    """List all available api routes."""
    return render_template ('index.html')
      
@app.route("/scrape")
def scrape():
     
     scraped_data = scrape_mars.scrape()
     mars_data.update({}, scraped_data, upsert=True)
     return redirect("/data")
@app.route("/data")
def data():
    mars_info = mongo.db.mars_data.find_one()
    return render_template("index.html", info=mars_info)
if __name__ == '__main__':
    app.run(debug=True)