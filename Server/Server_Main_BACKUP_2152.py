from flask import Flask
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect("HaD.db")
c = conn.cursor()


def initialize_db_tables():

    c.execute("""CREATE TABLE IF NOT EXISTS User (
                user_Name text PRIMARY KEY,
                user_password TEXT,
                user_email   TEXT,
                user_rank    REAL,
                user_first_Name TEXT,
                user_last_Name    TEXT
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Restrictions (
                 Rest_ID INTEGER PRIMARY KEY AUTOINCREMENT,
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

<<<<<<< HEAD
=======
@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    userName = requests.form['userName']
    c.execute("""SELECT user_Age FROM User""")
    c.execute("""INSERT INTO Users VALUES('KAKI','1234','kaki@gmail.com','3','kaki','kaka')""")
>>>>>>> 087e3d4dac41280b022e3c144ba286133188065d

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