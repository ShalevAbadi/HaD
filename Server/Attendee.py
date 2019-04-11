import sqlite3

class Attendee:

    def __init__(self,conn,event_ID,user_Name):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.event_ID = event_ID
        self.user_Name = user_Name

    def save_to_db(self):
        self.Event.save_to_db()
        self.User.save_to_db()
        self.cursor.execute("""INSERT INTO Attendee VALUES(?,?)""",(self.event_ID, self.user_Name))
        self.conn.commit()

    #@staticmethod
