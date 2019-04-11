from flask import Flask
app = Flask(__name__)
from flask_pymongo import PyMongo

@app.route("/")
def hello():
    return "Hello World!"

app.run(debug=True)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
