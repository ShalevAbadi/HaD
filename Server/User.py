import sqlite3

class User:
    def _init_(self,conn, user_Name, user_Password, user_Email, user_Rank, user_Age, user_First_Name, user_Last_Name):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.user_Name = user_Name
        self.user_Password = user_Password
        self.user_Email = user_Email
        self.user_Rank = user_Rank
        self.user_Age = user_Age
        self.user_First_Name = user_First_Name
        self.user_Last_Name = user_Last_Name

    def save_to_db(self):
        self.rank.save_to_db()
        self.restrictions.save_to_db()
        self.cursor.execute("""INSERT INTO User VALUES('?','?','?','?','?','?','?')""",
                            self.user_Name, self.user_Password,self.user_Email,self.user_Rank,self.user_Age,self.user_First_Name,self.user_Last_Name)
        self.conn.commit()

    @staticmethod
    def get_age_by_user_name(user_name,conn):
        cursor = conn.cursor()
        cursor.execute("""SELECT user_Age FROM User WHERE user_Name =?""", (user_name))
        return cursor.fetchone()

    @staticmethod
    def get_user_details(user_name,conn):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM User WHERE user_Name = '{}'""".format(user_name))
        return cursor.fetchone()