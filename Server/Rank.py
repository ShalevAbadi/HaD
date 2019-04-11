class Rank:

    def __init__(self,conn,id, user_name, points, description):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.id = id
        self.user_name = user_name
        self.points = points
        self.description = description

    def save_to_db(self):
        self.cursor.execute("""INSERT INTO Event VALUES('?','?', '?')""", (self.user_name, self.points, self.description))
        self.conn.commit()

    @staticmethod
    def get_user_ranks(conn, user_name):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Restrictions WHERE user_Name=?""", user_name)
        res_list = []
        for res in cursor:
            res_list.append(Rank(conn, res[0], res[1], res[2], res[3]))
        return res_list

    @staticmethod
    def calc_avg_rank(ranks):
        sum = 0
        for rank in ranks:
            sum+= rank.points
        return sum/len(rank)