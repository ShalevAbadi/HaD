from flask import Flask
import sqlite3
import requests


app = Flask(__name__)

conn = sqlite3.connect("HaD.db")
c = conn.cursor()


def initialize_db_tables():

    c.execute("""CREATE TABLE IF NOT EXISTS User (
                user_Name text PRIMARY KEY,
                user_Password TEXT,
                user_Email   TEXT,
                user_Rank    REAL,
                user_Age    INTEGER,
                user_First_Name TEXT,
                user_Last_Name    TEXT
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Restrictions (
                 restrictions_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 restrictions_Min_Age   INTEGER,
                 restrictions_Max_Age    INTEGER,
                 restrictions_Sex TEXT,
                 restrictions_Description    TEXT
                 )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Rank (
                 rank_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 FOREIGN KEY(user_Name) REFERENCES artist(User),
                 rank_Point   INTEGER,
                 rank_Description    TEXT,
                 )""")
    c.execute("""CREATE TABLE IF NOT EXISTS Category(
            category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            category_Name TEXT)
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS Event(
            event_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY(event_Manager) REFERENCES User(user_Name)
            event_Name TEXT,
            event_Description TEXT,
            evet_Picture BLOB,
            event_Start_Time INTEGER,
            event_End_Time INTEGER,
            event_Location TEXT,
            event_Minimum_Participants INTEGER,
            event_Maximum_Participants INTEGER,
            FOREIGN KEY(restrictions_ID) REFERENCES Restrictions(restrictions_ID)
            FOREIGN KEY(rank_ID) REFERENCES Rank(rank_ID))
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS Attendee(
            FOREIGN KEY(event_ID) REFERENCES Events(Event_ID)),
            FOREIGN KEY(user_Name) REFERENCES User(user_Name))
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS Chat(
                FOREIGN KEY(event_ID) REFERENCES Events(Event_ID)),
                FOREIGN KEY(user_Name) REFERENCES User(user_Name)),
                message TEXT,
                message_Send_Time INTEGER
            """)
    conn.commit()

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    userName = requests.form['userName']
    user_Password=requests.form['user_Password']
    user_Email=requests.form['user_Email']
    user_Rank=requests.form['user_Rank']
    user_Age=requests.form['user_Age']
    user_First_Name=requests.form['user_First_Name']
    user_Last_Name=requests.form['user_Last_Name']
    c.execute("""INSERT INTO Attendee VALUES('?','?','?','?','?','?','?')""",userName,user_Password,user_Email,user_Rank,user_Age,user_First_Name,user_Last_Name)

@app.route('/add_user_to_event', methods=['GET', 'POST'])
def add_user_to_event():

    event_ID = requests.form['event_ID']
    user_Name=requests.form['user_Name']

    c.execute("""INSERT INTO Attendee VALUES('?','?')""",event_ID,user_Name)
    #ADD NEW ENTITY TO Attendee

def get_age_by_user_name(user_name):
    c.execute("""SELECT user_Age FROM User WHERE user_Name =?""",(user_name))
    return c.fetchone()


def calc_distance(location):
   return 10


def get_events_by_user_name_and_location(user_name, location):
    age = get_age_by_user_name(user_name)
    print(age)
    c.execute()
    return

"""@app.route('/notes_getters', methods=['GET', 'POST'])
def notes_getters():
   if requests.method == 'POST':
      #f = request.files.getlist("file")
      userName = requests.form['userName']
      #return jsonify({'prediction': url_for('static', filename=f.filename)})
"""
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