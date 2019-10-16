from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)



app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route("/")
def home():


    mars_data_1_  = mongo.db.mars_data_1_.find_one()
    return render_template("index.html", mars_data_insert = mars_data_1_ )


@app.route("/scrape")
def scrape():

   
    mars_data_1_ = mongo.db.mars_data_1_
    mars_web_data = scrape_mars.scrape_info()
    mars_data_1_.update({}, mars_web_data, upsert=True)

    return redirect("/")
 


if __name__ == "__main__":
    app.run(debug=True)




