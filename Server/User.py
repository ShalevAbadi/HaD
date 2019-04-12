import sqlite3
import json


class User:
    def __init__(self,conn, user_Name, user_Password, user_Email, user_Age, user_First_Name, user_Last_Name):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.user_Name = user_Name
        self.user_Password = user_Password
        self.user_Email = user_Email
        self.user_Age = user_Age
        self.user_First_Name = user_First_Name
        self.user_Last_Name = user_Last_Name

    def to_json(self):
        return(json.dumps({'user_Name':self.user_Name,'user_Password':self.user_Password,'user_Email':self.user_Email,'user_Age':self.user_Age,'user_First_Name':self.user_First_Name,'user_Last_Name':self.user_Last_Name}))

    def save_to_db(self):
        self.cursor.execute("""INSERT INTO User VALUES('?','?','?','?','?','?')""",(
                            self.user_Name, self.user_Password,self.user_Email,self.user_Age,self.user_First_Name,self.user_Last_Name))
        self.conn.commit()

    @staticmethod
    def get_age_by_user_name(conn,user_name):
        cursor = conn.cursor()
        cursor.execute("""SELECT user_Age FROM User WHERE user_Name =?""", (user_name))
        return cursor.fetchone()

    @staticmethod
    def get_user_details(conn,user_name):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM User WHERE user_Name = '{}'""".format(user_name))
        return cursor.fetchone()
