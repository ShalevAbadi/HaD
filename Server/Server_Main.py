from flask import Flask
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect("HaD.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Category(
            category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            category_Name TEXT)
        """)

c.execute("""CREATE TABLE IF NOT EXISTS Event(
            event_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            event_Name TEXT,
            event_Description TEXT,
            evet_Picture BLOB,
            event_Start_Time INTEGER,
            event_End_Time INTEGER,
            event_Minimum_Participants INTEGER,
            event_Maximum_Participants INTEGER,
            FOREIGN KEY(restrictions_ID) REFERENCES Restrictions(restrictions_ID))
            FOREIGN KEY(rank_ID) REFERENCES Restrictions(rank_ID))
        """)
c.execute("""INSERT INTO Category(category_Name) VALUES ('Running')""")
conn.commit()


"""
@app.route("/")
def hello():
    return "Hello world"

@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)
app.run(debug=True)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
"""