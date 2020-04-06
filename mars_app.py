from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
import Mars_Scrape_Fxns
import os 

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')

#app.config["MONGO_URI"] = "mongodb://localhost:27017/"
#mongo = PyMongo(app)

mydb = client.mars_scrape

mycol = mydb.mars_collection

@app.route("/")
def home(): 
    mars_collection = mycol.find_one()
    return render_template("index.html", mars_collection=mars_collection) 

@app.route("/scrape")
def scrape():
    mars_collection = mycol
    mars_title = Mars_Scrape_Fxns.newsfxn()
    mars_news = Mars_Scrape_Fxns.newsfxn()
    mars_image = Mars_Scrape_Fxns.imgfxn()
    mars_weather = Mars_Scrape_Fxns.weatherfxn()
    mars_facts = Mars_Scrape_Fxns.factsfxn()
    mars_hemis = Mars_Scrape_Fxns.hemisfxn()

    data = {
        "mars_title": mars_title,
        "mars_news": mars_news,
        "mars_image": mars_image, 
        "mars_weather": mars_weather,
        "mars_facts": mars_facts,
        "mars_hemis": mars_hemis 
    }

    mycol.update({}, data, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)

