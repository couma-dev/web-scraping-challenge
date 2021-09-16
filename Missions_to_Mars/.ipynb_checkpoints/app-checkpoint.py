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
    hemisphere_image_urls= mongo.db.hemisphere_image_urls.find_one()
    return render_template ('index.html', mars = hemisphere_image_urls)
      
@app.route("/scrape")
def scrape():
     hemisphere_image_urls = mongo.db.hemisphere_image_urls
     mars_data = scrape_mars.scrape()
     hemisphere_image_urls.update({}, mars_data, upsert=True)
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)