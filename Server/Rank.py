import json


class Rank:

    def __init__(self,conn,id, user_name, points, description):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.id = id
        self.user_name = user_name
        self.points = points
        self.description = description

    def save_to_db(self):
        self.cursor.execute("""INSERT INTO Rank VALUES(null,?,?,?)""", (self.user_name, self.points, self.description))
        self.cursor.execute("SELECT last_insert_rowid()")
        temp = self.cursor.fetchone()
        self.id = temp[0]
        self.conn.commit()

    def to_json(self):
        return json.dumps({"rank_id" : self.id, "user_name" : self.user_name, "points": self.points, "description" : self.description})

    @staticmethod
    def get_user_ranks(conn, user_name):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Rank WHERE user_Name=?""", (user_name,))
        res_list = []
        for res in cursor:
            res_list.append(Rank(conn, res[0], res[1], res[2], res[3]))
        return res_list

    @staticmethod
    def calc_avg_rank(ranks):
        sum = 0
        for rank in ranks:
            sum+= rank.points
        return sum/len(ranks)

    @staticmethod
    def get_user_avg_rank(conn, user_name):
        user_ranks = Rank.get_user_ranks(conn, user_name)
        return Rank.calc_avg_rank(user_ranks) if user_ranks > 0 else 0
