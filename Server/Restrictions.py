import sqlite3
import json


class Restrictions():

    def __init__(self,conn, id, min_age, max_age, sex, description):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.id = id
        self. min_age = min_age
        self.max_age = max_age
        self.sex = sex
        self.description = description

    def save_to_db(self):
        self.cursor.execute("""INSERT INTO Restrictions VALUES(null, ?,?,?,?)""", (self.min_age, self.max_age, self.sex, self.description))
        self.cursor.execute("SELECT last_insert_rowid()")
        temp = self.cursor.fetchone()
        self.id = temp[0]
        self.conn.commit()

    def to_json(self):
        return json.dumps({"restrictions_id" : self.id, "min_age" : self.min_age, "max_age" : self.max_age, "sex" : self.sex, "description" : self.description})

    @staticmethod
    def get_from_db(conn, restriction_id):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Restrictions WHERE restrictions_ID=?""", (restriction_id,))
        res = cursor.fetchone()
        return Restrictions(conn, res[0], res[1], res[2], res[3], res[4])

