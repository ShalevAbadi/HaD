from sqlite3.dbapi2 import Connection

from flask import Flask,request
import sqlite3
import requests
from Restrictions import Restrictions
from Rank import Rank
from Attendee import Attendee
from Event import Event
from User import User

app = Flask(__name__)

conn= sqlite3.connect("HaD.db")
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
            FOREIGN KEY(event_ID) REFERENCES Event(Event_ID),
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

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        userName = requests.form['userName']
        user_Password=requests.form['user_Password']#Delete????
        user_Email=requests.form['user_Email']
        user_Age=requests.form['user_Age']
        user_First_Name=requests.form['user_First_Name']
        user_Last_Name=requests.form['user_Last_Name']
        user=User(conn,userName,user_Password,user_Email,user_Age,user_First_Name,user_Last_Name)
        user.save_to_db()
        #c.execute("""INSERT or replace INTO User VALUES(?,?,?,?,?,?)""",(userName,user_Password,user_Email,user_Age,user_First_Name,user_Last_Name))
        #conn.commit()

@app.route('/insert_msg_to_chat', methods=['GET', 'POST'])
def insert_msg_to_chat():
    if request.method == 'POST':
        event_ID = requests.form['event_ID']
        user_Name= requests.form['user_Name']
        c.execute("""INSERT INTO Attendee Chat('?','?')""",event_ID,user_Name)

@app.route('/add_user_to_event', methods=['GET', 'POST'])
def add_user_to_event():
    if request.method == 'POST':
        event_ID = requests.form['event_ID']
        user_Name=requests.form['user_Name']
        attendee=Attendee(conn,event_ID,user_Name)
        attendee.save_to_db()
        #c.execute("""INSERT INTO Attendee VALUES('?','?')""",event_ID,user_Name)

@app.route('/get_user_data', methods=['GET', 'POST'])
def get_user_data():
    userName = requests.form['userName']
    userDetails=User.get_user_details(conn, userName)
    user=User(conn,userDetails[0],userDetails[1],userDetails[2],userDetails[3],userDetails[4],userDetails[5])
    return(user.to_json())


@app.route('/notes_getters', methods=['GET', 'POST'])
def notes_getters():
   if requests.method == 'POST':
      #f = request.files.getlist("file")
      userName = requests.form['userName']


count = 0
@app.route("/")
def home_page():
    if count == 0:
        count += 1
        return initialize_db_tables()
    else:
        return "hello barda"

app.run(debug=True)

