from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

mongo = pymongo(app, url="mongodb://localhost:27017/mars_app")
#################################################
# Flask Routes
#################################################

@app.route("/scrape")

def home():
    """List all available api routes."""
    mars_dict= mongo.db.mars_dict.find_one()
    return render_template ('index.html', mars = mars_dict)
      
@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)