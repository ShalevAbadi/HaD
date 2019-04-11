from flask import Flask
import sqlite3
import requests
from Restrictions import Restrictions
from Rank import Rank
from Event import Event

app = Flask(__name__)

conn = sqlite3.connect("HaD.db")
c = conn.cursor()


def initialize_db_tables():

    c.execute("""CREATE TABLE IF NOT EXISTS User (
                user_Name text PRIMARY KEY,
                user_Password TEXT,
                user_Email   TEXT,
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

    c.execute("""CREATE TABLE IF NOT EXISTS Category(
            category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            category_Name TEXT)
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS Event(
            event_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            event_Manager TEXT,
            event_Name TEXT,
            event_Description TEXT,
            event_Picture BLOB,
            event_Start_Time INTEGER,
            event_End_Time INTEGER,
            event_Location_Lat INTEGER,
            event_Location_Lng INTEGER,
            event_Minimum_Participants INTEGER,
            event_Maximum_Participants INTEGER,
            restrictions_ID INTEGER,
            FOREIGN KEY(restrictions_ID) REFERENCES Restrictions(restrictions_ID),
            FOREIGN KEY(event_Manager) REFERENCES User(user_Name))
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS Attendee(
            event_ID INTEGER,
            user_Name TEXT,
            FOREIGN KEY(event_ID) REFERENCES Events(Event_ID),
            FOREIGN KEY(user_Name) REFERENCES User(user_Name))
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS Chat(
                message TEXT,
                message_Send_Time INTEGER,
                event_ID INTEGER,
                user_Name TEXT,
                FOREIGN KEY(event_ID) REFERENCES Events(Event_ID),
                FOREIGN KEY(user_Name) REFERENCES User(user_Name))
            """)

    c.execute("""CREATE TABLE IF NOT EXISTS Rank (
                 rank_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_Name TEXT,
                 rank_Point   INTEGER,
                 rank_Description    TEXT,
                 FOREIGN KEY(user_Name) REFERENCES User(user_Name))
                 """)
    conn.commit()

#@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    #userName = requests.form['userName']

    #MOCKING
    userName="KAKI"
    user=get_user_details(userName)

    user_Password=user[1]
    user_Email=user[2]
    user_Rank=user[3]
    user_Age=user[4]
    user_First_Name=user[5]
    user_Last_Name=user[6]
    c.execute("""INSERT INTO User VALUES('{}','{}','{}','{}','{}','{}','{}')""".format(userName,user_Password,user_Email,user_Rank,user_Age,user_First_Name,user_Last_Name))



#@app.route('/insert_msg_to_chat', methods=['GET', 'POST'])
def insert_msg_to_chat():
    event_ID = requests.form['event_ID']
    user_Name= requests.form['user_Name']
    c.execute("""INSERT INTO Attendee Chat('?','?')""",event_ID,user_Name)

#@app.route('/add_user_to_event', methods=['GET', 'POST'])
def add_user_to_event():

    event_ID = requests.form['event_ID']
    user_Name=requests.form['user_Name']

    c.execute("""INSERT INTO Attendee VALUES('?','?')""",event_ID,user_Name)
    #ADD NEW ENTITY TO Attendee

#@app.route('/add_user_to_event', methods=['GET', 'POST'])
def add_user_to_event():
    event_ID = requests.form['event_ID']
    user_Name = requests.form['user_Name']
    c.execute("""INSERT INTO Attendee Chat('?','?')""", event_ID, user_Name)
    # ADD NEW ENTITY TO Attendee

#USER METHODS
def get_age_by_user_name(user_name):
    c.execute("""SELECT user_Age FROM User WHERE user_Name =?""",(user_name))
    return c.fetchone()

def get_user_details(user_name):
    c.execute("""SELECT * FROM User WHERE user_Name = '{}'""".format(user_name))
    return c.fetchone()
#

def calc_distance(location):
   return 10


def get_events_by_user_name_and_location(user_name, location):
    age = get_age_by_user_name(user_name)
    print(age)
    c.execute()
    return

def create_rank():

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


initialize_db_tables()
#create_user()
#restrictions = Restrictions(conn, None, 10, 20, 'male', 'abasdbasdjasdasd')
#event = Event(conn, None, "tom", 'pizze', 'Friday morning pizze with tom', None, '12:00', '14:00', 33.078850, 33.783135, 2, 5, restrictions)
for i in Event.init_events_list_from_db(conn, 30, 30):
    print(i.to_json())
    print(i.restrictions.to_json())
 #   print(i.manager_user_name)
  #  print(i.restrictions.description)
#event.save_to_db()